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
        for guard in ("all three questions", "inviting a reply", "never sign off early",
                      "independent approval", "verified interactive save",
                      "scheduled run remains read-only"):
            self.assertIn(guard, prompt)

    def test_actual_task_prompt_has_the_three_questions_and_last_block_gate(self):
        task = self.setup.split("### Evening Companion task instruction", 1)[1]
        task = task.split("### Daily Companion Extra task instruction", 1)[0]
        for phrase in ("1. What got done today", "2. Did anything new open",
                       "3. Anything else from today", "configured output language",
                       "Closing Thought before these questions",
                       "Check the final answer for all three"):
            self.assertIn(phrase, task)

    def test_missing_source_does_not_remove_three_question_handoff(self):
        section = self.evening.split("**Scheduled handoff (mandatory on every run):**", 1)[1]
        section = section.split("## 5. Approval Handoff", 1)[0]
        for phrase in ("no changes", "source cannot be read", "Closing Thought",
                       "Do not sign off", "check the final lines"):
            self.assertIn(phrase.lower(), section.lower())

    def test_upgrade_checks_live_task_separately_from_repository(self):
        release = self.upgrade.split("For release 0.3.5", 1)[1].split("For release 0.3.4", 1)[0]
        for phrase in ("already-created Evening Scheduled Task", "all three capture questions",
                       "only with the user's explicit approval", "notification preferences",
                       "do not claim the scheduled-run fix is complete"):
            self.assertIn(phrase, release)

    def test_existing_installations_require_explicit_prompt_update(self):
        self.assertIn("For release 0.3.3 (Evening check-in completion guard)", self.upgrade)
        self.assertIn("only when explicitly requested", self.upgrade)


if __name__ == "__main__":
    unittest.main()
