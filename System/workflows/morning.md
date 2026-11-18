---
type: companion-workflow
schema_version: 2
scope: morning
---

# Morning Companion Workflow

Morning Scheduled Task entry point. Read `System/instructions.md`, `System/profile.md`, `System/policies/rules.md` and `System/policies/artifacts.md`, plus the selected storage adapter. This file owns Morning retrieval order, reconciliation sequence, eligibility filtering and surfacing actions; shared meaning/state semantics live in `rules.md`, and saved schemas/approval/persistence live in `artifacts.md`.

## 1. Required Inputs

1. Read `profile.md` and the configured Ledger via the selected storage adapter. If the Ledger is unavailable, report it and never reconstruct operational state from Daily Memory.
2. Resolve the actual scheduled occurrence local date/time in the configured timezone; stop without writes when uncertain.
3. Attempt each of the previous 7 local Daily Memory dates for context/history. Evaluate **standard Calendar recovery dates** independently, from yesterday backward, cap at 7. Skip Calendar re-reading a date only when a saved Daily Memory with positive evidence of complete Calendar coverage for the approved scope and candidate reconciliation for that date exists (use saved Briefing and current Ledger as evidence). A saved page or Auto-Saved status alone is not evidence of confirmation or closure. A newer complete date cannot hide an older gap. Read saved Briefings for each examined date when available; recover only unresolved-capable signals on uncertain dates.
4. If Calendar is approved, apply account/calendar scope per `rules.md` and read today's full local day across every included calendar with calendar identity retained. Read standard recovery dates for unresolved-capable signals. Independently perform the narrow 7-day financial safety look-back for the financial-action class in `rules.md`, regardless of Daily Memory checkpoints. Reuse retrieved dates and dedupe recovery paths.
5. If Gmail is approved, apply account scope per `rules.md` and review relevant mail from the previous 7 days, excluding Spam/Trash; prefer targeted reads.
6. Use PARA only when live context materially needs background. Normally retrieve at most 3 long-term vault files.
7. Use weather when useful and tied to actual plans.

Use only approved sources.

## 2. Source Processing

### 2.1 Calendar

Classify Calendar meaning, action eligibility and evidence only through `policies/rules.md`.

- Fixed work hours remain occupied unless supported evidence overrides them; do not infer free time from Calendar gaps for variable/none/unknown schedules.
- Reason about personal availability only inside the configured planning window. Show actual calendar events regardless of planning window. Missing or invalid planning window is a configuration gap: request an explicit answer interactively, and do not propose availability until resolved. When the user explicitly declined personal planning suggestions (`planning_window_start` and `planning_window_end` null), do not propose focus or personal-planning time at all; day orientation still uses the configured work/rest pattern, unless the user explicitly requests such reasoning.
- Build a brief natural orientation from today's work/rest pattern, Calendar and useful weather; do not turn rest days into productivity plans.
- Apply standard-recovery and financial-safety scopes above; do not replay ordinary past appointments/social/travel/context events.
- Do not broadly mine future Calendar to manufacture candidates.
- Freeze exact Calendar identity for every displayed event; use artifacts.md and the selected adapter for hidden capture, persistence and narrow recovery. Never expose IDs.

### 2.2 Gmail

Morning is not an inbox digest. Classify Gmail meaning/action eligibility only through `rules.md`. Omit routine low-signal or previously handled unchanged mail even if found again in the rolling search window; consolidate issues and prefer targeted reads.

When Gmail is approved, pass the selected Gmail result/status into the Daily Briefing according to the required artifact schema in `policies/artifacts.md`.

### 2.3 Ledger-first reconciliation

**Before** treating any Calendar/Gmail/recovery signal as a new candidate, apply the complete Ledger reconciliation precedence and standing-precedent semantics from `policies/rules.md`. This workflow owns **when** reconciliation runs; Rules owns what each reconciliation outcome means.

Only signals that remain genuinely new after that reconciliation proceed to new-candidate handling below.

### 2.4 Supporting Context

Daily Memory is historical context, not current state. PARA is pull-only. Weather is optional and plan-linked.

## 3. Operational State

### 3.1 Morning Eligibility Gate

Partition Ledger cards **before priority selection or Briefing composition**:

- `Closed` → historical/precedent only; **never routine-reminder eligible**.
- Open card with `revisit` later than today's local date → **Snoozed**.
- Every other open `Action` / `Waiting` / `Upcoming` card → **Eligible Now**.

Set **Visible Now** = Eligible Now minus yesterday's confirmed-decision exclusions in `rules.md` Section 4. Only Visible Now cards receive routine reminders; the same handoff also filters non-Ledger information across the Briefing.

Snoozed-card override, re-snooze and return-to-eligibility semantics follow `policies/rules.md` Section 4 (`revisit`): material new evidence may surface a Snoozed card before its `revisit` date only as a **state-change signal**, never as routine eligibility.

