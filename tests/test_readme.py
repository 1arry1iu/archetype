from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

REPO_ROOT = Path(__file__).resolve().parents[1]
README_PATH = REPO_ROOT / "README.md"
REPOSITORY = "1arry1iu/archetype"
MARKDOWN_LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
HEADING_PATTERN = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)


def github_slug(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text).strip().lower()
    text = re.sub(r"[^\w\- ]", "", text, flags=re.UNICODE)
    text = re.sub(r"\s+", "-", text)
    return text


def readme_anchors(content: str) -> set[str]:
    anchors: set[str] = set()
    counts: dict[str, int] = {}
    for heading in HEADING_PATTERN.findall(content):
        base = github_slug(heading)
        count = counts.get(base, 0)
        anchor = base if count == 0 else f"{base}-{count}"
        counts[base] = count + 1
        anchors.add(anchor)
    return anchors


def local_target(raw_target: str) -> tuple[str | None, str]:
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1].strip()

    if target.startswith("#"):
        return "", unquote(target[1:])

    parsed = urlsplit(target)
    if parsed.scheme or target.startswith("//"):
        if parsed.scheme in {"http", "https"} and parsed.netloc == "github.com":
            prefix = f"/{REPOSITORY}/"
            if parsed.path.startswith(prefix):
                repo_path = parsed.path[len(prefix):]
                match = re.match(r"(?:blob|tree)/[^/]+/(.+)$", repo_path)
                if match:
                    return unquote(match.group(1)), unquote(parsed.fragment)
        return None, ""

    return unquote(parsed.path), unquote(parsed.fragment)


def validate_readme_links() -> list[str]:
    content = README_PATH.read_text(encoding="utf-8")
    anchors = readme_anchors(content)
    errors: list[str] = []

    for raw_target in MARKDOWN_LINK_PATTERN.findall(content):
        path_text, fragment = local_target(raw_target)
        if path_text is None:
            continue

        if path_text == "":
            target_path = README_PATH
        else:
            target_path = (README_PATH.parent / path_text).resolve()
            try:
                target_path.relative_to(REPO_ROOT.resolve())
            except ValueError:
                errors.append(f"link escapes repository: {raw_target}")
                continue

        if not target_path.exists():
            errors.append(f"missing path: {path_text or 'README.md'} (from {raw_target})")
            continue

        if fragment and target_path == README_PATH:
            if fragment not in anchors:
                errors.append(f"missing README anchor: #{fragment}")

    return errors


def main() -> int:
    errors = validate_readme_links()
    if errors:
        print("README local-link validation failed:")
        for error in sorted(set(errors)):
            print(f"- {error}")
        return 1

    print("All README local paths and anchors exist.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
