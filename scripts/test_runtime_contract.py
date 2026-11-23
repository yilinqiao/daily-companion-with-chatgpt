"""Regression contracts for the v0.4.1 runtime split (not end-to-end AI tests)."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class RuntimeContracts(unittest.TestCase):
    def test_onboarding_bootstrap_uses_closed_questionnaire(self):
        setup = (ROOT / 'System/setup.md').read_text()
        prompt = setup.split('```text\n', 1)[1].split('\n```', 1)[0]
        self.assertIn('Do not invent questions', prompt)
        self.assertIn('If the setup text still cannot be read, stop', prompt)
        self.assertIn('Ask for my approval before installation or scheduled task activation', prompt)
        for metadata in ('VERSION', 'CHANGELOG', 'SHA'):
            self.assertNotIn(metadata, prompt)
        for name in ('README.md', 'docs/setup-guide.html'):
            self.assertIn(prompt, (ROOT / name).read_text())
        self.assertIn('closed questionnaire', setup)
        self.assertIn('preserve valid confirmed answers', setup)

    def test_onboarding_and_installation_do_not_require_release_metadata(self):
        setup = (ROOT / 'System/setup.md').read_text()
        questionnaire = setup.split('## 1. Onboarding', 1)[0]
        gate = setup.split('## 2. Check connectors and approve setup', 1)[1].split('### Google Calendar', 1)[0]
        self.assertIn('System/setup.md only', questionnaire)
        self.assertIn('conversation-only', questionnaire)
        self.assertIn('no private writes', questionnaire)
        self.assertIn('missing or inconsistent release metadata alone does not block setup', gate)
        self.assertIn('required files', gate)
        self.assertIn('before any private installation write', gate)
        self.assertIn('preserve valid confirmed answers', gate)
        self.assertIn('no writes or task activation', gate.lower())
        for backend in ('notion', 'github'):
            guide = (ROOT / f'System/setup/{backend}.md').read_text()
            self.assertIn('unknown installed markers may remain null', guide)

    def test_installation_sources_are_ready_before_approval(self):
        setup = (ROOT / 'System/setup.md').read_text()
        prompt = setup.split('```text\n', 1)[1].split('\n```', 1)[0]
        self.assertIn('Raw URL', prompt)
        self.assertIn('GitHub connector', prompt)
        for name in ('README.md', 'docs/setup-guide.html'):
            self.assertIn(prompt, (ROOT / name).read_text())
        pages = 'https://yilinqiao.github.io/daily-companion-with-chatgpt/'
        self.assertIn(pages + 'setup.html', prompt)
        self.assertLess(prompt.index(pages), prompt.index('Raw URL'))
        preflight = setup.split('## 2. Check connectors and approve setup', 1)[1].split('### Google Calendar', 1)[0]
        self.assertIn(pages, preflight)
        self.assertLess(preflight.index(pages), preflight.index('Raw URL'))
        for phrase in ('before requesting installation approval', 'complete contents', 'Raw URL', 'GitHub connector'):
            self.assertIn(phrase, preflight)
        initialization = setup.split('## 3. Initialize selected storage and verify readiness', 1)[1].split('## 4.', 1)[0]
        for phrase in ('reuse the verified source contents', 'without repeating approval', 'unless the approved plan changes'):
            self.assertIn(phrase, initialization)

    def test_onboarding_zip_fallback_and_user_questions(self):
        setup = (ROOT / 'System/setup.md').read_text()
        prompt = setup.split('```text\n', 1)[1].split('\n```', 1)[0]
        self.assertIn('https://github.com/yilinqiao/daily-companion-with-chatgpt/archive/refs/heads/main.zip', prompt)
        self.assertIn('upload', prompt)
        for phrase in ('High', 'if available', 'uploaded public ZIP', 'do not execute', 'user may ask questions at any point', 'pending unanswered question'):
            self.assertIn(phrase, setup)
        preflight = setup.split('## 2. Check connectors and approve setup', 1)[1].split('### Google Calendar', 1)[0]
        self.assertIn('uploaded public ZIP', preflight)

    def test_notion_persistent_tool_permission_is_optional_and_scoped(self):
        guide = (ROOT / 'System/setup/notion.md').read_text()
        for phrase in ('Allow ChatGPT to use Notion', 'Always allow', 'if offered', 'does not replace explicit installation approval', 'scheduled task activation'):
            self.assertIn(phrase, guide)

    def test_day_planning_question_keeps_existing_fields(self):
        setup = (ROOT / 'System/setup.md').read_text()
        question = next(line for line in setup.splitlines() if line.startswith('4. '))
        for phrase in ('Daily planning window', 'help you plan your day', '07:00–21:00', 'planning_window_start', 'planning_window_end', 'never default either to null', 'Fixed working hours'):
            self.assertIn(phrase, question)

    def test_live_notion_daily_source_combined(self):
        guide = (ROOT / 'System/setup/notion.md').read_text()
        runtime = (ROOT / 'System/storage/notion.md').read_text()
        setup = (ROOT / 'System/setup.md').read_text()
        for phrase in ('MUST share one Daily Companion data source', 'single-select Category',
                       'Category (**select**', 'Created time', 'Last edited time',
                       'Legacy Drive URL', 'Daily Briefing & Memory',
                       'Last 7 days', 'Ledger Audit (All)', '**Action Ledger**'):
            self.assertIn(phrase, guide)
        self.assertIn('ONE shared `Daily Companion` source', runtime)
        self.assertIn('ONE shared Daily Companion source', setup)
        self.assertIn('**Plan** means the existing **Action Ledger**', guide)
        self.assertIn('not a fourth database', guide.lower())
        self.assertIn('do not create a fourth plan database', setup.lower())
        self.assertIn('Plan / tasks / projects', (ROOT / 'README.md').read_text())
        self.assertIn('No additional Plan database is created.', (ROOT / 'docs/GETTING_STARTED.md').read_text())
        self.assertIn('there is no fourth Plan database', (ROOT / 'docs/setup-guide.html').read_text())
        self.assertNotIn('Category (multi-select: Morning briefing, Evening memory', guide)

    def test_notion_signup_at_storage_choice(self):
        setup = (ROOT / 'System/setup.md').read_text()
        choice = next(line for line in setup.splitlines() if line.startswith('7. Storage choice:'))
        for phrase in ('no Notion account', 'Google account', 'setup/notion.md'):
            self.assertIn(phrase, choice)
        notion = (ROOT / 'System/setup/notion.md').read_text()
        for phrase in ('https://app.notion.com/signup', 'Continue with Google', 'Never ask for credentials or verification codes', 'harmless scoped read'):
            self.assertIn(phrase, notion)

    def test_saved_checkpoint_is_not_confirmation(self):
        morning = (ROOT / 'System/workflows/morning.md').read_text()
        self.assertIn('saved Daily Memory with positive evidence', morning)
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