When a `Waiting` card reaches or passes its `revisit` date, do not treat it as unchanged: surface it for ownership reassessment under `rules.md` (still genuinely external -> remain `Waiting`; the user's follow-up is now due -> propose `MOVE -> Action`; materially changed -> the normal lifecycle). Scheduled Morning surfaces and proposes; the interactive write follows the usual authorization rules.

### 3.2 New Candidates

For each qualifying untracked signal remaining after Ledger-first reconciliation, surface it once as a **new Action Ledger candidate** in its natural Briefing location. Scheduled Morning does not write it.

Before finalizing, account for saved-Briefing candidates from each examined date under `rules.md`: every clear candidate must already be represented, reliably Closed/no-action, or re-surfaced for reconciliation. Deduplicate across dates and sources.

### 3.3 Active Coverage

Every Visible Now issue appears substantively exactly once, allocated below.

## 4. Output Composition

Compose one concise Daily Briefing using the exact schema and required-slot/cardinality rules in `policies/artifacts.md`; do not restate those artifact constraints here.

On Sundays, also recap the preceding local Monday–Saturday from saved Daily Memories (identify provisional Auto-Saved versus user-approved Edited records) in the conditional weekly slots. Show the date range and material coverage gaps. Offer only grounded, tentative personal patterns; never invent an insight, turn one into an Action Ledger item, or let the recap repeat routine reminders. ChatGPT native Memory may add long-term context when surfaced, but cannot independently date or verify this week's events.

### 4.1 Briefing-level issue allocation and de-duplication

Build one issue set after reconciliation, keyed by Ledger ID or underlying distinct obligation. Consolidate evidence across sources. Allocate:

1. `What Matters Today`: up to 3 highest-value issues.
2. `Email`: material Gmail changes/new Gmail candidates not consumed above.
3. `Open Loops / Carry Forward`: remaining Visible Now items only.

Keep required Calendar event lines and Gmail status minimal when an issue already has a home. Continued silence is not Email news; a still-visible Waiting card gets its ordinary reminder. If material emails are already covered in priorities, acknowledge that, not a falsely clear inbox.

Before finalizing, verify every Visible Now card appears once; scan **the entire Briefing** (including opening, Calendar, Weather and Flavour) for unchanged decisions/information from yesterday's approved Memory or earlier saved Briefings. Never use a priority, recap, or “no action needed” paragraph to repeat a suppressed item. Prior Briefings suppress stale FYI/email replays, not the ordinary daily reminder of an unresolved Ledger card. Apply exceptions in rules.md.

- Give each substantive issue one primary home.
- Use only the **Visible Now** set for routine active-card coverage; never leak a future-`revisit` Snoozed card into a routine Briefing slot.
- Use Weather / Source Status only when useful.
- Surface behavioural patterns only when `rules.md` evidence thresholds are met.
- Include **exactly one non-weather Daily Flavour item in every Morning Briefing** if any non-weather flavour category remains enabled in `profile.md`. Choose from `humour`, `fun_fact`, `inspiration` and `tiny_challenge`; do not interpret “all enabled” as including all four each day. Add a short `## Daily Flavour` section (normally 1–2 lines) after practical content. Never disguise operational follow-ups as a tiny challenge.
- Rotate categories across days when prior saved Daily Briefings reveal the recent categories; prefer a category not used in the last three Briefings. If history is unavailable, pick a suitable category without claiming novelty. Do not invent factual claims for fun facts; use safe, verifiable general knowledge or omit unsupported details and choose a different category. Humour should be considerate and low-key; inspiration should be a concrete thought, not fabricated quotations; tiny challenges are strictly optional and require no saved follow-up.
- Weather is **separate** from the one daily non-weather flavour slot: include weather only when the user approved web/weather and it is useful or plan-linked. Do not count weather toward the daily flavour slot. If all non-weather categories are explicitly disabled, omit the section and honor that preference.

Outside the Markdown artifact, when new candidates exist, state clearly that they were **detected but not written to the Action Ledger during the scheduled run**.

## 5. Approval Handoff

For Notion, with verified autosave consent, auto-save the initial Briefing with Calendar ID section before finishing the plain conversational output; no save approval button for a successfully saved snapshot. If auto-save fails or is unauthorized, offer the full interactive save preview under storage/notion.md. Offer separate Ledger approval only if a concrete delta exists. For GitHub, follow the Morning approval/save protocol in `policies/artifacts.md`. Use artifacts.md for independent artifact/Ledger approvals and text fallback.

## 6. Write Boundary

Follow the Scheduled Run Write Boundary in `policies/artifacts.md`: Notion auto-saves only its initial Daily page; GitHub is read/output only. Neither may mutate Ledger, Gmail or Calendar.
