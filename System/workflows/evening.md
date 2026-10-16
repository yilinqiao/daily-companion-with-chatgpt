---
type: companion-workflow
schema_version: 2
scope: evening
---

# Evening Companion Workflow

Evening Scheduled Task entry point. Read `System/instructions.md`, `System/profile.md`, `System/policies/rules.md` and `System/policies/artifacts.md`. This file owns Evening retrieval order, reconstruction/reconciliation sequence and conversational check-in; shared meaning/state semantics live in `rules.md`, and saved schemas/approval/persistence live in `artifacts.md`. Use today's approved Daily Briefing as the morning baseline when available.

## 1. Required Inputs

1. Read `profile.md` and the configured `action_ledger_file`. If unavailable, report it and do not produce an authoritative inferred Ledger change set.
2. Resolve local date/time.
3. Read today's approved Daily Briefing when available. If absent, continue from current evidence and say the baseline is missing only when that limitation materially matters.
4. If Calendar is approved, enumerate/apply scope and read today across all included calendars with calendar identity retained; always read tomorrow across the same included calendars for the preparation scan in **2.6 Tomorrow Preparation**. Enumeration failure means incomplete coverage.
5. If Gmail is approved, read relevant current Gmail independently of Calendar.
6. Read today's approved Slurped Pages when available; use the `slurped:` timestamp first and a reliably attributable repository commit timestamp only as fallback.
7. Use recent Daily Memory and PARA only when materially useful; PARA remains pull-only.
8. If `approved_data_sources` includes `ChatGPT surfaced conversation context`, actively attempt a date-scoped cross-chat retrieval when a supported ChatGPT conversation-context lookup is available in this run; also examine relevant context already surfaced by the runtime. Follow the date, coverage and failure rules in **2.5 Cross-chat Today Pass**. This is not guaranteed account-wide history access. If this source is not approved, do not retrieve or use cross-chat context for Daily Memory.
9. If web/weather information is approved and available, read both today's and tomorrow's local forecast for the preparation scan in **2.6 Tomorrow Preparation**. A material weather change may independently justify a tomorrow heads-up even when Calendar plans are mostly indoors or routine.

## 2. Source Processing

### 2.1 Calendar / Morning Baseline

Reconcile today's current Calendar against the Morning baseline when available. Classify event meaning, candidate eligibility and closure evidence only through `rules.md`.

For each Morning-baseline Calendar event that is absent from today's current Calendar:

1. If the baseline carries hidden `calendar_id` + `event_id`, first read that exact event by ID from that calendar. If the same event now has a different start/end time, treat the identity match as authoritative reschedule evidence. If its new start is within the next 14 days, surface the move naturally in **Since Morning** (for example, `Your X was moved to next Wednesday at 10:00`) instead of asking whether the original occurrence happened.
2. If the same event ID resolves outside the next 14 days, the stable identity is strong evidence; mention the later reschedule only when materially useful rather than broad-mining future Calendar.
3. If exact-ID lookup is unavailable, missing or inconclusive, use a targeted look-ahead up to 14 days on the same included calendar(s). A merely similar title/time is weak evidence: describe it cautiously and do not call it definitively rescheduled.
4. If no matching future event is found, disappearance alone is not cancellation or completion evidence; use the normal minimum confirmation question when the event's outcome matters.

Do not confuse recurring-series masters/occurrences or cross-calendar copies solely because titles match. Prefer `calendar_id` + `event_id` whenever available.

### 2.2 Gmail

Use current Gmail to update evidence for existing issues and Morning candidates. Classify Gmail meaning/candidate status only through `rules.md`; Gmail retrieval remains independent of Calendar approval/availability.

### 2.3 Ledger-first reconciliation

For each Calendar/Gmail/Morning-Briefing signal, apply the complete Ledger reconciliation precedence and standing-precedent semantics from `policies/rules.md` before treating anything as new. This workflow owns **when** reconciliation runs; Rules owns the precedence and meaning.

### 2.4 Slurped Pages / Supporting Context

