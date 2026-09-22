import os, re
wiki_dir = '/home/runner/work/elsa-core/elsa-core/doc/wiki'
broken = []
for fname in sorted(os.listdir(wiki_dir)):
    if not fname.endswith('.md'):
        continue
    fpath = os.path.join(wiki_dir, fname)
    content = open(fpath).read()
    links = re.findall(r'\[([^\]]*)\]\(([^)]+)\)', content)
    for text, url in links:
        if url.startswith('http') or url.startswith('#'):
            continue
        url_clean = url.split('#')[0]
        if not url_clean:
            continue
        abs_path = os.path.normpath(os.path.join(wiki_dir, url_clean))
        if not os.path.exists(abs_path):
            broken.append((fname, text, url))
if broken:
    for f, t, u in broken:
        print(f'{f}: [{t}]({u})')
else:
    print('OK')
