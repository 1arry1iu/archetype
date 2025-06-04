import os
import re
import sys

# Path to README
README_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'README.md')

with open(README_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

table_pattern = re.compile(r"\| Shorthand \| Prompt \| Function \|\n\|---\|---\|---\|\n((?:\|.*\n)+?)\n", re.MULTILINE)
match = table_pattern.search(content)
if not match:
    print('README table not found')
    sys.exit(1)

rows = [line.strip() for line in match.group(1).strip().split('\n') if line.strip()]
missing = []

for row in rows:
    # row like: | A's | [Archetypes](https://github.com/.../GPTs) | Useful/fun personas |
    parts = [p.strip() for p in row.strip('|').split('|')]
    if len(parts) < 3:
        continue
    prompt_field = parts[1]
    m = re.match(r"\[(.*?)\]\((.*?)\)", prompt_field)
    if not m:
        prompt = prompt_field
        link = ''
    else:
        prompt, link = m.groups()

    path = None
    if 'github.com' in link and '/archetype/' in link:
        # extract after /archetype/tree/main/ or /archetype/blob/main/
        m2 = re.search(r'/archetype/(?:tree|blob)/main/([^\)\#]+)', link)
        if m2:
            path = m2.group(1)
    if not path:
        # fallback to prompt name
        path = prompt

    local_path = os.path.join(os.path.dirname(README_PATH), path)
    if not os.path.exists(local_path):
        missing.append(path)

if missing:
    print('Missing paths:', ', '.join(missing))
    sys.exit(1)

print('All README categories exist.')