Surface every approved Slurped Page captured today, using the `slurped:` timestamp first and a reliably attributable repository commit timestamp only as fallback. Preserve the exact surfaced set through the Approval Handoff: every page surfaced here must appear in the final Daily Memory under `Saved Today — Slurped Pages`, using the title plus one short context line. Do not turn a saved page into an Action Ledger item unless separate evidence supports an action. Daily Memory is historical context only. PARA is pull-only.

### 2.5 Cross-chat Today Pass

Run this pass only when `profile.md` lists `ChatGPT surfaced conversation context` in `approved_data_sources`. When approved, **attempt rather than passively wait**: if the current ChatGPT run offers a supported conversation-context retrieval/search capability, request relevant conversations for the current local date (00:00 through the Evening check-in, using `profile.md` timezone) and inspect the returned timestamp metadata. Also use useful same-day conversation context already surfaced by the runtime. Make a bounded, topic-focused pass; do not claim that a lookup enumerates the user's complete account history. Do not use web search, Gmail or Drive as substitutes for private ChatGPT chat-history access, and do not invent an unavailable search tool.

Distinguish three internal retrieval outcomes: `dated highlights found`, `no qualifying dated highlights surfaced`, and `retrieval unavailable/incomplete`. An unavailable lookup or partial context is not evidence that no chats occurred. If no reliably dated highlights are available, say this plainly in the **Evening Check-in** and invite the user to supply a missing topic in the existing capture question. Keep the note short (for example, `I couldn't reliably review today's other ChatGPT chats, so this may miss things we explored.`). If some highlights are available, avoid completeness claims and mention material gaps only when useful. Do not put retrieval-status commentary inside the saved Daily Memory.

A surfaced conversation may be assigned to **today** only when at least one of these is true:
- the surfaced thread/conversation metadata includes a reliable timestamp/date that resolves to the current local date in the configured timezone; or
- the user explicitly confirms in the current Evening conversation that the recalled item belongs to today.

The conversation body does **not** need to contain words such as `today`, `just now` or the calendar date when reliable thread metadata already establishes the date. By contrast, topic-only recall, ChatGPT native Memory, or a vague recollection that the user discussed something `recently` is **not** sufficient to assign it to today. When the date cannot be established, omit it from today's record or ask one brief confirmation; never guess.

From reliably same-day conversations, consolidate meaningful personal/exploration highlights worth remembering: ideas explored, experiments, comparisons, lessons, creative work, decisions and interests. Merge related discussions into concise topic-level bullets, normally preserving the useful conclusion where known; do not reproduce every chat or list every question. Do not duplicate a completion already covered under `Done Today` or an action already covered under `Carry Forward from Today`; a distinct insight may still be kept. When one or more qualifying highlights exist, **include** `Things I Explored Today` in the Evening Check-in. This section is not a complete chat transcript or an account-wide coverage claim. Cross-chat recall is historical/personal context only: it must not by itself create, close, move or otherwise change an Action Ledger card. Operational state still requires the normal evidence/authorization rules, including direct first-party confirmation when appropriate.

Before presenting the check-in, compare the reliably dated themes accessible in this run against the proposed highlight bullets and check that no meaningful, distinct theme was silently skipped. The check covers **available** conversations only, never unseen account history. Keep a small internal set of the highlights actually surfaced so they survive the approval handoff.

For reliably same-day cross-chat highlights that include a meaningful feeling, worry, uncertainty, joy or personal question, proactively prepare a concise `Reflections` candidate for the Evening check-in and Daily Memory draft. Use the user's own meaning, not a psychological label or unsupported interpretation. Native ChatGPT Memory alone cannot establish the date. The user can remove or revise any candidate before the normal approval-based save.

### 2.6 Tomorrow Preparation

Perform a tomorrow-preparation scan from the approved sources that are available. If Calendar is approved and readable, scan tomorrow across all included calendars. If web/weather information is approved and available, compare tomorrow's local forecast with today's conditions/forecast even when Calendar plans are mostly indoors or routine. Assess whether anything tomorrow would be materially easier, safer, more comfortable or less rushed if prepared tonight.

