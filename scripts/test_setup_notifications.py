"""Guard first-run notification handoff and client-capability honesty."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class SetupNotificationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.setup = (ROOT / "System/setup.md").read_text(encoding="utf-8")
        cls.getting_started = (ROOT / "docs/GETTING_STARTED.md").read_text(encoding="utf-8")
        cls.guide = (ROOT / "docs/setup-guide.html").read_text(encoding="utf-8")
        cls.readme = (ROOT / "README.md").read_text(encoding="utf-8")
        cls.upgrade = (ROOT / "System/upgrade.md").read_text(encoding="utf-8")
        cls.engine = (ROOT / "System/daily_companion_extra.md").read_text(encoding="utf-8")

    def test_both_daily_tasks_have_completion_notification_handoff(self):
        handoff = self.setup.split("**First-run completion-notification handoff", 1)[1]
        for phrase in ("Morning Companion", "Evening Companion",
                       "Notify when complete", "Settings > Notifications",
                       "confirmed by user", "not verified"):
            self.assertIn(phrase, handoff)
        self.assertIn("Never infer this switch is enabled", handoff)

    def test_extra_default_notify_and_unverified_platform_noop_alerts(self):
        handoff = self.setup.split("**First-run completion-notification handoff", 1)[1]
        for phrase in ("Daily Companion Extra", "recommend turning it on for all three",
                       "Prioritize notification of a real Surprise", "condition-watch", "do not promise suppression",
                       "not a reason to reset"):
            self.assertIn(phrase, handoff)
        self.assertIn("before the date or already claimed, stop silently", self.engine)
        self.assertIn("If Auto Mode stops silently, do not notify the user.", self.setup)
        self.assertNotIn("do not recommend turning on", handoff)
        self.assertNotIn("should not produce alerts for routine silent checks", self.readme)

    def test_user_facing_guides_and_upgrade_keep_notifications_manual(self):
        for document in (self.getting_started, self.guide, self.readme):
            self.assertIn("Notify when complete", document)
            self.assertIn("Notifications", document)
        self.assertIn("notification guidance", self.upgrade)
        self.assertIn("no profile/state schema", self.upgrade)
        self.assertIn("For release 0.3.2 (Extra completion notification preference):", self.upgrade)
        for guide in (self.readme, self.getting_started, self.guide):
            self.assertIn("Extra", guide)
            self.assertIn("silent", guide)


if __name__ == "__main__":
    unittest.main()
