"""Protect the scheduled Evening check-in handoff from premature sign-off."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class EveningHandoffTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.evening = (ROOT / "System/workflows/evening.md").read_text(encoding="utf-8")
        cls.setup = (ROOT / "System/setup.md").read_text(encoding="utf-8")
        cls.upgrade = (ROOT / "System/upgrade.md").read_text(encoding="utf-8")
        cls.notion = (ROOT / "System/storage/notion.md").read_text(encoding="utf-8")
        cls.artifacts = (ROOT / "System/policies/artifacts.md").read_text(encoding="utf-8")

    def test_notion_initial_display_matches_verified_full_body_without_approval_preview(self):
        section = self.evening.split("## 4. Output Composition", 1)[1].split("## 5. Approval Handoff", 1)[0]
        for rule in (section, self.notion, self.artifacts):
            self.assertIn("complete user-visible body", rule)
            self.assertIn("ordinary chat", rule)
            self.assertIn("editable approval preview", rule)
        self.assertIn("no separate summary", section)
        self.assertIn("outside the body", section)
        self.assertIn("full safe draft", section)
        self.assertIn("GitHub is read-only", section)
        self.assertNotIn("no full Markdown draft yet", section)

    def test_scheduled_check_in_cannot_sign_off_before_questions(self):
        section = self.evening.split("Then ask these three general questions:", 1)[1]
        questions, following = section.split("## 5. Approval Handoff", 1)
        for prompt in ("1. What got done today", "2. Did anything new open",
                       "3. Anything else from today"):
            self.assertIn(prompt, questions)
        for guard in ("**Scheduled handoff (mandatory on every run):**", "invitation to reply here",
                      "Do not sign off", "wait for their reply"):
            self.assertIn(guard, questions)
        self.assertIn("After answers, compose the complete Daily Memory", following)

    def test_new_user_task_prompt_contains_stop_gate(self):
        prompt = self.setup.split("### Evening Companion task instruction", 1)[1]
        prompt = prompt.split("### Daily Companion Extra task instruction", 1)[0]
        for guard in ("all three required capture questions", "invite reply",
                      "independent approval", "current artifact and storage rules"):
            self.assertIn(guard, prompt)

    def test_actual_task_prompt_has_the_three_questions_and_last_block_gate(self):
        task = self.setup.split("### Evening Companion task instruction", 1)[1]
        task = task.split("### Daily Companion Extra task instruction", 1)[0]
        self.assertIn("workflows/evening.md", task)
        for phrase in ("1. What got done today", "2. Did anything new open",
                       "3. Anything else from today", "Closing Thought", "check the final lines"):
            self.assertIn(phrase, self.evening)
        for phrase in ("What got done today", "Did anything new open", "Anything else from today"):
            self.assertIn(phrase, task)

    def test_task_prompt_questions_are_unconditional_after_successful_save(self):
        prompt = self.setup.split("### Evening Companion task instruction", 1)[1]
        prompt = prompt.split("### Daily Companion Extra task instruction", 1)[0]
        for text in ("EVERY run", "success AND failure", "successful full-body Notion Auto-Saved",
                     "generic invitation", "check the final lines", "all source/status/link notes"):
            self.assertIn(text.lower(), prompt.lower())
        questions = ("1. What got done today", "2. Did anything new open",
                     "3. Anything else from today")
        positions = [prompt.index(q) for q in questions]
        self.assertEqual(positions, sorted(positions))
        for q in questions:
            self.assertEqual(prompt.count(q), 1)
        self.assertIn("independent approval", prompt)
        self.assertIn("GitHub Scheduled Evening remains read-only", prompt)

    def test_missing_source_does_not_remove_three_question_handoff(self):
        section = self.evening.split("**Scheduled handoff (mandatory on every run):**", 1)[1]
        section = section.split("## 5. Approval Handoff", 1)[0]
        for phrase in ("no changes", "source cannot be read", "Closing Thought",
                       "Do not sign off", "check the final lines"):
            self.assertIn(phrase.lower(), section.lower())

    def test_upgrade_checks_live_task_separately_from_repository(self):
        for phrase in ("actual existing task prompts", "all three Evening fallback questions",
                       "separately approved", "notification preferences", "observed status separately"):
            self.assertIn(phrase, self.upgrade)

    def test_existing_installations_require_explicit_prompt_update(self):
        self.assertIn("task changes and any migration", self.upgrade)
        self.assertIn("Never rerun setup", self.upgrade)


if __name__ == "__main__":
    unittest.main()
