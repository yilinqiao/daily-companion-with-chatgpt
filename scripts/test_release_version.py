"""Release gate rejects incomplete or misleading version announcements."""
import unittest
from pathlib import Path
from types import SimpleNamespace

from check_release_version import comparison_base, release_problems


class ReleaseVersionTests(unittest.TestCase):
    def test_checked_in_version_has_current_dated_changelog(self):
        root = Path(__file__).resolve().parents[1]
        version = (root / "VERSION").read_text(encoding="utf-8").strip()
        notes = (root / "CHANGELOG.md").read_text(encoding="utf-8")
        self.assertEqual(release_problems(None, version, {"VERSION", "CHANGELOG.md"}, notes), [])

    def test_pr_release_gate_uses_full_base_without_checking_each_push(self):
        workflow = (Path(__file__).resolve().parents[1] / ".github/workflows/public-template-check.yml").read_text(encoding="utf-8")
        self.assertIn("push:\n    branches: [main]", workflow)
        self.assertIn("pull_request:\n    branches: [main]", workflow)
        self.assertIn("if: github.event_name == 'pull_request'", workflow)
        self.assertNotIn("github.event.before", workflow)

    def test_first_versioned_release(self):
        self.assertEqual(release_problems(None, "0.1.0", {"VERSION", "CHANGELOG.md", "System/upgrade.md"},
                                          "## 0.1.0 — 2026-10-11\n"), [])

    def test_instruction_edit_requires_bump(self):
        problems = release_problems("0.1.0", "0.1.0", {"System/instructions.md"},
                                    "## 0.1.0 — 2026-10-11\n")
        self.assertTrue(any("increase" in p for p in problems))

    def test_bump_requires_changed_notes(self):
        problems = release_problems("0.1.0", "0.1.1", {"VERSION", "System/instructions.md"},
                                    "## 0.1.1 — 2026-10-11\n")
        self.assertTrue(any("CHANGELOG.md must change" in p for p in problems))

    def test_release_header_must_match(self):
        problems = release_problems("0.1.0", "0.1.1", {"VERSION", "CHANGELOG.md"},
                                    "## 0.1.0 — 2026-10-11\n")
        self.assertTrue(any("dated entry" in p for p in problems))

    def test_no_downgrade(self):
        problems = release_problems("0.2.0", "0.1.9", {"VERSION", "CHANGELOG.md"},
                                    "## 0.1.9 — 2026-10-11\n")
        self.assertTrue(any("increase" in p for p in problems))

    def test_numeric_comparison(self):
        self.assertEqual(release_problems("0.1.9", "0.1.10", {"VERSION", "CHANGELOG.md"},
                                          "## 0.1.10 — 2026-10-11\n"), [])

    def test_invalid_or_duplicate_release(self):
        for version, notes in (("v0.1.1", ""), ("0.01.1", ""),
                               ("0.1.1", "## 0.1.1 — 2026-10-11\n## 0.1.1 — 2026-10-11\n"),
                               ("0.1.1", "## 0.1.1 — 2026-02-30\n")):
            with self.subTest(version=version, notes=notes):
                self.assertTrue(release_problems("0.1.0", version, {"VERSION", "CHANGELOG.md"}, notes))

    def test_unchanged_commit_needs_no_release(self):
        self.assertEqual(release_problems("0.1.0", "0.1.0", set(), "## 0.1.0 — 2026-10-11\n"), [])

    def test_new_branch_with_history_requires_explicit_baseline(self):
        def git(*args):
            return SimpleNamespace(stdout="a" * 40 + " " + "b" * 40 + "\n")
        with self.assertRaisesRegex(ValueError, "reliable previous head"):
            comparison_base("0" * 40, git)

    def test_initial_repository_with_no_parent(self):
        self.assertIsNone(comparison_base("0" * 40, lambda *args: SimpleNamespace(stdout="a" * 40 + "\n")))

    def test_explicit_event_base_is_resolved(self):
        calls = []
        def git(*args):
            calls.append(args)
            return SimpleNamespace(stdout="c" * 40 + "\n")
        self.assertEqual(comparison_base("b" * 40, git), "c" * 40)
        self.assertIn("b" * 40 + "^{commit}", calls[0])


if __name__ == "__main__":
    unittest.main()
