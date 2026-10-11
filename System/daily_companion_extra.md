---
type: companion-surprise-engine
schema_version: 4
enabled: true
weekly_due_dates: []
last_approved_auto_delivery: null
last_mode: null
last_type: null
recent_types: []
recent_themes: []
---

# Companion Surprise Engine

This file is the canonical owner of Companion Surprise behaviour and its lightweight delivery state. The frontmatter is mutable state; the body is the stable engine contract. Any state write must preserve this body exactly and modify only the defined frontmatter state fields, and it may only happen in an interactive turn: scheduled runs are read-only on this platform.

## Cadence Contract

- One automatic surprise is planned for **one randomly chosen local date in each complete Monday–Sunday calendar week**. Dates use the timezone in `System/profile.md`. The `weekly_due_dates` frontmatter list contains exactly one ISO `YYYY-MM-DD` date for each consecutive scheduled week, in ascending order. This is a pre-generated genuinely randomized schedule, not a fixed weekday or a 7–14 day interval.
- During setup, initialization or explicit interactive repair, create a schedule for the **next 104 complete Monday–Sunday weeks**, starting on the Monday after the current local week; sample one weekday independently and randomly for each week. A one-off catch-up for the current partial week is not required. Do not expose chosen dates in the normal user-facing conversation.
- The dedicated daily scheduled check is read-only: it compares today's local date against `weekly_due_dates`. It never needs to advance state to reach next week's entry. If one due-day run fails or is missed, do not send an unsolicited late duplicate; next week's independently planned day remains valid. Delivery does not depend on the user replying `approve`.
- A scheduled check cannot prove a push notification was received. If user notifications are disabled or the task fails, report limitations truthfully when asked. A weekly planned date is **not** a guarantee of delivery.
- If the list is missing, malformed, non-consecutive, expired or contains duplicate weeks, Auto stops silently and waits for an interactive repair. On any interactive approval, resume or maintenance request with fewer than 8 planned future weeks, append independently randomized dates until there are at least 104 future complete weeks, preserving all existing future dates. Never silently rewrite past delivery history.
- `enabled` controls automatic delivery only. Manual Mode stays available when Auto is disabled. Manual delivery does not consume or reschedule the weekly calendar.
- ChatGPT native Memory may inspire tone or ordinary details, but is never a cadence/state input or reliable evidence of actual delivery.

## Auto Mode

Auto Mode is invoked only by the existing **daily** `Daily Companion Extra` check. It is strictly read-only.

1. Resolve today's local date using `System/profile.md` timezone; fresh-read this file from the configured canonical System folder.
2. If `enabled: false`, stop silently.
3. Validate `weekly_due_dates`: ISO dates, ascending, at most one date per calendar week, and consecutive covered weeks from its first to last entry. If invalid or empty, stop silently; never generate dates from the scheduled run.
4. If today's local date is not one of the planned dates, stop silently. Never use an older date as a catch-up trigger.
5. On a match, compose exactly one surprise under Creation Rules and render it. End with the optional feedback/pause prompt below. Do not reveal future planned dates.
6. Write nothing. No Drive/GitHub file update, Daily artifact, Action Ledger, Gmail or Calendar mutation. No state advancement is required for next week's delivery.

A second execution on the same due date could duplicate output because scheduled checks cannot persist a delivery marker; keep the task at one daily run rather than adding overlapping scheduled checks.

## Manual Mode

Manual Mode is invoked when the user explicitly asks for a Companion Surprise, for example `surprise me`, `give me a little surprise`, or an equivalent direct request in the user's own language. A statement of low mood by itself is not enough; the user must actually ask for the surprise.

1. Fresh-read this exact file and execute immediately. Manual Mode is a one-off explicit request and is allowed even when automatic delivery is disabled.
2. Manual Mode never reads, writes or depends on the weekly dates, last approval or other Auto frontmatter, and never changes them.
3. Compose exactly one surprise under the Creation Rules below. If the user's request includes mood/context, use it only as a tone signal; do not automatically turn the surprise into therapy, advice, coaching or reassurance.
4. Render the surprise immediately. Do not append the Approval Handoff prompt; that prompt belongs only to an automatic delivery.

## Approval Handoff

An automatic delivery may end with this optional feedback line, adapted to the user's language:

> Enjoyed that? Say **approve** if you'd like me to remember the style for variety. Say **stop surprise** any time to pause future surprises.

- **approve** after a clearly visible automatic delivery: fresh-read the file; optionally record feedback by updating `last_approved_auto_delivery`, `last_mode: auto`, `last_type`, `recent_types`, and `recent_themes` (at most five entries each). This is for variety **only**, not permission for next week's surprise. Preserve the existing weekly schedule and all engine-body text.
- **stop surprise**: in an interactive turn set `enabled: false`, preserve the schedule/history, verify the write and confirm the pause. Manual Mode remains available.
- **resume surprises**: in an interactive turn set `enabled: true`, and if the schedule has expired or fewer than eight future weeks remain, refresh it as defined above. Preserve upcoming scheduled dates wherever possible; verify the write.
- **Unrelated replies or silence** do not affect the schedule. Next week's surprise remains planned.
- If a requested state write is blocked or cannot be verified, explain that fact without pretending the setting/history changed. Auto never attempts to bypass platform safety checks.

## Creation Rules

- Make the result feel personal without becoming a recap. Prefer specific, ordinary details from roughly the last 7-14 days of already available context.
- If more context is needed, use a narrow read of up to 3 recent Daily Memories and at most 1 relevant PARA file. Do not broaden Gmail or Calendar retrieval merely to manufacture emotional content.
- Never include Action Ledger items, reminders, follow-ups, productivity coaching or disguised advice unless the user explicitly asks for that instead of a surprise.
- Avoid generic praise, motivational cliches, forced sentiment and repetitive summaries. Warm, funny, tender, whimsical, curious or lightly absurd are all valid.
- Vary the form. Examples include a tiny letter, postcard, one-line observation, playful award, micro-story, future note, fake museum label, miniature scene or another invented format that fits recent life.
- In Auto Mode, use `last_type`, `recent_types` and `recent_themes` to avoid obvious repetition; do not repeat the same type on consecutive deliveries unless there is a strong creative reason. Manual Mode does not read or update these fields and relies on the current request and context for variety.
- Use mostly text, sometimes a more visual/card-like presentation, and only occasionally an actual generated image when image generation is available. If image generation is unavailable, silently choose a non-image form.
- Full surprise content belongs only in the conversation. Never store full surprise text or generated images in this state file.

## State Contract

Mutable frontmatter fields are limited to: `enabled`, `weekly_due_dates`, `last_approved_auto_delivery`, `last_mode`, `last_type`, `recent_types` and `recent_themes`. A weekly schedule is initially generated during interactive setup and may only be refreshed or repaired in an authorized interactive turn; automatic checks never write or advance it. Preserve unrelated frontmatter fields if present and do not modify Daily Memory, Action Ledger, Gmail or Calendar as part of Surprise bookkeeping. Legacy `next_due`, `min_gap_days` and `max_gap_days` should be migrated once during an authorized upgrade, preserving historical type/theme/approval fields; a past legacy due date must never cause a catch-up delivery.