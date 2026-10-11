"""Compute only the requested week's date; never read or write vault files.

The caller supplies dates already resolved in the profile's local timezone.
This is a calculator, not a scheduler or proof of successful delivery.
"""
import argparse
from datetime import date, timedelta
import hashlib
import json
import re
import secrets


def _iso_date(value):
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise ValueError("Expected an ISO YYYY-MM-DD date")
    return date.fromisoformat(value)


def initialize(completed_date):
    """Fresh random seed and next Monday; persist only in approved setup."""
    start = completed_date + timedelta(days=7 - completed_date.weekday())
    return {"start_week": start.isoformat(), "schedule_seed": secrets.token_hex(16)}


def due_date(local_date, start_week, schedule_seed):
    """Stable pseudorandom date for this week, or None before activation."""
    start = _iso_date(start_week)
    if start.weekday() != 0:
        raise ValueError("start_week must be a Monday")
    if not isinstance(schedule_seed, str) or not re.fullmatch(r"[0-9a-f]{32}", schedule_seed):
        raise ValueError("Expected a 32-character lowercase hexadecimal seed")
    monday = local_date - timedelta(days=local_date.weekday())
    if monday < start:
        return None
    # Rejection sampling avoids the tiny bias from reducing all 256-bit
    # values modulo seven. A week is an input, never a stored calendar.
    limit = (1 << 256) - ((1 << 256) % 7)
    counter = 0
    while True:
        message = f"daily-companion-v5|{schedule_seed}|{monday.isoformat()}|{counter}"
        value = int.from_bytes(hashlib.sha256(message.encode("ascii")).digest(), "big")
        if value < limit:
            return monday + timedelta(days=value % 7)
        counter += 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    init = commands.add_parser("init", help="Generate initial state without saving it")
    init.add_argument("--date", required=True, help="Setup completion date in profile timezone")
    due = commands.add_parser("due", help="Calculate only the current local week's date")
    due.add_argument("--date", required=True, help="Today's date in profile timezone")
    due.add_argument("--start-week", required=True)
    due.add_argument("--seed", required=True)
    args = parser.parse_args()
    try:
        local_date = _iso_date(args.date)
        if args.command == "init":
            output = initialize(local_date)
        else:
            result = due_date(local_date, args.start_week, args.seed)
            output = {"due_date": result.isoformat() if result else None,
                      "due_today": result == local_date}
    except ValueError as error:
        parser.error(str(error))
    print(json.dumps(output))


if __name__ == "__main__":
    main()
