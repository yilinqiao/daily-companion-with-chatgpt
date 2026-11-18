"""Static regression sentinels; scenario execution still requires runtime review."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class BehavioralContracts(unittest.TestCase):
    def require(self, path, *phrases):
        contents = (ROOT / path).read_text()
        for phrase in phrases:
            self.assertIn(phrase, contents, path)

    def test_recovery_requires_positive_coverage(self):
        self.require('System/workflows/morning.md', 'positive evidence',
                     'candidate reconciliation', 'each examined date', 'cap at 7')

    def test_runtime_notion_mapping(self):
        self.require('System/storage/notion.md', 'File name', 'As of',
                     'Morning briefing', 'Evening memory', 'Opened', 'Closed On',
                     'Standing Until', 'System file name', 'Task ID')

    def test_evening_failure_and_fresh_state(self):
        self.require('System/workflows/evening.md', 'auto-save fails or is unauthorized',
                     'fresh-read the Ledger after answers', 'no authoritative inferred Ledger delta')

    def test_stale_approval(self):
        self.require('System/policies/artifacts.md', 'fresh-read private instructions',
                     'seek fresh approval', 'without broad source refresh')

    def test_extra_failure_is_not_silence(self):
        self.require('System/daily_companion_extra.md', 'report a material failure',
                     'before anchor, or not the chosen weekday, stop silently')

    def test_upgrade_pins_and_labels(self):
        self.require('System/upgrade.md', 'same immutable candidate SHA',
                     'stop on downgrade', 'installed_template_version to the verified candidate semver',
                     'leave suspended tasks suspended')
        self.require('System/setup/github.md', 'match the pinned upstream')

    def test_maintenance_registry(self):
        self.require('System/maintenance.md', 'docs/BEHAVIORAL_CONTRACTS.md')
        registry = (ROOT / 'docs/BEHAVIORAL_CONTRACTS.md').read_text()
        for number in range(1, 17):
            self.assertIn(f'BC-{number:02d}', registry)
        self.assertIn('not a runtime dependency', registry)


if __name__ == '__main__':
    unittest.main()
