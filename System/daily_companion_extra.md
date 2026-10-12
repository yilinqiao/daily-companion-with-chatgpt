---
type: companion-surprise-engine
schema_version: 6
enabled: true
scheduled_writes_authorized: false
next_due_date: null
delivery_status: idle
delivery_due_date: null
delivery_claimed_at: null
last_attempt_date: null
last_approved_auto_delivery: null
last_mode: null
last_type: null
recent_types: []
recent_themes: []
---

# Companion Surprise Engine

This file owns Surprise rules and state. Keep its body intact on state writes. Auto has one narrowly authorized scheduled write exception: it may update only its own scheduling/delivery fields in this file in the configured **private** repository. Morning/Evening remain read-and-output only. Extra must never write profile, Daily, Ledger, other notes, Gmail or Calendar.

## Cadence and Date Selection

- Setup chooses one arbitrary local date in the complete Monday–Sunday calendar week immediately after setup finishes, storing it as next_due_date. Use the timezone in the configured profile. Save one date, never a future calendar, seed or hash. No Python, SHA-256, hashing service or executable script is required.
- Choose freely from those seven dates, without a fixed weekday or predictable rotation. Consecutive weeks may pick the same weekday. This is a conversational random choice, not a claim of cryptographic randomness or a mathematically uniform distribution. Check the ISO YYYY-MM-DD date exists and lies in the intended week; ordinary calendar reasoning is sufficient.
- Each daily check compares today's local date with the saved date. Earlier means silence. Equal or later means one eligible delivery, including one late delivery after missed checks. Never replay a backlog of missed weeks.
- Before the final response, choose one date in the calendar week immediately after the **local delivery-attempt week**, and replace the saved date under the completion protocol. A late Monday delivery schedules the following week, not another delivery in the same week. Weekly cadence is a plan, not a guarantee of execution or notification receipt.
- Auto continues without weekly approve. Setup/task activation explicitly authorizes only the narrow state writes below. Only explicit pause/stop/disable turns Auto off; Manual remains available while paused.
- Keep planned dates/bookkeeping out of normal user-facing output. Dates/timestamps are private operational state, never public-template data. Do not store surprise content or generated images here.

## Valid State

- Private initialized state has schema v6, booleans enabled and scheduled_writes_authorized, a valid non-null next_due_date and delivery_status of idle or claimed. The consent flag starts false and becomes true only through explicit interactive authorization of Extra's narrow scheduled writes; never infer it from enabled or connector access.
- idle: delivery_due_date and delivery_claimed_at are null. last_attempt_date is null before the first committed delivery attempt, otherwise the valid local ISO date of that attempt, not proof of rendered/received output. The next date is later than that committed delivery attempt and in a later Monday–Sunday week.
- claimed: delivery_due_date equals the unchanged next_due_date; delivery_claimed_at is a valid timezone-aware ISO timestamp. A claim reserves an attempt; it is **not proof of delivery**. Never clear/expire it automatically. It blocks later scheduled attempts until the owning run completes or an authorized interactive recovery occurs.
- Null date, unsupported schema, legacy cadence fields, inconsistent claim or invalid attempt-date relation stops Auto silently. Never initialize/migrate/repair state in a scheduled run; explain repair in an interactive check. Public dates/history remain null, status idle.

## Auto Mode

Run only through one daily Daily Companion Extra task. A file read does not prove scheduled write access. Use supported authorized connector operations and respect platform blocks.

1. Fresh-read this engine, the configured profile, System/instructions.md and applicable shared policies from the exact repository/path (map System to the configured system_folder). Follow the user's language/style and approved-source boundaries. Require completed setup, approved GitHub access and verified private repository identity/visibility. Never write to yilinqiao/daily-companion-with-chatgpt or substitute another repository. If disabled, scheduled_writes_authorized is not true, before the date or already claimed, stop silently. Validate state and resolve the current local date.
2. Prepare one surprise privately under Creation Rules; do not expose it yet. Immediately before claiming, fresh-read profile/engine, revalidate enabled/setup/date/state and scheduled-write consent, and use the current file SHA (or expected branch head for an atomic ref update). Preserve the body, feedback and unrelated fields. If still due and idle, change only delivery_status to claimed, delivery_due_date to the current next_due_date, and delivery_claimed_at to the current local ISO timestamp.
3. Commit that single-file claim and read back. Only a run with a confirmed successful conditional write and matching read-back owns it. A competing run, stale-SHA conflict, ambiguous timeout or prepared/unreferenced tree is not a confirmed claim. Stop without rendering on uncertainty/error; never assume ownership because another run wrote identical values. Report actual saved/pending state when readable. Never bypass a safety block or blindly retry a write.
4. Immediately before completion, fresh-read engine/profile. Require the owned claim still matches, setup complete, Auto enabled and scheduled_writes_authorized true. If paused, changed or unavailable, stop without output, leaving the claim for interactive review. Resolve the local date again and choose one next_due_date in the calendar week after this attempt week. Commit only next_due_date to that chosen date, last_attempt_date to today's local date, delivery_status to idle, delivery_due_date to null and delivery_claimed_at to null. Preserve any concurrent feedback/customizations, enabled, consent and full body; use the fresh SHA and a conditional single-file write. Never grant permission or resume Auto during completion.
5. Confirm the completion write succeeded and read back the exact planned fields. If the Sunday–Monday boundary changed during this handoff, verify the selected date remains in the following complete week; if it does not, stop before output and report the actual saved state for review. Do not claim exact atomic timing across GitHub/chat. Immediately before the final response, recheck setup/enabled/consent and the verified attempted-date/next-date fields; a changed or unreadable result stops without surprise output and is reported as pending/uncertain. Then render the prepared surprise exactly once in the final response. No approve question; optionally say **Say “pause surprises” any time to pause.** Do not require tools to run after a final response.
6. A claim/completion error or ambiguous response stops without surprise output. Inspect actual state when readable and report a brief actionable failure, distinguishing a pending claim from a schedule already advanced or an unknown result. Never blindly retry, repeat content, manufacture success or assume an error means nothing committed. A pending claim blocks later runs until interactive recovery. If the schedule already advanced, preserve it and inspect the recorded attempt interactively.

