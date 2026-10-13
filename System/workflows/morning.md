---
type: companion-workflow
schema_version: 2
scope: morning
---

# Morning Companion Workflow

Morning Scheduled Task entry point. Read `System/instructions.md`, `System/profile.md`, `System/policies/rules.md` and `System/policies/artifacts.md`. This file owns Morning retrieval order, reconciliation sequence, eligibility filtering and surfacing actions; shared meaning/state semantics live in `rules.md`, and saved schemas/approval/persistence live in `artifacts.md`.

## 1. Required Inputs

1. Read `profile.md` and the configured `action_ledger_file`. If the Ledger is unavailable, report it and never reconstruct operational state from Daily Memory.
2. Resolve local date/time in the configured timezone.
3. Attempt each of the previous 7 local Daily Memory dates for context/history. Define **standard Calendar recovery dates** as the consecutive missing Daily Memory dates immediately before today: start yesterday, continue backward only while each date is missing, stop at the first existing Daily Memory, cap at 7. Also read yesterday's approved Daily Briefing when available for candidate continuity.
4. If Calendar is approved, enumerate all visible calendars, apply exclusions, and read today's full local day across every included calendar with calendar identity retained. Read standard recovery dates for unresolved-capable signals. Independently perform the narrow 7-day financial safety look-back for the financial-action class in `rules.md`, regardless of Daily Memory checkpoints. Reuse retrieved dates and dedupe recovery paths.
5. If Gmail is approved, review relevant mail from the previous 7 days, excluding Spam/Trash; prefer targeted reads.
6. Use PARA only when live context materially needs background. Normally retrieve at most 3 long-term vault files.
7. Use weather when useful and tied to actual plans.

Use only approved sources.

## 2. Source Processing

### 2.1 Calendar

Classify Calendar meaning, action eligibility and evidence only through `policies/rules.md`.

- Fixed work hours remain occupied unless supported evidence overrides them; do not infer free time from Calendar gaps for variable/none/unknown schedules.
- Reason about personal availability only inside the configured planning window. When no planning window is configured (`planning_window_start` and `planning_window_end` null), do not propose focus or personal-planning time at all; day orientation still uses the configured work/rest pattern, unless the user explicitly requests such reasoning.
- Build a brief natural orientation from today's work/rest pattern, Calendar and useful weather; do not turn rest days into productivity plans.
- Apply standard-recovery and financial-safety scopes above; do not replay ordinary past appointments/social/travel/context events.
- Do not broadly mine future Calendar to manufacture candidates.
- For every Calendar event rendered into the Daily Briefing, retain stable source identity when the connector exposes it: `calendar_id` plus `event_id`. During the scheduled Morning preview, keep this event-to-identity mapping internal to the run/conversation and **do not render IDs or `dc-calendar` comments anywhere in the user-facing Briefing or surrounding conversation**. On an approved interactive save, `policies/artifacts.md` may inject the hidden Calendar metadata into the saved Briefing as the narrowly defined machine-metadata exception to visible exact-save behaviour. Prefer the connector identity frozen during Morning generation when it is still available. If that mapping did not survive the scheduled-to-interactive handoff, perform only the narrow save-time Calendar identity refresh defined in `policies/artifacts.md`; use it to recover machine identity for exact uniquely matched approved events and never to refresh or rewrite the approved visible Briefing. If identity still cannot be matched confidently, omit the hidden metadata rather than guessing or exposing it. This identity is historical linkage for Evening reconciliation, not operational state.

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

Before finalizing, account for yesterday's approved-Briefing candidates under `rules.md`: every clear candidate must already be represented, reliably Closed/no-action, or re-surfaced for reconciliation.

### 3.3 Active Coverage

Surface every **Visible Now** active card exactly once **at the underlying-issue level, not once per source section**. Coverage is satisfied when that issue is rendered substantively in exactly one of `What Matters Today`, `Email`, or `Open Loops / Carry Forward`. A material Gmail update to an existing Visible Now Ledger card may therefore satisfy that card's Morning coverage in `Email`; it must not then be repeated in `Open Loops / Carry Forward`.

Select the highest-value Visible Now issues for the Briefing's priority slot. Any Visible Now active issue not already consumed by a higher-priority slot or a material Email update falls through to `Open Loops / Carry Forward`, using the exact structure and cardinality defined in `policies/artifacts.md`.

## 4. Output Composition

Compose one concise Daily Briefing using the exact schema and required-slot/cardinality rules in `policies/artifacts.md`; do not restate those artifact constraints here.

