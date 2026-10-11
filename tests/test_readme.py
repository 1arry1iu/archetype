"""Repository-wide Markdown links, anchors and README inventory validation."""
from collections import Counter
from functools import lru_cache
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "1arry1iu/archetype"
MARKDOWN = MarkdownIt("commonmark", {"html": True}).enable("table")


class HTMLReferences(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.anchors = set()
        self.targets = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.anchors.add(a["id"])
        if tag == "a" and a.get("name"):
            self.anchors.add(a["name"])
        if tag in {"a", "img"}:
            value = a.get("href" if tag == "a" else "src")
            if value:
                self.targets.append(value)

    handle_startendtag = handle_starttag


def github_slug(value):
    value = re.sub(r"[^\w\- ]", "", value.lower(), flags=re.UNICODE)
    return value.replace(" ", "-")


@lru_cache(maxsize=None)
def read_document(path):
    tokens = MARKDOWN.parse(path.read_text(encoding="utf-8"))
    anchors, links, counts = set(), [], Counter()
    for index, token in enumerate(tokens):
        if token.type == "heading_open" and index + 1 < len(tokens):
            inline = tokens[index + 1]
            if inline.type == "inline":
                title = "".join(t.content for t in (inline.children or []) if t.type in {"text", "code_inline"})
                slug = github_slug(title)
                occurrence = counts[slug]
                anchors.add(slug if occurrence == 0 else f"{slug}-{occurrence}")
                counts[slug] += 1
        if token.type == "html_block":
            parser = HTMLReferences()
            parser.feed(token.content)
            anchors.update(parser.anchors)
            links.extend((target, (token.map or [0])[0] + 1) for target in parser.targets)
        if token.type == "inline":
            line = (token.map or [0])[0] + 1
            for child in token.children or []:
                if child.type == "link_open" and child.attrGet("href"):
                    links.append((child.attrGet("href"), line))
                elif child.type == "image" and child.attrGet("src"):
                    links.append((child.attrGet("src"), line))
                elif child.type == "html_inline":
                    parser = HTMLReferences()
                    parser.feed(child.content)
                    anchors.update(parser.anchors)
                    links.extend((target, line) for target in parser.targets)
    return anchors, links


def local_target(source, raw_target):
    parsed = urlsplit(raw_target)
    path = parsed.path
    if parsed.scheme or parsed.netloc:
        if parsed.scheme != "https" or parsed.netloc.lower() != "github.com":
            return None
        prefix = f"/{REPOSITORY}/"
        if not path.startswith(prefix):
            return None
        match = re.fullmatch(r"(?:blob|tree)/main/(.+)", path[len(prefix):])
        if not match:
            return None
        path = match.group(1)
        target = ROOT / unquote(path)
    else:
        if path.startswith("//"):
            return None
        target = source.parent / unquote(path)
    return target.resolve(), unquote(parsed.fragment)


def validate_links(documents):
    errors = []
    for source in documents:
        _, links = read_document(source)
        for raw_target, line in links:
            info = local_target(source, raw_target)
            if info is None:
                continue
            target, fragment = info
            origin = f"{source.relative_to(ROOT)}:{line}"
            if not target.is_relative_to(ROOT):
                errors.append(f"{origin}: link escapes repository: {raw_target}")
            elif not target.exists():
                errors.append(f"{origin}: missing path: {raw_target}")
            elif fragment and target.suffix.lower() == ".md":
                anchors, _ = read_document(target)
                if fragment not in anchors:
                    errors.append(f"{origin}: missing anchor #{fragment} in {target.relative_to(ROOT)}")
    return errors


def validate_inventory():
    readme = ROOT / "README.md"
    content = readme.read_text(encoding="utf-8")
    found = re.search(r"\*\*Current inventory:\*\*(.+?)(?:\n\n|$)", content, re.S)
    if not found:
        return ["README.md: missing Current inventory summary"]
    summary = found.group(1)
    categories = {
        "standalone specialists": sorted((ROOT / "Prompts").glob("*.md")),
        "Construct modules": sorted((ROOT / "Prompts" / "Construct").glob("*.md")),
        "knowledge maps": sorted((ROOT / "Knowledge Maps").glob("*.md")),
        "GPT plugin archives": sorted((ROOT / "GPT Plugins").glob("*.zip")),
        "Grok skill archives": sorted((ROOT / "Grok Skills").glob("*.zip")),
    }
    counts = {name: len(paths) for name, paths in categories.items()}
    counts["Markdown specifications"] = counts["standalone specialists"] + counts["Construct modules"]
    counts["versioned ZIP distributions"] = counts["GPT plugin archives"] + counts["Grok skill archives"]
    errors = []
    for label, number in counts.items():
        display = label[:-1] if number == 1 and label.endswith("s") else label
        if not re.search(rf"\b{number}\s+{re.escape(display)}\b", summary):
            errors.append(f"README.md: inventory summary should state {number} {display}")
    _, refs = read_document(readme)
    linked = set()
    for ref, _ in refs:
        result = local_target(readme, ref)
        if result:
            linked.add(result[0])
    for category, files in categories.items():
        for file in files:
            if file.resolve() not in linked:
                errors.append(f"README.md: missing {category} inventory link: {file.relative_to(ROOT)}")
    return errors


def main():
    documents = sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)
    errors = validate_links(documents) + validate_inventory()
    if errors:
        print("Repository integrity validation failed:")
        for error in sorted(set(errors)):
            print(f"- {error}")
        return 1
    print(f"Validated Markdown links, anchors, and inventory across {len(documents)} documents.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
