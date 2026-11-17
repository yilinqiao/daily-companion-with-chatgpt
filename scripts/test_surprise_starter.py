"""Exercise the public checker against clean and accidentally initialized state."""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


BLANK = """---
type: companion-surprise-engine
schema_version: 7
enabled: true
anchor_monday: null
weekday_pattern: null
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

    def test_clean_pattern_starter_is_publishable(self):
        status, output = self.check(BLANK)
        self.assertEqual(status, 0, output)

    def test_initialized_anchor_is_not_publishable(self):
        self.assertEqual(self.check(BLANK.replace("anchor_monday: null", "anchor_monday: 2026-11-23"))[0], 1)

    def test_initialized_pattern_is_not_publishable(self):
        self.assertEqual(self.check(BLANK.replace("weekday_pattern: null", "weekday_pattern: " + "1" * 104))[0], 1)

    def test_legacy_scheduled_write_consent_is_not_publishable(self):
        self.assertEqual(self.check(BLANK.replace("enabled: true", "enabled: true\nscheduled_writes_authorized: true"))[0], 1)

    def test_duplicate_anchor_cannot_hide_initialized_state(self):
        state = BLANK.replace("anchor_monday: null", "anchor_monday: null\nanchor_monday: 2026-11-23")
        self.assertEqual(self.check(state)[0], 1)

    def test_duplicate_pattern_cannot_hide_initialized_state(self):
        state = BLANK.replace("weekday_pattern: null", "weekday_pattern: null\nweekday_pattern: " + "2" * 104)
        self.assertEqual(self.check(state)[0], 1)

    def test_legacy_claim_is_not_publishable(self):
        self.assertEqual(self.check(BLANK.replace("enabled: true", "enabled: true\ndelivery_status: claimed"))[0], 1)

    def test_missing_pattern_is_not_publishable(self):
        self.assertEqual(self.check(BLANK.replace("weekday_pattern: null\n", ""))[0], 1)

    def test_legacy_seed_cannot_be_shipped_as_new_state(self):
        self.assertEqual(self.check(BLANK.replace("enabled: true", "enabled: true\nschedule_seed: null\nstart_week: null"))[0], 1)

    def test_legacy_schema_cannot_be_shipped(self):
        self.assertEqual(self.check(BLANK.replace("schema_version: 7", "schema_version: 6"))[0], 1)


if __name__ == "__main__":
    unittest.main()
