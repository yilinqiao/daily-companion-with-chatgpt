---
type: companion-workflow
schema_version: 2
scope: evening
---

# Evening Companion Workflow

Evening Scheduled Task entry point. Read `System/instructions.md`, `System/profile.md`, `System/policies/rules.md` and `System/policies/artifacts.md`, plus the selected storage adapter. This file owns Evening retrieval order, reconstruction/reconciliation sequence and conversational check-in; shared meaning/state semantics live in `rules.md`, and saved schemas/approval/persistence live in `artifacts.md`. Use today's saved Daily Briefing as the morning baseline when available.

## 1. Required Inputs

1. Read `profile.md` and the configured Ledger via selected storage adapter. If unavailable, report it and do not produce an authoritative inferred Ledger change set.
2. Resolve actual scheduled occurrence local date/time; stop without writes if uncertain.
3. Read today's saved Daily Briefing when available. If absent, continue from current evidence and say the baseline is missing only when that limitation materially matters.
4. If Calendar is approved, apply account/calendar scope per `rules.md` and read today across all included calendars with calendar identity retained; always read tomorrow across the same included calendars for the preparation scan in **2.6 Tomorrow Preparation**. Enumeration failure means incomplete coverage.
5. If Gmail is approved, apply account scope per `rules.md` and read relevant current Gmail independently of Calendar.
6. Read today's approved capture source, if configured; use the selected adapter's reliable capture-time rules.
7. Use recent Daily Memory and PARA only when materially useful; PARA remains pull-only.
8. If `approved_data_sources` includes `ChatGPT surfaced conversation context`, actively attempt a date-scoped cross-chat retrieval when a supported ChatGPT conversation-context lookup is available in this run; also examine relevant context already surfaced by the runtime. Follow the date, coverage and failure rules in **2.5 Cross-chat Today Pass**. This is not guaranteed account-wide history access. If this source is not approved, do not retrieve or use cross-chat context for Daily Memory.
9. If web/weather information is approved and available, read both today's and tomorrow's local forecast for the preparation scan in **2.6 Tomorrow Preparation**. A material weather change may independently justify a tomorrow heads-up even when Calendar plans are mostly indoors or routine.

## 2. Source Processing

### 2.1 Calendar / Morning Baseline

Reconcile today's current Calendar against the Morning baseline when available. Classify event meaning, candidate eligibility and closure evidence only through `rules.md`.

For each Morning-baseline Calendar event that is absent from today's current Calendar:

1. If the baseline carries Notion-only Calendar ID section or GitHub hidden `calendar_id` + `event_id`, first read that exact event by ID from that calendar. If the same event now has a different start/end time, treat the identity match as authoritative reschedule evidence. If its new start is within the next 14 days, surface the move naturally in **Since Morning** (for example, `Your X was moved to next Wednesday at 10:00`) instead of asking whether the original occurrence happened.
2. If the same event ID resolves outside the next 14 days, the stable identity is strong evidence; mention the later reschedule only when materially useful rather than broad-mining future Calendar.
3. If exact-ID lookup is unavailable, missing or inconclusive, use a targeted look-ahead up to 14 days on the same included calendar(s). A merely similar title/time is weak evidence: describe it cautiously and do not call it definitively rescheduled.
4. If no matching future event is found, disappearance alone is not cancellation or completion evidence; use the normal minimum confirmation question when the event's outcome matters.

Do not confuse recurring-series masters/occurrences or cross-calendar copies solely because titles match. Prefer `calendar_id` + `event_id` whenever available.

### 2.2 Gmail

Use current Gmail to update evidence for existing issues and Morning candidates. Classify Gmail meaning/candidate status only through `rules.md`; Gmail retrieval remains independent of Calendar approval/availability.

### 2.3 Ledger-first reconciliation

For each Calendar/Gmail/Morning-Briefing signal, apply the complete Ledger reconciliation precedence and standing-precedent semantics from `policies/rules.md` before treating anything as new. This workflow owns **when** reconciliation runs; Rules owns the precedence and meaning.

### 2.4 Slurped Pages / Supporting Context

Surface every approved Slurped Page captured today, using the selected adapter's capture-time rules. Preserve the exact surfaced set through the Approval Handoff: every page surfaced here must appear in the final Daily Memory under `Saved Today — Slurped Pages`, using the title, original link and one short context line. Do not turn a saved page into an Action Ledger item unless separate evidence supports an action. Daily Memory is historical context only. PARA is pull-only.

### 2.5 Cross-chat Today Pass

Only if `ChatGPT surfaced conversation context` is approved: actively attempt a bounded topic-focused conversation lookup for today's local date (midnight through check-in), when supported, and inspect already surfaced context. Do not substitute other connectors or claim complete account history. Reliable local-date thread metadata OR explicit user confirmation is required; topic-only recall/native Memory is insufficient. No guessing. Distinguish dated highlights, no qualifying highlights and unavailable/incomplete retrieval. Mention material gaps briefly in check-in, not saved Memory; invite missing topics via the existing questions.

Include meaningful distinct same-day cross-chat ideas, conclusions, experiments, decisions and personal highlights in Other Updates & Explorations if any; consolidate by topic and check no available distinct theme was silently lost. Preserve reliably dated feelings, worries, joys or questions as optional Reflections candidates subject to normal approval-based save. Cross-chat context alone never authorizes Ledger state changes.

### 2.6 Tomorrow Preparation

Scan tomorrow's included Calendar and compare today's and tomorrow's approved/available local forecast. For outdoor or weather-sensitive plans (gardening, plant work, hiking, exercise, outdoor events), retrieving tomorrow's weather is mandatory when approved/available; check rain, temperature, wind/gusts and UV. Surface only material impacts.