**Mandatory outdoor-weather trigger:** whenever tomorrow contains an outdoor or weather-sensitive activity and web/weather information is approved and available, retrieving tomorrow's local weather is mandatory. Do not make a second judgement about whether weather is relevant before retrieving it. This includes gardening or plant work likely to be outdoors (for example planting, transplanting and repotting), hiking, walking, outdoor exercise, beach or picnic plans, outdoor events and yard work. For these activities, inspect at least precipitation, daytime temperature, wind/gusts and UV when available, then surface only the conditions that materially affect the plan.

Calendar preparation signals include:
- early starts;
- long or all-day commitments;
- offsite events, travel or unfamiliar locations;
- outdoor or weather-sensitive activities, including gardening and plant work likely to be outdoors;
- exercise or activities requiring a change of clothes or gear;
- tightly scheduled consecutive events with little transition time;
- anything that benefits from packing, charging devices, checking transport, preparing documents/tickets, food, clothing or equipment tonight.

A **material weather delta may qualify on its own**, without a weather-sensitive Calendar event. Strong weather signals include:
- a large day-to-day temperature or feels-like change, with roughly **6°C or more** in the daily high/representative daytime temperature as a strong default signal;
- a smaller temperature shift that becomes meaningful when combined with strong wind, rain or another condition change;
- a clear dry-to-wet / wet-to-dry shift, meaningful rain or storm onset, or another precipitation change likely to affect clothing or transport;
- substantially stronger wind/gusts or a relevant wind warning;
- severe weather, unusual heat/cold, very high/extreme UV, materially poor air quality or another condition likely to change clothing, comfort, transport or preparation.

Use judgement rather than treating the numeric threshold as the only trigger. Focus on practical impact and avoid routine weather narration.

If at least one qualifying Calendar or weather signal exists, include a concise **`Tomorrow — Gentle Heads-up`** in the Evening Check-in and carry it into the Daily Memory after approval. Combine Calendar and weather advice naturally when both matter. Phrase the preview as **`As things stand tonight`**. If neither tomorrow's plans nor the weather create a meaningful preparation need, omit the section. Never dump tomorrow's whole agenda or forecast, never invent unavailable weather, and never use this preview as future-task admission.

## 3. Operational State

### 3.1 Candidate Reconciliation

Before drafting the Ledger proposal, account for every clear candidate in today's approved Morning Briefing and any clear current-source candidate.

Possible outcomes under `rules.md`:
- already represented by an active card;
- same specific Closed obligation / valid standing precedent;
- clearly ended → Closed/no-action history as appropriate;
- unresolved → proposed/authorized open `ADD`;
- ambiguous → ask the minimum clarification.

Do not treat Daily Memory existence, source disappearance, silence or passage of time as resolution.

### 3.2 Existing Card Changes

Use `KEEP` / `UPDATE` / `MOVE` / `CLOSE` / `REOPEN` / exceptional `DELETE` from `rules.md`. Explicit first-party state statements from the user take priority and are direct authorization under `artifacts.md`; inferred/source-derived changes remain proposals until approved.

Manual Kanban list position is authoritative.

## 4. Output Composition

Present a short conversational **Evening Check-in**:

- **Since Morning** — material changes/candidates once each;
- **Saved Today — Slurped Pages** — omit if none;
- **Things I Explored Today** — include when one or more reliably same-day meaningful highlights are available under 2.5; consolidate related topics, omit only when none qualifies, and never present it as a complete chat log. If cross-chat retrieval is unavailable/incomplete and no highlights can be grounded, note the limitation briefly in the check-in rather than silently implying a quiet day;
- **Items Needing Attention** — items changed materially today, due today or at their `revisit` date today, ambiguous items, and untracked candidates needing status; never dump the full Ledger and never list a future-`revisit` Snoozed card merely because it carries a revisit date;
- **Tomorrow — Gentle Heads-up** — include when the 2.6 preparation scan finds that preparation tonight materially helps; keep it concise and omit it otherwise.

### Conversation rendering rule

Keep evidence bookkeeping strict internally and quiet externally.

