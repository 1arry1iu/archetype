from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

REPO_ROOT = Path(__file__).resolve().parents[1]
README_PATH = REPO_ROOT / 'README.md'
REPOSITORY_URL_PATTERN = re.compile(
    r'^https://github\.com/1arry1iu/archetype/(?:tree|blob)/main/(.+)$'
)
MARKDOWN_LINK_PATTERN = re.compile(r'(?<!!)\[[^]]+\]\(([^)]+)\)')

content = README_PATH.read_text(encoding='utf-8')

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

    local_path = REPO_ROOT / path
    if not local_path.exists():
        missing.append(path)

categories_pattern = re.compile(
    r"## Categories\n\n\| Category \| GPTs \|\n\|---\|---\|\n((?:\|.*\n)+?)\n",
    re.MULTILINE,
)
categories_match = categories_pattern.search(content)
if not categories_match:
    print('README categories table not found')
    sys.exit(1)

for target in MARKDOWN_LINK_PATTERN.findall(categories_match.group(1)):
    target = target.strip()
    repository_match = REPOSITORY_URL_PATTERN.match(target)

    if repository_match:
        path = repository_match.group(1)
    elif not urlsplit(target).scheme and not target.startswith(('#', '//')):
        path = target
    else:
        continue

    path = unquote(path.split('#', 1)[0].split('?', 1)[0])
    if not (REPO_ROOT / path).exists():
        missing.append(path)

if missing:
    print('Missing paths:', ', '.join(sorted(set(missing))))
    sys.exit(1)

print('All README paths and category links exist.')
