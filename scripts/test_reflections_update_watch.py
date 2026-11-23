"""Protect optional reflections, Sunday recap, and read-only version watch contracts."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReflectionAndWatchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.morning = (ROOT / "System/workflows/morning.md").read_text(encoding="utf-8")
        cls.evening = (ROOT / "System/workflows/evening.md").read_text(encoding="utf-8")
        cls.artifacts = (ROOT / "System/policies/artifacts.md").read_text(encoding="utf-8")
        cls.setup = (ROOT / "System/setup.md").read_text(encoding="utf-8")
        cls.upgrade = (ROOT / "System/upgrade.md").read_text(encoding="utf-8")

    def test_sunday_recap_is_date_scoped_and_tentative(self):
        self.assertIn("preceding local Monday–Saturday", self.morning)
        for slot in ("## This Week", "## Something You May Not Have Noticed"):
            self.assertIn(slot, self.artifacts)
        self.assertIn("never invent an insight", self.morning)

    def test_sunday_recap_required_even_with_missing_memories(self):
        for phrase in ("fetch every available Daily Memory body", "all six dates",
                       "before display or auto-save"):
            self.assertIn(phrase, self.morning)
        for phrase in ("required every Sunday", "even if no saved Memory is available",
                       "missing or inaccessible dates", "omit both weekly slots on other days"):
            self.assertIn(phrase, self.artifacts)
        self.assertIn("Sunday only and conditional", self.artifacts)

    def test_reflections_need_approval_and_reliable_date(self):
        for phrase in ("## Reflections", "reliably dated cross-chat context",
                       "user approval"):
            self.assertIn(phrase, self.artifacts)
        for phrase in ("same-day cross-chat", "normal approval-based save",
                       "do not add a required fourth question"):
            self.assertIn(phrase, self.evening)
        self.assertIn("3. Anything else from today worth capturing?", self.evening)

    def test_watch_is_read_only_and_asks_for_specific_approval(self):
        self.assertIn("Daily Companion Update Watch", self.setup)
        self.assertIn("06:00", self.setup)
        self.assertIn("## 0. Scheduled update watch (read-only)", self.upgrade)
        self.assertIn("must never modify", self.upgrade)
        self.assertIn("concrete diff", self.upgrade)
        self.assertIn("condition-watch", self.setup)
        self.assertIn("no-change checks", self.setup)

    def test_current_users_do_not_get_silent_new_task(self):
        self.assertIn("Existing installations are **not** silently given a new task", self.upgrade)
        self.assertIn("separately with explicit task-activation approval", self.upgrade)

    def test_watch_version_only_and_failure_threshold(self):
        watch = self.upgrade.split("## 0. Scheduled update watch (read-only)", 1)[1].split("## 1. Compare", 1)[0]
        for phrase in ("VERSION alone", "CHANGELOG is optional", "no commit SHA required",
                       "three consecutive daily failures", "reliably available run history",
                       "otherwise remain silent", "never write"):
            self.assertIn(phrase, watch)
        self.assertNotIn("one immutable default-branch commit", watch)
        self.assertNotIn("Only verified newer releases or material failure warrant output", self.setup)
        self.assertIn("Do not require an immutable candidate SHA", self.upgrade.split("## 1. Compare", 1)[1])

    def test_connector_first_watch_and_simple_actual_file_upgrade(self):
        watch = self.upgrade.split("## 0. Scheduled update watch (read-only)", 1)[1].split("## 1. Compare", 1)[0]
        self.assertIn("Use the GitHub connector first", watch)
        self.assertLess(watch.index("GitHub connector"), watch.index("Raw VERSION"))
        self.assertIn("https://yilinqiao.github.io/daily-companion-with-chatgpt/version.html", watch)
        self.assertIn("CHANGELOG is optional", watch)
        compare = self.upgrade.split("## 1. Compare", 1)[1].split("## 2. Propose", 1)[0]
        for phrase in ("Compare actual contents", "Do not require an immutable candidate SHA",
                       "installed baseline SHA", "no full-file diff", "missing paths", "no writes"):
            if phrase == "no full-file diff":
                self.assertIn("no mandatory full-file diff", compare)
            else:
                self.assertIn(phrase, compare)
        self.assertNotIn("same immutable candidate SHA", compare)
        self.assertIn("user may still approve the concrete rule changes without a known version", compare)
        apply = self.upgrade.split("## 3. Apply approved changes", 1)[1]
        self.assertIn("installed_template_commit is optional", apply)
        self.assertIn("fresh SHA for each approved file", apply)
        self.assertIn("Missing metadata alone is not a failed upgrade", apply)


if __name__ == "__main__":
    unittest.main()