GitHub and a chat response do not share an atomic transaction. This protocol reserves an attempt and verifies the next schedule **before** the final reply, so final-response-only scheduled environments can follow it. last_attempt_date is bookkeeping, **not a delivery receipt**. A crash after claiming leaves a pending claim; a crash after advancing but before output may miss that week's surprise while retaining next week's plan. Neither is automatically retried. Do not advertise exactly-once delivery or notification receipt. Keep one task without overlapping retries; conditional writes remain necessary. The attempt week is resolved at the final write; a boundary between that write and response can still affect observed output time.

## Manual Mode

Only an explicit request such as surprise me triggers Manual; low mood alone is not a request. Fresh-read the engine and compose/render now, including while paused, using current request/context for variety. Do not claim, consume, move, repair or change Auto dates/state. No approval question. Mood is a tone signal, not a request for therapy/coaching/advice.

## Interactive Controls and Recovery

- **pause**, **pause surprises**, **stop surprise**, or a clear equivalent: set only enabled false with a fresh SHA, preserving dates, claim and history; verify and confirm. A bare pause in a Surprise conversation counts; clarify an unrelated conversation's ambiguous target. A pending claim remains pending. Manual stays available.
- **resume surprises**: set only enabled true, preserve valid date/claim/history and verify. A pending claim still needs recovery; do not clear it on resume. An idle overdue date is eligible at the next daily check. Invalid state needs a specific repair.
- Explicitly grant/revoke Extra scheduled state writes: set only scheduled_writes_authorized after explaining the exact five scheduled fields and verifying the write. Revocation blocks completion writes too and leaves any claim for interactive recovery. Pause/resume never silently grants this permission; if absent, explain Auto cannot proceed until the user explicitly grants it.
- **recover/repair Surprise**: read state and the relevant task run/output evidence, including whether the next date already advanced. A pending claim is not proof of output. If a claim is pending and output is absent, propose rearming the same overdue date or skipping/rescheduling into the week after recovery, with the loss/duplicate tradeoff stated if output is unknown. If output is reliably present, propose clearing the claim and scheduling after recovery; only reliably evidenced prior attempts may inform last_attempt_date. If state already advanced but output was lost, preserve the next date and report the missed attempt; an explicit manual surprise request can render content without modifying Auto. Never guess, auto-replay or expire a claim. Obtain approval of a concrete state repair, preserve pause/consent/history/body, use a fresh SHA and verify. A skip never invents a delivery receipt; unknown history retains the prior last_attempt_date. Recovery does not silently render another surprise.
- Explicit style-feedback requests may interactively update last_approved_auto_delivery, last_mode, last_type, recent_types and recent_themes (maximum five entries each). Preserve schedule/claim/body. Legacy feedback neither controls cadence nor proves every delivery. Never solicit approve to continue Auto.
- On a blocked/unverified write, explain the actual result. Never create duplicate tasks or enable paused tasks to force progress.

## Creation Rules

- Personal without becoming a recap: prefer specific ordinary details from roughly the last 7–14 days of already available context.
- If needed, narrowly read up to 3 recent Daily Memories and at most 1 relevant PARA file. Do not broaden Gmail/Calendar retrieval merely to manufacture emotional content.
- No Ledger items, reminders, follow-ups, productivity coaching or disguised advice unless explicitly requested instead of a surprise.
- Avoid generic praise, motivational cliches, forced sentiment and repetition. Warm, funny, tender, whimsical, curious or lightly absurd are valid.
- Vary forms: tiny letter, postcard, playful award, micro-story, fake museum label or another fitting format. Optional feedback may be sparse/stale; never infer delivery history from it.
- Mostly text, sometimes a card-like presentation, occasionally a generated image when available; otherwise text silently. Full content belongs only in the conversation.

## State Ownership and Migration

Scheduled mutable fields are only next_due_date, delivery_status, delivery_due_date, delivery_claimed_at and last_attempt_date. Setup, authorized upgrade/repair and the owning run's completion may select dates. Interactive controls also own enabled, scheduled_writes_authorized and feedback. Preserve unrelated frontmatter and the whole engine body; never write Daily, Ledger, profile, other notes, Gmail or Calendar.

An approved v5 upgrade replaces the hash calculator with v6: preserve enabled, feedback and unrelated state; remove schedule_seed, start_week and older cadence fields; initialize one date in the week after migration completes, idle claim fields, last_attempt_date null and scheduled_writes_authorized true only if explicitly granted (otherwise false) (feedback is not verified delivery history). Explain scheduled write permission and late delivery. Migrate only after approval of this concrete change and removal of the old read-only task-prompt restriction. Suspend a previously enabled Extra for migration, preserve already paused/never-activated status, and do not rerun onboarding or recreate Morning/Evening. Apply the same explicit conservative migration to older formats while preserving user data. No future list, scheduled auto-migration, invented prior attempt history or new calculation test. Public state stays uninitialized.
