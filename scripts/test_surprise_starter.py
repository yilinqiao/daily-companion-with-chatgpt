"""Exercise the public checker against clean and accidentally initialized state."""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


BLANK = """---
type: companion-surprise-engine
schema_version: 6
enabled: true
scheduled_writes_authorized: false
next_due_date: null
delivery_status: idle
delivery_due_date: null
delivery_claimed_at: null
last_attempt_date: null
last_approved_auto_delivery: null
last_mode: null
last_type: null
recent_types: []
recent_themes: []
---
"""


class SurpriseStarterTests(unittest.TestCase):
    def check(self, state):
        source = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory(prefix="companion-starter-", dir=source.parent) as name:
            target = Path(name) / "template"
            shutil.copytree(source, target, ignore=shutil.ignore_patterns(".git", "__pycache__"))
            (target / "System/daily_companion_extra.md").write_text(state + "\nGeneric engine rules.\n", encoding="utf-8")
            result = subprocess.run([sys.executable, "-B", str(target / "scripts/check_public_release.py")],
                                    capture_output=True, text=True)
            return result.returncode, result.stdout

    def test_clean_single_date_starter_is_publishable(self):
        status, output = self.check(BLANK)
        self.assertEqual(status, 0, output)

    def test_initialized_date_is_not_publishable(self):
        self.assertEqual(self.check(BLANK.replace("next_due_date: null", "next_due_date: 2026-10-22"))[0], 1)

    def test_claimed_delivery_is_not_publishable(self):
        self.assertEqual(self.check(BLANK.replace("delivery_status: idle", "delivery_status: claimed"))[0], 1)

    def test_private_scheduled_write_consent_is_not_publishable(self):
        self.assertEqual(self.check(BLANK.replace("scheduled_writes_authorized: false", "scheduled_writes_authorized: true"))[0], 1)

    def test_duplicate_consent_cannot_hide_private_authorization(self):
        state = BLANK.replace("scheduled_writes_authorized: false", "scheduled_writes_authorized: false\nscheduled_writes_authorized: true")
        self.assertEqual(self.check(state)[0], 1)

    def test_duplicate_date_cannot_hide_initialized_state(self):
        state = BLANK.replace("next_due_date: null", "next_due_date: null\nnext_due_date: 2026-10-22")
        self.assertEqual(self.check(state)[0], 1)

    def test_claim_timestamp_is_not_publishable(self):
        self.assertEqual(self.check(BLANK.replace("delivery_claimed_at: null", "delivery_claimed_at: 2026-10-22T19:00:00+11:00"))[0], 1)

    def test_missing_claim_state_is_not_publishable(self):
        self.assertEqual(self.check(BLANK.replace("delivery_due_date: null\n", ""))[0], 1)

    def test_legacy_seed_cannot_be_shipped_as_new_state(self):
        self.assertEqual(self.check(BLANK.replace("enabled: true", "enabled: true\nschedule_seed: null\nstart_week: null"))[0], 1)

    def test_legacy_schema_cannot_be_shipped(self):
        self.assertEqual(self.check(BLANK.replace("schema_version: 6", "schema_version: 5"))[0], 1)


if __name__ == "__main__":
    unittest.main()
