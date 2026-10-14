"""Static contract checks for the one-morning handled-information handoff.

These tests protect the Markdown instructions; actual LLM output still needs
production observation and cannot be proved by static CI.
"""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class MorningRepeatSuppressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rules = (ROOT / "System/policies/rules.md").read_text(encoding="utf-8")
        cls.morning = (ROOT / "System/workflows/morning.md").read_text(encoding="utf-8")
        cls.evening = (ROOT / "System/workflows/evening.md").read_text(encoding="utf-8")
        cls.artifacts = (ROOT / "System/policies/artifacts.md").read_text(encoding="utf-8")
        cls.workflow = (ROOT / ".github/workflows/public-template-check.yml").read_text(encoding="utf-8")

    def test_approved_memory_suppresses_handled_fyi_without_ledger_card(self):
        handoff = self.rules.split("### Yesterday handoff", 1)[1].split("### Dates", 1)[0]
        for condition in ("Yesterday's **approved Daily Memory**",
                          "handled information", "whether or not an issue has a Ledger card",
                          "Do not repeat an unchanged item anywhere in the next Briefing",
                          "including to say no action is needed"):
            self.assertIn(condition, handoff)

    def test_unresolved_card_does_not_disappear_on_mere_mention(self):
        handoff = self.rules.split("### Yesterday handoff", 1)[1].split("### Dates", 1)[0]
        self.assertIn("Mere mention of an unresolved Ledger item is not a decision", handoff)
        self.assertIn("its normal daily reminder remains", handoff)
        self.assertIn("Keep Ledger state unchanged", handoff)
        self.assertIn("resume ordinary open-item reminders afterward", handoff)
        self.assertIn("Prior Briefings suppress stale FYI/email replays, not the ordinary daily reminder of an unresolved Ledger card", self.morning)

    def test_due_revisit_requested_and_new_evidence_override_suppression(self):
        handoff = self.rules.split("### Yesterday handoff", 1)[1].split("### Dates", 1)[0]
        for exception in ("Today's due/revisit action", "requested reminder",
                          "material new evidence", "essential Calendar/source status"):
            self.assertIn(exception, handoff)

    def test_rolling_email_search_and_all_briefing_sections_dedupe(self):
        self.assertIn("rolling Gmail look-back does not make a previously handled, unchanged notice new", self.rules)
        self.assertIn("previously handled unchanged mail", self.morning)
        self.assertIn("scan **the entire Briefing**", self.morning)
        self.assertIn("including opening, Calendar, Weather and Flavour", self.morning)
        self.assertIn("earlier approved Briefings", self.morning)
        self.assertIn("Never use a priority, recap, or", self.morning)

    def test_one_operational_home_and_visible_now_coverage(self):
        self.assertIn("Give each substantive issue one primary home", self.morning)
        self.assertIn("verify every Visible Now card appears once", self.morning)
        self.assertIn("remaining Visible Now Action Ledger items", self.artifacts)
        self.assertIn("complete coverage of Visible Now active Ledger items", self.artifacts)

    def test_evening_records_handled_non_ledger_items_without_false_card(self):
        self.assertIn("including non-Ledger emails/FYIs", self.evening)
        self.assertIn("Do not confuse mere mentions with decisions or create Ledger cards from FYIs", self.evening)
        self.assertIn("explicit unresolved next steps go in", self.evening)

    def test_regressions_run_after_release_gate_failure(self):
        steps = self.workflow.split("      - name: Regression checks", 1)[1]
        self.assertIn("if: ${{ !cancelled() }}", steps)
        self.assertIn("python3 -B -m unittest discover -s scripts -p 'test_*.py'", steps)


if __name__ == "__main__":
    unittest.main()
