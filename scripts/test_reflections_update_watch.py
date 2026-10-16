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

    def test_reflections_need_approval_and_reliable_date(self):
        for phrase in ("## Reflections", "reliably dated cross-chat context",
                       "user approval"):
            self.assertIn(phrase, self.artifacts)
        for phrase in ("same-day cross-chat", "normal approval-based save",
                       "do not add a required fourth question"):
            self.assertIn(phrase, self.evening)
        self.assertIn("3. Anything else from today worth capturing?", self.setup)

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


if __name__ == "__main__":
    unittest.main()
