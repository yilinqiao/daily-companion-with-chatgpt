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
                     'candidate reconciliation', 'each examined date', 'cap at 7',
                     'A newer complete date cannot hide an older gap')

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

    def test_evening_and_extra_have_independent_task_identity(self):
        setup = (ROOT / 'System/setup.md').read_text()
        activation = setup.split('## 4. Activate Scheduled Tasks', 1)[1]
        self.assertIn('Never combine Evening and Extra', activation)
        self.assertIn('report partial activation', activation)
        self.assertNotIn('### Combined Evening + Extra task instruction', activation)
        evening = activation.split('### Evening Companion task instruction', 1)[1].split('### Daily Companion Extra task instruction', 1)[0]
        self.assertIn('target date cannot be verified', evening)
        self.assertIn('no writes', evening)
        self.assertIn('ask these three questions', evening)
        self.require('System/upgrade.md', 'existing combined Evening + Extra',
                     'explicit task-activation approval', 'preserve Extra state')

    def test_upgrade_actual_contents_and_optional_labels(self):
        self.require('System/upgrade.md', 'Do not require an immutable candidate SHA',
                     'stop on downgrade', 'installed_template_version to the verified candidate semver',
                     'installed_template_commit is optional', 'fresh SHA for each approved file',
                     'leave suspended tasks suspended')
        self.require('System/setup/github.md', 'match the retrieved upstream source files')

    def test_setup_prefers_native_intelligent_ui(self):
        for path in ('System/setup.md', 'README.md', 'docs/setup-guide.html'):
            self.require(path, "Prefer ChatGPT's native Intelligent UI throughout onboarding whenever it improves the user experience. Use interactive choices, time selectors and confirmation controls where appropriate.")
        self.require('System/setup.md', 'Ask exactly one question per turn',
                     'obtain separate explicit task activation approval')
        self.require('docs/BEHAVIORAL_CONTRACTS.md', 'Prefer native Intelligent UI when useful')
        for path in ('System/setup.md', 'README.md', 'docs/setup-guide.html'):
            self.require(path, 'compact current-stage header', 'thin five-segment progress bar')

    def test_maintenance_registry(self):
        self.require('System/maintenance.md', 'docs/BEHAVIORAL_CONTRACTS.md')
        registry = (ROOT / 'docs/BEHAVIORAL_CONTRACTS.md').read_text()
        for number in range(1, 17):
            self.assertIn(f'BC-{number:02d}', registry)
        self.assertIn('not a runtime dependency', registry)


if __name__ == '__main__':
    unittest.main()