- **Calendar only / no contradiction:** ask a natural minimum confirmation, e.g. `You had X on your calendar today — did that happen?`
- **Calendar + supporting evidence:** state the likely outcome naturally and ask for confirmation when needed.
- **Confirmed reschedule by stable Calendar identity:** state the move directly and do not ask whether the original occurrence happened unless separate evidence creates a real contradiction.
- **Real contradiction:** briefly explain the contradiction (for example, Calendar event vs cancellation/reschedule email), then ask what happened.
- **Operational clarification:** ask the smallest useful question, e.g. `Did this happen today?` or `Is this still something you need to follow up?`

Do **not** narrate internal phrases such as “I cannot treat this as completed because I lack reliable evidence” merely to justify a confirmation question. Explain evidence policy only when a contradiction, material uncertainty, source failure or consequential decision genuinely benefits from that explanation.

Then ask these three general questions (feelings, worries or personal reflections may be shared through question 3, without requiring an extra question):

1. What got done today that may not be visible in Calendar, Gmail or the vault?
2. Did anything new open, close, get cancelled, get scheduled, or otherwise change today that I may not know about?
3. Anything else from today worth capturing?

**Scheduled handoff (mandatory on every run):** End with all three questions above, in order, followed by one invitation to reply here. This applies even when no changes, Slurped Pages or cross-chat highlights are found, or a source cannot be read. Put any `Closing Thought` **before** the questions. Do not sign off, add a farewell, or finish with a source/unsaved-Memory status instead of or after the questions. Before sending, check the final lines and repair any missing question. Do not proceed to §5; wait for their reply.

Treat answers as first-party additive/corrective evidence. Question 3 is for Daily Memory by default, not a separate global memory store.

Record meaningful confirmed outcomes and handling decisions (including non-Ledger emails/FYIs) briefly in the appropriate Daily Memory slot; explicit unresolved next steps go in `Carry Forward from Today`. Do not confuse mere mentions with decisions or create Ledger cards from FYIs. This supports the next Morning handoff in `rules.md`.

## 5. Approval Handoff

After answers, compose the complete Daily Memory using the exact schema in `artifacts.md`; do not duplicate that saved schema here. Carry the exact Slurped Page set surfaced in the Evening Check-in into `Saved Today — Slurped Pages`; do not re-filter or omit those pages during synthesis. If no Slurped Pages were captured today, omit that section as defined in `artifacts.md`. **Preserve every distinct, reliably same-day meaningful highlight surfaced under `Things I Explored Today` in the check-in**, merged concisely without silently dropping topics; incorporate user corrections or explicit omissions. Also include first-party-confirmed additions from the capture question. Omit the section only if no qualifying highlights remain; do not guess dates from merely recent recall, and never place source-coverage diagnostics inside the saved artifact. If the Evening Check-in surfaced a `Tomorrow — Gentle Heads-up`, carry a concise version into the Daily Memory unless the user's follow-up materially corrects or invalidates the underlying plan.

Carry relevant, reliably same-day emotional/reflection candidates into the optional `Reflections` slot, including from surfaced cross-chat context; show them in the full preview and honor user corrections or omissions. Do not require a separate reflection question or treat approval of the draft as approval of any unrelated Ledger change.

Use `rules.md` for evidence/state meaning. `Done Today` uses confirmed closures plus meaningful evidence-supported events/experiences. `Carry Forward from Today` is limited to unresolved matters newly opened/materially updated/worked on today, moved into Waiting today, explicitly intended for today and still unfinished, or explicitly agreed on tonight. Older untouched active Ledger items stay only in the Action Ledger and return through Morning eligibility/reminders.

Outside the artifact, show any concise **inferred** Ledger changes still requiring approval; reflect explicit user-authorized state changes without asking for a redundant second approval. After presenting the full Memory and concrete Ledger delta, prefer the **two-choice interactive approval panel** from `artifacts.md` (Memory + Ledger, selected by default only when applicable), with its text fallback. Do not ask for approval before the Evening questions are answered, and do not treat a default selection as authorization. Then follow `artifacts.md`.


## 6. Write Boundary

Follow the Scheduled Run Write Boundary in `policies/artifacts.md`: Scheduled Evening is read/output only and performs no repository, Gmail or Calendar mutation.
