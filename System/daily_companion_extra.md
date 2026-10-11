---
type: companion-surprise-engine
schema_version: 5
enabled: true
start_week: null
schedule_seed: null
last_approved_auto_delivery: null
last_mode: null
last_type: null
recent_types: []
recent_themes: []
---

# Companion Surprise Engine

This file owns Companion Surprise behaviour and its lightweight state. The frontmatter is mutable state; the body is the stable engine contract. Any state write must preserve the body and modify only defined fields in an authorized interactive turn. Scheduled runs remain strictly read-only.

## Cadence Contract

- Auto is enabled by default and plans one random local date per complete Monday–Sunday calendar week, starting in the week after setup finishes. Use the timezone in `System/profile.md`. No `approve` reply or weekly maintenance is required. Only an explicit pause/stop/disable request pauses Auto.
- Setup stores a fresh random 128-bit `schedule_seed` (32 lowercase hexadecimal characters) and `start_week` (the Monday after the local setup completion week) in this file. It does **not** generate or store a list of future dates. Keep the seed and chosen dates out of normal user-facing output. The seed is scheduling state, not an account credential.
- Each daily check calculates **only the current week's** date from the seed and that week's Monday. The result is deterministic within a week and pseudorandom across weeks, so daily checks cannot redraw the day. Every weekday has equal selection probability over a randomly chosen seed; consecutive weeks may legitimately choose the same weekday. This is not a fixed weekday or a 7–14 day interval.
- Use the pure, read-only calculator in `scripts/surprise_schedule.py`, or execute its exact algorithm in an available code tool: SHA-256 of ASCII `daily-companion-v5|<schedule_seed>|<week_monday_YYYY-MM-DD>|<counter>`, starting counter at 0; interpret the digest as an unsigned big-endian integer. Reject values at least `2^256 - (2^256 mod 7)` and increment the counter; otherwise use `value mod 7` as the Monday-based day offset. Do not approximate hashes, improvise dates, fetch a public hashing website with private state, or randomly draw again each day.
- A GitHub file read does not execute Python. Setup must check whether the scheduled environment can execute this calculation with a code tool; do not claim Auto is operational unless this capability is verified. If calculation is unavailable at runtime, stop silently. This calculator never starts tasks, sends notifications or modifies a file.
- A failed/missed due-day run is skipped without late catch-up. A planned weekly date is not a guarantee of delivery or notification receipt. Missing/malformed state stops Auto silently until an authorized interactive repair; there is no calendar expiry or renewal threshold.
- `enabled` controls Auto only. Manual Mode remains available while paused, and never consumes or reschedules an automatic surprise. Native ChatGPT Memory is not a scheduling input or reliable delivery marker.

## Auto Mode

Auto Mode is invoked only by the single daily `Daily Companion Extra` check.

1. Fresh-read this file and `System/profile.md` from the configured repository. If setup is incomplete, stop silently. Resolve today's local date in the configured timezone.
2. If `enabled: false`, stop silently. Require schema v5, a valid Monday ISO `start_week`, and a 32-character lowercase hexadecimal seed. Invalid state stops silently; never repair it in a scheduled run.
3. Resolve this week's Monday. Before `start_week`, stop silently. Calculate this week's due date using the exact calculator above; do not generate later weeks or persist the result.
4. If today is not that date, stop silently. Never trigger from an older date.
5. On a match, compose exactly one surprise under Creation Rules and render it. No approval question is needed. An optional brief line may say: **Say “pause surprises” any time to pause.** Silence and unrelated replies keep weekly Auto enabled.
6. Write nothing: no state update, Daily artifact, Ledger, Gmail or Calendar mutation. The next week's calculation uses its own Monday automatically.

A rerun on the same due day may duplicate output because read-only checks cannot persist a delivery marker. Keep exactly one daily task; do not add overlapping checks or automatically retry a completed due-day delivery.

## Manual Mode

The user must explicitly ask for a surprise, such as `surprise me` or an equivalent request in their language. Low mood alone is not such a request.

1. Fresh-read this file and compose one surprise immediately, including while Auto is paused.
2. Do not read, write or depend on Auto scheduling/feedback state. Use the current request and context for variety.
3. Mood/context is a tone signal, not a request for therapy, coaching or advice.
4. Render the surprise without an approval question.

## Interactive Controls

- **pause**, **pause surprises**, **stop surprise**, or a clear equivalent targeting Surprise: the request itself authorizes setting `enabled: false`. Fresh-read, write only that field, preserve seed/start/history, verify the write and confirm. A bare “pause” in a Surprise conversation counts; in a Morning/Evening or unrelated conversation, clarify the target rather than pausing the wrong feature. Manual Mode stays available.
- **resume surprises**: set `enabled: true` in an interactive turn, preserve the seed and start week, verify and confirm. Never redraw the current week or catch up missed dates. If today's calculated due date has already passed, wait for next week's date. Invalid state requires a specific authorized repair, not an automatic replacement.
- Feedback is optional. A clear request to remember a visible surprise's style may update `last_approved_auto_delivery`, `last_mode: auto`, `last_type`, `recent_types` and `recent_themes` (maximum five entries each), after read-back verification. These legacy feedback fields are not proof of every delivery and never control cadence. Do not solicit `approve` or treat it as a requirement for continuing Auto.
- If a requested write is blocked or cannot be verified, explain it without claiming the setting changed. Do not bypass a safety block.

## Creation Rules

- Make the result feel personal without becoming a recap. Prefer specific, ordinary details from roughly the last 7–14 days of already available context.
- If more context is needed, narrowly read up to 3 recent Daily Memories and at most 1 relevant PARA file. Do not broaden Gmail or Calendar retrieval just to manufacture emotional content.
- Never include Ledger items, reminders, follow-ups, productivity coaching or disguised advice unless explicitly requested instead of a surprise.
- Avoid generic praise, motivational cliches, forced sentiment and repetitive summaries. Warm, funny, tender, whimsical, curious or lightly absurd are all valid.
- Vary the form: a tiny letter, postcard, playful award, micro-story, fake museum label or another fitting format. In Auto, use available recent conversation output and optional type/theme feedback for variety; feedback history may be sparse or stale. Manual Mode uses only the current request/context.
- Use mostly text, sometimes a card-like presentation, and occasionally an actual generated image when available. Otherwise choose text silently.
- Full surprise content belongs only in the conversation. Never store it or generated images in this state file.

## State Contract and Migration

Interactive mutable fields are `enabled`, `start_week`, `schedule_seed`, `last_approved_auto_delivery`, `last_mode`, `last_type`, `recent_types` and `recent_themes`. Only authorized initial setup or explicit repair/upgrade may generate a seed. Pausing, resuming, feedback, repeated setup checks and scheduled runs preserve it. Preserve unrelated frontmatter and all personal feedback history; Surprise bookkeeping must not modify Daily Memory, Ledger, Gmail or Calendar.

During an explicitly authorized upgrade from v4 or older, preserve `enabled` and feedback history, remove `weekly_due_dates` and legacy `next_due`, `min_gap_days`, `max_gap_days`, set schema v5, and initialize one seed with a start week after the upgrade completes. Explain that the old calendar is replaced; do not silently migrate a live installation, recreate bulk dates or catch up missed deliveries. Public template fields remain null/empty.
