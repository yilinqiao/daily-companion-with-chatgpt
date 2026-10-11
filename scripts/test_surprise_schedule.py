"""Regression checks for the read-only, one-week-at-a-time schedule."""
from datetime import date, timedelta
import unittest
from unittest.mock import patch

from surprise_schedule import due_date, initialize


class SurpriseScheduleTests(unittest.TestCase):
    def test_published_calculation_vector(self):
        self.assertEqual(due_date(date(2026, 10, 12), "2026-10-12", "0" * 32), date(2026, 10, 12))

    def test_setup_starts_next_calendar_week(self):
        for day in range(7):
            completed = date(2026, 10, 5) + timedelta(days=day)
            state = initialize(completed)
            self.assertEqual(state["start_week"], "2026-10-12")
            self.assertEqual(len(state["schedule_seed"]), 32)
            self.assertIsNone(due_date(completed, **state))

    def test_same_date_all_week_and_no_state_mutation(self):
        state = {"start_week": "2026-10-12", "schedule_seed": "0" * 32}
        original = state.copy()
        monday = date(2026, 10, 12)
        results = {due_date(monday + timedelta(days=i), **state) for i in range(7)}
        self.assertEqual(len(results), 1)
        self.assertTrue(monday <= results.pop() <= monday + timedelta(days=6))
        self.assertEqual(state, original)

    def test_rolls_forward_without_expiry(self):
        state = {"start_week": "2026-10-12", "schedule_seed": "0" * 32}
        offsets = set()
        for i in range(600):
            monday = date(2026, 10, 12) + timedelta(weeks=i)
            due = due_date(monday, **state)
            self.assertTrue(monday <= due <= monday + timedelta(days=6))
            offsets.add((due - monday).days)
        self.assertEqual(offsets, set(range(7)))

    def test_year_boundary_and_leap_day(self):
        for monday in (date(2026, 12, 28), date(2028, 2, 28)):
            state = {"start_week": "2026-10-12", "schedule_seed": "1" * 32}
            self.assertEqual(due_date(monday, **state), due_date(monday + timedelta(days=6), **state))

    def test_rejects_invalid_state(self):
        for start, seed in (("2026-10-13", "0" * 32), ("20261012", "0" * 32),
                            ("2026-10-12", "not-a-seed"), (None, None)):
            with self.subTest(start=start, seed=seed), self.assertRaises(ValueError):
                due_date(date(2026, 10, 12), start, seed)

    def test_hash_rejection_removes_modulo_bias(self):
        class Digest:
            def __init__(self, value):
                self.value = value
            def digest(self):
                return self.value
        with patch("surprise_schedule.hashlib.sha256", side_effect=[Digest(b"\xff" * 32), Digest(b"\x00" * 32)]) as hashed:
            self.assertEqual(due_date(date(2026, 10, 12), "2026-10-12", "0" * 32), date(2026, 10, 12))
            self.assertEqual(hashed.call_count, 2)


if __name__ == "__main__":
    unittest.main()
