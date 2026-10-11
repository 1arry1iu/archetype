"""Regression coverage for Markdown links, anchors and README inventory."""
from pathlib import Path
import tempfile
import unittest
import test_readme as validator


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.old_root = validator.ROOT
        validator.ROOT = self.root
        validator.read_document.cache_clear()
        self.addCleanup(self.restore)

    def restore(self):
        validator.ROOT = self.old_root
        validator.read_document.cache_clear()

    def write(self, name, contents):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(contents, encoding="utf-8")
        return path

    def check(self, markdown):
        source = self.write("README.md", markdown)
        validator.read_document.cache_clear()
        return validator.validate_links([source])

    def test_reference_links_and_titles(self):
        self.write("reference.md", "# Reference\n")
        self.assertEqual(self.check('[text][ref]\n\n[ref]: reference.md "Title"\n'), [])

    def test_parentheses_and_quoted_title(self):
        self.write("file (draft).md", "# Draft\n")
        self.assertEqual(self.check('[draft](file%20(draft).md "Title")\n'), [])

    def test_missing_image(self):
        self.assertIn("missing path", str(self.check("![image](missing.png)\n")))

    def test_ignore_fenced_code(self):
        self.assertEqual(self.check("```md\n[x](missing.md)\n```\n"), [])

    def test_duplicate_headings_and_cross_document_anchors(self):
        self.write("guide.md", "# Hello *World*\n# Hello World\n<a id=\"manual\"></a>\n")
        self.assertEqual(self.check("[one](guide.md#hello-world-1) [two](guide.md#manual)\n"), [])
        self.assertIn("missing anchor", str(self.check("[bad](guide.md#unknown)\n")))

    def test_same_repo_github_links(self):
        self.write("guide.md", "# Guide\n")
        self.assertEqual(self.check("[guide](https://github.com/1arry1iu/archetype/blob/main/guide.md#guide)"), [])

    def test_external_urls_ignored(self):
        self.assertEqual(self.check("[web](https://example.org/x)"), [])

    def test_path_escape(self):
        self.assertIn("escapes repository", str(self.check("[x](../../outside.md)")))

    def test_html_image(self):
        self.assertIn("missing path", str(self.check('<img src="missing.png">')))

    def test_inventory_missing_link(self):
        self.write("Prompts/A.md", "# A\n")
        self.write("README.md", "**Current inventory:** 1 Markdown specifications (1 standalone specialists and 0 Construct modules), 0 knowledge maps, 0 versioned ZIP distributions (0 GPT plugin archives and 0 Grok skill archives).\n")
        self.assertIn("missing standalone", str(validator.validate_inventory()))


if __name__ == "__main__":
    unittest.main()
