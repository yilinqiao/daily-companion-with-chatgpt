"""Regression contracts for the v0.4.1 runtime split (not end-to-end AI tests)."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class RuntimeContracts(unittest.TestCase):
    def test_saved_checkpoint_is_not_confirmation(self):
        morning = (ROOT / 'System/workflows/morning.md').read_text()
        self.assertIn('first successfully saved Daily Memory', morning)
        self.assertIn('not evidence of confirmation or closure', morning)
        self.assertIn('independent', morning.lower())

    def test_evening_reuses_saved_baseline(self):
        evening = (ROOT / 'System/workflows/evening.md').read_text()
        self.assertIn("today's saved Daily Briefing", evening)
        self.assertNotIn("today's approved Daily Briefing", evening)

    def test_diary_has_six_slots(self):
        artifacts = (ROOT / 'System/policies/artifacts.md').read_text()
        memory = artifacts.split('## 3. Daily Memory Schema')[1].split('## 4.')[0]
        headings = [line for line in memory.splitlines() if line.startswith('## ')]
        self.assertEqual(headings, ["## Today's Journal", '## Other Updates & Explorations',
                                   '## Carry Forward from Today', '## Saved Today — Slurped Pages',
                                   '## Reflections', '## Tomorrow — Gentle Heads-up'])

    def test_installation_not_runtime(self):
        for backend in ('notion', 'github'):
            self.assertTrue((ROOT / f'System/setup/{backend}.md').is_file())
            adapter = (ROOT / f'System/storage/{backend}.md').read_text()
            self.assertNotIn('## Setup and permission proof', adapter)
            self.assertNotIn('## Approved setup initialization', adapter)

    def test_read_only_surprise(self):
        engine = (ROOT / 'System/daily_companion_extra.md').read_text()
        self.assertIn('anchor_monday: null', engine)
        self.assertIn('weekday_pattern: null', engine)
        self.assertIn('modulo 104', engine)
        self.assertIn('no scheduled writes', engine.lower())
        self.assertNotIn('delivery_status:', engine)

    def test_notion_exact_identity_and_fresh_schema(self):
        adapter = (ROOT / 'System/storage/notion.md').read_text()
        for phrase in ('unfiltered', 'next_cursor', 'fresh schema', 'date + Category', 'Calendar ID'):
            self.assertIn(phrase, adapter)

    def test_fallback_questions_in_actual_prompt(self):
        setup = (ROOT / 'System/setup.md').read_text()
        prompt = setup.split('### Evening Companion task instruction')[1].split('### Daily Companion Extra task instruction')[0]
        for phrase in ('What got done today', 'Did anything new open', 'Anything else from today', 'no writes'):
            self.assertIn(phrase, prompt)

    def test_failed_initial_save_has_manual_path(self):
        adapter = (ROOT / 'System/storage/notion.md').read_text()
        self.assertIn('approved exact-date creation', adapter)
        self.assertIn('prove no existing row', adapter)
        morning = (ROOT / 'System/workflows/morning.md').read_text()
        self.assertIn('auto-save fails or is unauthorized', morning)

    def test_upgrade_requires_safe_non_atomic_writes(self):
        upgrade = (ROOT / 'System/upgrade.md').read_text()
        self.assertIn('suspend affected enabled tasks', upgrade)
        self.assertIn('changed since preview', upgrade)

    def test_capture_mapping_and_extra_readiness(self):
        profile = (ROOT / 'System/profile.md').read_text()
        self.assertIn('capture_source: null', profile)
        setup = (ROOT / 'System/setup.md').read_text()
        self.assertIn('persist the approved capture_source', setup)
        engine = (ROOT / 'System/daily_companion_extra.md').read_text()
        self.assertIn('setup_complete:true', engine)
        self.assertIn('quoted string', engine)