### 4.1 Briefing-level issue allocation and de-duplication

Before rendering sections, build one Briefing-level issue set after Ledger reconciliation. Key an existing operational issue by its stable Ledger card ID; key an untracked candidate by the same underlying obligation/dependency/commitment rather than by source, thread, message or section. Merge Calendar/Gmail/recovery evidence that belongs to the same underlying issue into that one issue record.

Assign every substantive operational issue exactly one **primary home**, then mark it **consumed** for operational coverage. Use this allocation order:

1. `What Matters Today` — up to 3 highest-value issues.
2. `Email` — material Gmail changes or genuinely new Gmail candidates not already consumed by `What Matters Today`. A material Gmail update to an existing Visible Now Ledger item counts as that item's one Morning appearance.
3. `Open Loops / Carry Forward` — only remaining Visible Now Ledger items not already consumed above. Treat this section as the remainder/catch-all, never as a second full rendering of the Ledger.

Section observability may still require minimal source text without creating a second substantive issue. For example, a Calendar event may still appear as its event line when Calendar is approved, and the Email section must still report Gmail status when Gmail is approved. If the substantive issue already lives elsewhere, keep that source text minimal and do not restate the action/wait/background.

For Gmail specifically:

- A new reply, decision, request, failure, confirmation or other material state change may justify an Email issue.
- **No new reply / continued silence is not itself an Email issue.** If the underlying Waiting card is still Visible Now, its unchanged state belongs only in its primary operational home, normally `Open Loops / Carry Forward`.
- If all material Gmail issues were already consumed by `What Matters Today`, the Email section may say briefly that important email updates are reflected there and that there are no additional Email items. Never falsely say Gmail was clear when a material update was surfaced elsewhere.

Before finalizing, dedupe by underlying issue across `What Matters Today`, `Email`, and `Open Loops / Carry Forward`; keep its first primary home and verify every Visible Now card appears once. Also scan **the entire Briefing** (including opening, Calendar, Weather and Flavour): remove unchanged issues already handled in yesterday's approved Memory or earlier approved Briefings, unless `rules.md` permits a new reminder. Never use a priority, recap, or “no action needed” paragraph to explain a suppressed item. Prior Briefings suppress stale FYI/email replays, not the ordinary daily reminder of an unresolved Ledger card. Keep required Calendar/source-status facts concise.

- Give each substantive issue one primary home.
- Use only the **Visible Now** set for routine active-card coverage; never leak a future-`revisit` Snoozed card into a routine Briefing slot.
- Use Weather / Source Status only when useful.
- Surface behavioural patterns only when `rules.md` evidence thresholds are met.
- Include **exactly one non-weather Daily Flavour item in every Morning Briefing** if any non-weather flavour category remains enabled in `profile.md`. Choose from `humour`, `fun_fact`, `inspiration` and `tiny_challenge`; do not interpret “all enabled” as including all four each day. Add a short `## Daily Flavour` section (normally 1–2 lines) after practical content. Never disguise operational follow-ups as a tiny challenge.
- Rotate categories across days when prior approved Daily Briefings reveal the recent categories; prefer a category not used in the last three Briefings. If history is unavailable, pick a suitable category without claiming novelty. Do not invent factual claims for fun facts; use safe, verifiable general knowledge or omit unsupported details and choose a different category. Humour should be considerate and low-key; inspiration should be a concrete thought, not fabricated quotations; tiny challenges are strictly optional and require no saved follow-up.
- Weather is **separate** from the one daily non-weather flavour slot: include weather only when the user approved web/weather and it is useful or plan-linked. Do not count weather toward the daily flavour slot. If all non-weather categories are explicitly disabled, omit the section and honor that preference.

Outside the Markdown artifact, when new candidates exist, state clearly that they were **detected but not written to the Action Ledger during the scheduled run**.

## 5. Approval Handoff

Follow the Morning approval/save protocol in `policies/artifacts.md`. After displaying the complete Briefing and any concrete inferred Ledger delta, prefer its **two-choice interactive approval panel** (Briefing + Ledger, each selected by default only when applicable), with a mandatory separate text-choice fallback. A panel selection alone never writes; only submitted interactive approval authorizes the selected operation. Artifact approval and Ledger-state authorization remain separate.

## 6. Write Boundary

Follow the Scheduled Run Write Boundary in `policies/artifacts.md`: Scheduled Morning is read/output only and performs no repository, Gmail or Calendar mutation.
