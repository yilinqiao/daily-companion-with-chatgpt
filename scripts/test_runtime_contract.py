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
        gate = setup.split('### Step 3 of 5 · Your Storage', 1)[1].split('### Step 4 of 5', 1)[0]
        self.assertIn('System/setup.md only', questionnaire)
        self.assertIn('conversation-only', questionnaire)
        self.assertIn('no private writes', questionnaire)
        self.assertIn('missing or inconsistent release metadata alone does not block setup', gate)
        self.assertIn('required files', gate)
        self.assertIn('before any private installation write', gate)
        self.assertIn('preserve valid confirmed answers', gate.lower())
        self.assertIn('no writes or task activation', gate.lower())
        for backend in ('notion', 'github'):
            guide = (ROOT / f'System/setup/{backend}.md').read_text()
            self.assertIn('unknown installed markers may remain null', guide)

    def test_installation_sources_are_ready_before_approval(self):
        setup = (ROOT / 'System/setup.md').read_text()
        prompt = setup.split('```text\n', 1)[1].split('\n```', 1)[0]
        self.assertIn('Use the GitHub connector', prompt)
        self.assertIn('sign up with Google', prompt)
        self.assertIn('yilinqiao/daily-companion-with-chatgpt', prompt)
        for name in ('README.md', 'docs/setup-guide.html'):
            self.assertIn(prompt, (ROOT / name).read_text())
        preflight = setup.split('### Step 3 of 5 · Your Storage', 1)[1].split('### Step 4 of 5', 1)[0]
        for phrase in ('before requesting installation approval', 'complete contents', 'GitHub connector',
                       'default branch (main)', 'Reuse complete bodies already read', 'No SHA'):
            self.assertIn(phrase, preflight)
        initialization = setup.split('## 3. Initialize selected storage and verify readiness', 1)[1].split('## 4.', 1)[0]
        for phrase in ('reuse the verified source contents', 'without repeating approval', 'unless the approved plan changes'):
            self.assertIn(phrase, initialization)

    def test_connector_first_and_no_manual_upload_or_metadata_gate(self):
        setup = (ROOT / 'System/setup.md').read_text()
        prompt = setup.split('```text\n', 1)[1].split('\n```', 1)[0]
        for phrase in ('High', 'if available', 'GitHub connector', 'sign up with Google',
                       'do not ask me to upload files'):
            self.assertIn(phrase, prompt)
        for phrase in ('user may ask questions at any point', 'pending unanswered question',
                       'Notion users need only read access', 'Do not look up or verify a SHA for installation'):
            self.assertIn(phrase, setup)
        preflight = setup.split('### Step 3 of 5 · Your Storage', 1)[1].split('### Step 4 of 5', 1)[0]
        for phrase in ('System/setup/notion.md', 'System/storage/notion.md', 'GitHub connector',
                       'missing path', 'No SHA', 'no writes or task activation'):
            self.assertIn(phrase, preflight)
        for name in ('System/setup.md', 'README.md', 'docs/GETTING_STARTED.md', 'docs/setup-guide.html'):
            public_text = (ROOT / name).read_text()
            self.assertNotIn('archive/refs/heads/main.zip', public_text)
            self.assertNotIn('uploaded public ZIP', public_text)

    def test_notion_visual_defaults_are_optional_and_native(self):
        guide = (ROOT / 'System/setup/notion.md').read_text()
        runtime = (ROOT / 'System/storage/notion.md').read_text()
        setup = (ROOT / 'System/setup.md').read_text()
        for phrase in ('native `icon` = 🌿', 'assets/daily-companion-cover.png',
                       'System database: ⚙️', 'Daily Companion database: 📖', 'Action Ledger database: 📋',
                       'ONE combined parent-page `update_content` call', 'changing only the icon attribute', 'Skip reused/customized databases',
                       '📄 by default', 'gets 👤', 'System Index gets 🗂️',
                       'existing batch create-pages request', 'never a readiness or activation gate',
                       'Keep existing custom icons and covers', 'no separate retries or readiness gate'):
            self.assertIn(phrase, guide)
        for phrase in ('native `icon` = ☀️ for Morning Briefing or 🌙 for Evening Memory',
                       'Preserve existing icons on revisions or replay', 'no extra retries',
                       'actual body and identity verification remain required'):
            self.assertIn(phrase, runtime)
        self.assertIn('appearance is not a readiness gate', setup)

    def test_notion_setup_batches_and_avoids_redundant_verification(self):
        guide = (ROOT / 'System/setup/notion.md').read_text()
        setup = (ROOT / 'System/setup.md').read_text()
        upgrade = (ROOT / 'System/upgrade.md').read_text()
        for phrase in ('ONE native batch create-pages call', 'not twelve consecutive calls',
                       'Never truncate or summarize source bodies', 'retrying only genuinely missing pages',
                       'do not fetch it again merely to repeat verification',
                       'do not require a separate full-body fetch and comparison of every page',
                       'Profile, System index and a representative runtime System page',
                       'not independently compared full stored text',
                       'final separate update sets setup_complete:true and is read back',
                       'Do not repeat successful reads or writes on resume'):
            self.assertIn(phrase, guide)
        self.assertNotIn('Verify every System page body', guide)
        self.assertIn('create all missing System pages in one supported batch', setup)
        self.assertIn('GitHub retains its own existing read-back requirements', setup)
        self.assertIn('not a relaxation of normal runtime saves', upgrade)

    def test_notion_system_titles_are_suffix_free_but_index_preserves_paths(self):
        guide = (ROOT / 'System/setup/notion.md').read_text()
        runtime = (ROOT / 'System/storage/notion.md').read_text()
        setup = (ROOT / 'System/setup.md').read_text()
        upgrade = (ROOT / 'System/upgrade.md').read_text()
        for phrase in ('only the final `.md` suffix removed', 'System/workflows/morning',
                       'stable canonical logical path including `.md`', 'exact page ID',
                       'rather than creating duplicates'):
            self.assertIn(phrase, guide)
        self.assertIn('remove the final `.md` suffix', setup)
        self.assertIn('both legacy `.md` titles and suffix-free titles are supported', runtime)
        self.assertIn('Do not rename pages during scheduled runtime', runtime)
        self.assertIn('rename the same pages in place', upgrade)
        self.assertIn('unchanged IDs, bodies, index mappings and task destinations', upgrade)
        self.assertIn('not an upgrade blocker', upgrade)

    def test_notion_permission_reminder_is_proactive(self):
        guide = (ROOT / 'System/setup/notion.md').read_text()
        setup = (ROOT / 'System/setup.md').read_text()
        for phrase in ('Before the first Notion connector call', 'before the first approved Notion write', 'resumed installation', 'rather than Allow once', 'before invoking the tool'):
            self.assertIn(phrase, guide)
        self.assertIn('before the first Notion connector call', setup)
        self.assertIn('including resumed setup', setup)
        self.assertIn('Respect a declined or one-time permission', guide)

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
                       'exactly three independent databases', 'Daily Briefing & Memory',
                       'Last 7 days', 'Ledger Audit (All)', '**Action Ledger**'):
            self.assertIn(phrase, guide)
        self.assertIn('ONE shared `Daily Companion` source', runtime)
        self.assertNotIn('Legacy Drive URL', guide)
        self.assertNotIn('Legacy Drive URL', runtime)
        self.assertIn('private Notion parent page', guide)
        self.assertIn('Do not require the add-data-source capability', guide)
        self.assertIn('Do not mark setup complete or activate tasks with an unverified required structure', guide)
        self.assertIn('exactly three independent databases under it', setup)
        self.assertIn('existing single-database multi-source suites remain supported', runtime)
        self.assertIn('do not assume the suite ID is a database ID', runtime)
        self.assertIn('database IDs distinct from data source IDs', guide)
        upgrade = (ROOT / 'System/upgrade.md').read_text()
        self.assertIn('preserve existing properties, historical links and working mappings', upgrade)
        self.assertIn('Existing completed installations keep their working layouts', upgrade)
        self.assertIn('For paused, incomplete onboarding, retain confirmed answers', upgrade)
        self.assertIn('three independent databases', (ROOT / 'README.md').read_text())
        self.assertIn('three independent databases', (ROOT / 'docs/GETTING_STARTED.md').read_text())
        self.assertIn('three independent databases', (ROOT / 'docs/setup-guide.html').read_text())
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
        choice = next(line for line in setup.splitlines() if line.startswith('Storage choice:'))
        for phrase in ('no Notion account', 'Google account', 'setup/notion.md'):
            self.assertIn(phrase, choice)
        notion = (ROOT / 'System/setup/notion.md').read_text()
        for phrase in ('https://app.notion.com/signup', 'Continue with Google', 'Never ask for credentials or verification codes', 'harmless scoped read'):
            self.assertIn(phrase, notion)

    def test_onboarding_finishes_each_topic_in_stage_order(self):
        setup = (ROOT / 'System/setup.md').read_text()
        stages = ('### Step 1 of 5 · About You', '### Step 2 of 5 · Your Data Sources',
                  '### Step 3 of 5 · Your Storage', '### Step 4 of 5 · Your Daily Routine',
                  '## 2. Review & Launch (Step 5 of 5)')
        self.assertEqual([setup.index(s) for s in stages], sorted(setup.index(s) for s in stages))
        data = setup.split(stages[1], 1)[1].split(stages[2], 1)[0]
        self.assertLess(data.index('#### Google Calendar'), data.index('#### Gmail'))
        self.assertLess(data.index('#### Gmail'), data.index('#### Web and weather'))
        self.assertIn('complete its account selection', data)
        self.assertIn('do not add a mandatory capture-source question', data)
        storage = setup.split(stages[2], 1)[1].split(stages[3], 1)[0]
        self.assertIn('private destination selection and harmless access checks', storage)
        self.assertIn('before explicit installation approval', storage)
        review = setup.split(stages[4], 1)[1].split('## 3.', 1)[0]
        self.assertIn('do not re-ask confirmed account/destination questions', review)
        self.assertIn('Ask for explicit approval of actual setup writes', review)

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
