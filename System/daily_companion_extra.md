---
type: companion-surprise-engine
schema_version: 7
enabled: true
anchor_monday: null
weekday_pattern: null
last_approved_auto_delivery: null
last_mode: null
last_type: null
recent_types: []
recent_themes: []
---

# Daily Companion Extra

Independent of Morning/Evening and Ledger. Read this private engine and profile only, plus narrow approved context if eligible. No scheduled writes on either backend.

## Initialization (interactive setup only)

Choose a private anchor_monday in the first complete local Monday–Sunday week after setup completion, and an arbitrary 104-character weekday_pattern (quoted string) using digits 1–7, one digit per week. Verify anchor Monday, valid local date, length and digits. Never reveal pattern or future dates. Preserve valid existing state on resume; only a fresh never-activated provisional anchor may be aligned if setup crosses weeks.

## Auto Mode

Require setup_complete:true, verified private backend/destination and profile; follow its approved sources, language and style. Use the actual scheduled occurrence local date in profile timezone, never delayed execution time. If occurrence, profile, engine or state is unavailable/invalid, disabled, before anchor, or not the chosen weekday, stop silently without output or writes. Compute elapsed whole weeks since anchor_monday, index modulo 104 (zero-based); compare pattern digit with local weekday (Monday=1, Sunday=7). Only matching dates qualify. Generate surprise using Creation Rules. No catch-up, delivery claim, date advancement, receipts or scheduled state updates. A retry could duplicate content; no exact-once claim.

## Manual Mode

For an explicit Surprise request, compose now even if paused; do not consume or change Auto cadence. No approval to continue.

## Interactive Controls

Use fresh state and selected adapter's private System write/verify boundary.

- Pause/resume changes only enabled; preserve anchor, pattern and feedback. If target ambiguous, clarify. Do not silently create or enable tasks.
- Invalid state needs an explicit approved repair, not automatic reinitialization.
- Save style feedback only on explicit request; retain up to five recent types/themes. Feedback is not delivery proof. Never expose future dates or pattern.

## Creation Rules

- Personal, not a recap: use specific ordinary details from the last 7–14 days of available approved context; if useful, read up to 3 recent Daily Memories and 1 relevant PARA note. No broad email/Calendar scan.
- No Ledger items, reminders, productivity coaching or disguised advice. Mood is a tone signal, not a therapy request.
- Warm, funny, tender, whimsical or curious; avoid generic praise, motivational clichés, forced sentiment and repetition. Vary forms, e.g. postcard, tiny letter, playful award, micro-story or museum label.
- Mostly text, sometimes a card or generated image when available; otherwise text. Content stays in conversation. Silence at workflow level does not guarantee platform notification suppression.

Legacy v6 claim/date state requires explicit upgrade per upgrade.md; preserve prior enabled/feedback and history. Never reset a live pattern.
