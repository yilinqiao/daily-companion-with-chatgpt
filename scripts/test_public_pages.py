from html.parser import HTMLParser
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class TextContent(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.text = []
        self.feed(html)

    def handle_data(self, data):
        self.text.append(data)


class PublicPagesTests(unittest.TestCase):
    def test_build_mirrors_complete_public_rules_and_version(self):
        with tempfile.TemporaryDirectory() as tmp:
            site = Path(tmp) / "site"
            commit = "a" * 40
            subprocess.run([sys.executable, "-B", str(ROOT / "scripts/build_public_pages.py"),
                            str(site), "--commit", commit], check=True, cwd=ROOT)
            version = (ROOT / "VERSION").read_text().strip()
            self.assertEqual((site / "VERSION").read_text().strip(), version)
            self.assertIn(version, (site / "version.html").read_text())
            self.assertIn(commit, (site / "version.html").read_text())
            self.assertIn("System/setup.html", (site / "index.html").read_text())
            self.assertIn((ROOT / "System/setup.md").read_text(),
                          "".join(TextContent((site / "setup.html").read_text()).text))
            bundle = "".join(TextContent((site / "bundle.html").read_text()).text)
            for original in (ROOT / "System").rglob("*.md"):
                rel = original.relative_to(ROOT)
                self.assertEqual((site / rel).read_bytes(), original.read_bytes())
                readable = TextContent((site / rel.with_suffix(".html")).read_text()).text
                self.assertIn(original.read_text(), "".join(readable))
                self.assertIn(original.read_text(), bundle)
            self.assertEqual((site / "CHANGELOG.md").read_bytes(), (ROOT / "CHANGELOG.md").read_bytes())
            cover = Path("assets/daily-companion-cover.webp")
            self.assertEqual((site / cover).read_bytes(), (ROOT / cover).read_bytes())
            self.assertEqual((site / cover).read_bytes()[8:12], b"WEBP")
            self.assertFalse((site / "Daily").exists())
            self.assertFalse((site / ".git").exists())
            self.assertFalse((site / ".github").exists())
            self.assertFalse((site / "Archives").exists())

    def test_build_refuses_to_overwrite_an_existing_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            site = Path(tmp)
            sentinel = site / "existing.txt"
            sentinel.write_text("keep")
            result = subprocess.run([sys.executable, "-B", str(ROOT / "scripts/build_public_pages.py"), str(site)],
                                    capture_output=True, cwd=ROOT)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(sentinel.read_text(), "keep")


if __name__ == "__main__":
    unittest.main()