Preparation signals: early starts, long/offsite events, travel, unfamiliar locations, gear/clothing changes, tight transitions or packing/charging/documents/food. A weather delta alone can qualify: roughly 6°C daytime change, smaller shift with rain/wind, dry/wet transition, storm, warnings, severe temperatures, high/extreme UV or poor air quality. Use practical judgement rather than a rigid threshold.

If preparation tonight helps, include `Tomorrow — Gentle Heads-up` (As things stand tonight) and carry into Memory unless corrected. Otherwise omit. No agenda/forecast dump, invented weather or future-task admission.

## 3. Operational State

### 3.1 Candidate Reconciliation

Before drafting the Ledger proposal, account for every clear candidate in today's saved Morning Briefing and any clear current-source candidate.

Possible outcomes under `rules.md`:
- already represented by an active card;
- same specific Closed obligation / valid standing precedent;
- clearly ended → Closed/no-action history as appropriate;
- unresolved → proposed/authorized open `ADD`;
- ambiguous → ask the minimum clarification.

Do not treat Daily Memory existence, source disappearance, silence or passage of time as resolution.

### 3.2 Existing Card Changes

Use `KEEP` / `UPDATE` / `MOVE` / `CLOSE` / `REOPEN` / exceptional `DELETE` from `rules.md`. Explicit first-party state statements from the user take priority and are direct authorization under `artifacts.md`; inferred/source-derived changes remain proposals until approved.

Manual status/property or Kanban list position is authoritative.

## 4. Output Composition

Use these inputs to compose the provisional Diary-first Memory for Notion, or a short conversational **Evening Check-in** for GitHub:

- **Since Morning** — material changes/candidates once each;
- **Saved Today — Slurped Pages** — omit if none;
- **Other Updates & Explorations** — include when one or more reliably same-day meaningful highlights are available under 2.5; consolidate related topics, omit only when none qualifies, and never present it as a complete chat log. If cross-chat retrieval is unavailable/incomplete and no highlights can be grounded, note the limitation briefly in the check-in rather than silently implying a quiet day;
- **Items Needing Attention** — items changed materially today, due today or at their `revisit` date today, ambiguous items, and untracked candidates needing status; never dump the full Ledger and never list a future-`revisit` Snoozed card merely because it carries a revisit date;
- **Tomorrow — Gentle Heads-up** — include when the 2.6 preparation scan finds that preparation tonight materially helps; keep it concise and omit it otherwise.

### Conversation rendering rule

Keep evidence bookkeeping internal. Calendar alone: ask if it happened when material; supporting evidence: state likely outcome and confirm if needed; exact-ID reschedule: state the move; contradiction: briefly explain and ask. Ask the smallest useful clarification. Do not narrate internal evidence thresholds.

For Notion, prepare one complete provisional Diary-first Memory using only supported evidence and the artifact schema. With verified autosave consent, auto-save and verify it under storage/notion.md. Display the same complete user-visible body in ordinary chat, in the same order, without omissions or regeneration; no separate summary or editable approval preview. Put verified URL/status outside the body. If auto-save fails or is unauthorized, show the full safe draft with an honest unsaved notice outside the body. Defer the editable approval preview until after answers. GitHub is read-only and retains its conversational check-in and interactive save after answers.

Then ask these three general questions:

Feelings, worries or personal reflections may be shared through question 3; do not add a required fourth question.

1. What got done today that may not be visible in Calendar, Gmail or your saved notes?
2. Did anything new open, close, get cancelled, get scheduled, or otherwise change today that I may not know about?
3. Anything else from today worth capturing?

**Scheduled handoff (mandatory on every run):** End with all three questions above, in order, followed by one invitation to reply here. This applies after successful verified full Notion Auto-Saved Memory display and after a failed/unauthorized save, during a GitHub read-only check-in, and even when no changes, Slurped Pages or cross-chat highlights are found, or a source cannot be read. Put any `Closing Thought` **before** the questions. Do not sign off, add a farewell, or finish with a source/unsaved-Memory status instead of or after the questions. Before sending, check the final lines and repair any missing question. Do not proceed to §5; wait for their reply.

Treat answers as first-party additive/corrective evidence. Question 3 is for Daily Memory by default, not a separate global memory store.

Record meaningful confirmed outcomes and handling decisions (including non-Ledger emails/FYIs) briefly in the appropriate Daily Memory slot; explicit unresolved next steps go in `Carry Forward from Today`. Do not confuse mere mentions with decisions or create Ledger cards from FYIs. This supports the next Morning handoff in `rules.md`.

## 5. Approval Handoff

After answers, compose the complete Daily Memory using the six Diary-first sections in `artifacts.md`. Preserve all distinct surfaced capture links, meaningful reliably same-day highlights, reflections and corrected tomorrow preparation once, incorporating user corrections. Keep coverage diagnostics out of saved Memory. Carry forward only unresolved matters newly opened/updated/worked on today, moved into Waiting today, intended for today but unfinished, or agreed tonight; older untouched cards stay in Ledger.

Preserve the user's own wording and meaning in Journal; lightly organize without replacing their voice. Before proposing a delta, fresh-read the Ledger after answers; if unavailable, continue Memory with no authoritative inferred Ledger delta. Present the full revised Markdown, independent concrete inferred Ledger delta when available, and approval panel/text fallback under artifacts.md. Direct first-party card instructions retain their scoped authority. Do not ask for approval before answers; do not save a revision until submitted approval. For Notion edit the same initial page, or use the adapter's approved creation fallback if no page exists; verify before marking Edited.

## 6. Write Boundary

Follow the Scheduled Run Write Boundary in `policies/artifacts.md`: Notion auto-saves only its initial provisional Daily page; GitHub is read/output only. Neither mutates Ledger, Gmail or Calendar.
