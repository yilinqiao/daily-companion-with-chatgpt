---
type: companion-policy
schema_version: 2
scope: shared-rules
---

# Daily Companion Rules

Canonical owner of shared meaning, evidence, Action Ledger state and continuity semantics. Workflows own retrieval order, run sequence, filtering and conversational actions; `artifacts.md` owns saved schemas, approval and persistence. Non-owner files may invoke these semantics but must not redefine their qualification/evidence criteria.

## 1. Information Model and Source Authority

- **Daily Briefing**: approved Morning snapshot; historical once saved.
- **Daily Memory**: approved human end-of-day record; historical once saved; not current operational state.
- **Action Ledger** (`action_ledger.md`): single source of truth for unresolved and historical operational items. Fixed Kanban lists: `Action`, `Waiting`, `Upcoming`, `Closed`.
- **PARA / other vault notes**: pull-only project/domain/context background; never auto-import task prose into the Ledger.
- Stable user configuration belongs in `profile.md`; durable operational handling knowledge belongs in the Action Ledger; project/domain context stays with its source/area. Do not create a separate global long-term-memory state file. A feature-owned delivery/state file such as `daily_companion_extra.md` is not a long-term-memory store and does not violate this rule.

Source authority: Calendar → current event details; Gmail → current email state; `profile.md` → configuration/location/region; Action Ledger → current/historical operational state and standing handling precedents; Daily artifacts → historical snapshots; PARA → project/context background; Slurped Pages → saved pages captured in the vault (Evening surfaces them; `artifacts.md` owns their Daily Memory slot). Report material conflicts.

When Calendar is approved: enumerate all visible calendars; with `include_all`, exclude only configured stable IDs. Newly visible calendars are included automatically. Enumeration failure means incomplete coverage. Regional holiday applicability uses `normal_location` / `region`, not `weather_location`. Context events may affect orientation but do not become tasks merely by existing.

Native ChatGPT Memory may personalize conversation but is never the sole source of truth for portable facts, operational state, completion, or how state changed.

## 2. Action Ledger Schema and Status Meaning

The Kanban list is authoritative status. Do not store a duplicate `status` field in card metadata.

### `Action`

Use when the user, their household, or another known owner needs to take a meaningful action now.

### `Waiting`

Use when the required action has already been taken and the next meaningful step depends primarily on another person, organisation, system or external outcome. When user follow-up becomes due, move to `Action`.

### `Upcoming`

Use when attention is confirmed for the future but no meaningful action is required yet. A due/revisit date alone does not determine status; use the actual action state.

### `Closed`

Use when the loop has clearly ended because it was completed, resolved, confirmed no-action/automatic, cancelled, declined or superseded. Closed cards remain as durable history and are never automatically deleted. Newest Closed cards should appear first; an interactive write that closes a card inserts it at the top of the `Closed` list while preserving the relative order of the existing cards.

A Closed card with `scope: "standing"` is also an active handling precedent for future similar signals until an optional `standing_until` date has passed. Standing precedents are policy-like history, not an open task.

### File frontmatter

`action_ledger.md` carries a small file-level contract in addition to card metadata:

- `type: companion-action-ledger` and `schema_version` identify the file model and its version;
- `kanban-plugin: board` is the Obsidian Kanban file marker;
- `updated_at` records the local ISO-8601 time of the most recent **authorized interactive write**, stamped automatically by the assistant when that write occurs. It is never maintained manually and never updated by scheduled read-only runs. Manual user moves inside the Kanban board are not individually timestamped (the plugin emits no per-card modified date); the current Kanban list position is authoritative and is reflected at the next authorized interactive write.

### Card format and metadata

Each card has:
1. a short human-readable title;
2. a concise visible description of the current next step/wait/outcome;
3. one hidden HTML comment `<!-- dc: {...} -->`.

Core metadata:
- `id`: unique stable kebab-case ID; immutable and never reused;
- `opened`: date first admitted/recorded; immutable;
- `closed`: `null` while open; closure date when reliably known;
- `source`: optional when a clear source exists.

Optional metadata: `owner`, `due`, `revisit`, `resolution`, `scope`, `standing_until`.

Preferred `resolution`: `completed`, `no_action`, `cancelled`, `declined`, `superseded`.

Do not add empty optional fields. Do not expose machine fields in the visible title/description.

If a manually moved Closed card has no reliable historical closure date, do not invent one merely to complete metadata; its column remains authoritative and `closed` may stay `null` until reliable evidence exists.

## 3. Admission, Reconciliation and Durable History

Admit/record only a concrete unresolved obligation, follow-up, commitment, dependency, meaningful loose end, or an operational loop that has been explicitly assessed and needs durable closure/handling history. Do not turn every fact, idea, conversation, FYI or ordinary event into a Ledger card.

### Calendar

Calendar is evidence, not a task list.

- Ordinary appointments/meetings/travel/social events normally stay Calendar-only.
- Relevant future dated commitment may qualify for `Upcoming`.
- Concrete unresolved obligation may qualify for `Action`.
- User-action financial obligations/money movements are strongly action-like whenever action or confirmation remains outstanding: transfers, repayments, levies, rates, bills, invoices, fees, tax, premiums, deposits, settlement payments and refunds requiring follow-up.
- Already handled, reliably automatic or purely informational financial events are not active actions.
- Interpret semantics, not keywords alone; ambiguity requires minimum clarification.
- Time passage/disappearance is never completion evidence.

### Gmail

Gmail is evidence, not a task list.

- Concrete unresolved ACTION → eligible `Action`.
- Genuine unresolved external dependency → eligible `Waiting`.
- FYI → context only.
- Read/unread state, lost prominence, search-window disappearance or silence is never resolution.

### Reconciliation precedence

Before treating a new Calendar/Gmail/other source signal as a new candidate, reconcile it against the Action Ledger in this order:

1. **Same active underlying item** → update/reuse that card; never duplicate it.
2. **Same specific Closed obligation** → treat it as already handled unless reliable evidence shows the loop genuinely reopened.
3. **Applicable standing precedent** → apply it when still valid. If there is no material exception/change, suppress routine candidate creation. If a material exception appears, surface/reclassify the new operational issue.
4. **Otherwise** → classify as a genuinely new candidate.

Same category/entity is not enough to call something the same obligation. A new billing period, new deadline or materially new obligation can be a new card. If identity is genuinely ambiguous and silent merging could hide meaningful work, ask/surface minimally rather than silently merge.

**Standing-precedent exceptions keep the precedent intact.** A material exception (for example a debit failure, an overdue/manual-action request, or a change that creates a new manual obligation) is a new operational issue: surface/classify it normally - usually as a new open card - and leave the standing Closed record in place so it continues to suppress future routine signals. Do not REOPEN a standing Closed card merely because one routine signal failed. Only when the user confirms the underlying arrangement itself has ended or changed should the precedent stop suppressing routine signals: record that reliably (for example a past `standing_until` on the standing card) and classify the new state under the normal lifecycle.

A standing precedent uses semantic relevance from its human-readable title/description/context; do not require a brittle keyword list. A `standing_until` in the past means the precedent remains historical but no longer suppresses new signals.

### Candidate persistence

Detection/surfacing during Scheduled Morning/Evening is not a repository write. New unresolved candidates require an interactive authorized/approved state change before entering an open list.

When a clear operational candidate is explicitly assessed and its loop is confirmed ended (`completed`, `no_action`, `cancelled`, `declined`, `superseded`), retain a Closed record when it provides useful durable operational/de-duplication history. A standing precedent should usually replace repeated per-cycle no-action cards; do not create a new Closed card for every routine recurring bill already covered by the same standing rule.

Every clear candidate surfaced in an approved Morning Briefing must later have an explicit operational outcome: already represented in the Ledger, reliably Closed/no-action, approved/authorized for open admission, or still unresolved and re-surfaced for reconciliation. A Daily Memory file is not proof that candidate reconciliation succeeded.

## 4. Lifecycle, User Authority and Dates

Normal lifecycle operations:

- **KEEP**: no material change.
- **UPDATE**: same card, meaningful content/metadata change.
- **MOVE**: same open loop changes between `Action` / `Waiting` / `Upcoming`.
- **CLOSE**: move the same card to `Closed`, change `[ ]` → `[x]`, set reliable `closed` date, update visible outcome and add useful `resolution`. Preserve any existing `due`/`revisit` values as historical record: they become inert while Closed and are not cleared by CLOSE.
- **REOPEN**: when clearly the same underlying loop becomes active again, move the existing card to the correct open list, change `[x]` → `[ ]`, set `closed: null`, remove stale `resolution`, preserve original `id` and `opened`.
- **DELETE**: exceptional; only for explicit removal of an erroneous/duplicate/history record. Closure never means deletion.

Unmentioned existing cards default to KEEP. Valid closure evidence includes explicit user completion/no-action/cancellation/decline, reliable source confirmation, or clearly superseding later state. Absence from sources/artifacts and passage of time are not closure.

Explicit user statements about a card's state take priority over inference. Examples:
- “keep this open” → keep open;
- “this is done” → CLOSE;
- “we're waiting for them” → MOVE to `Waiting`;
- “I don't need to do anything; it's direct debit” → CLOSE with `resolution: "no_action"`; use `scope: "standing"` when the statement clearly establishes an ongoing handling rule;
- “remind me later; nothing to do now” → usually `Upcoming` or a `revisit` on the actual current status, depending on meaning.

Manual Kanban moves are first-party state changes. Treat the current list as authoritative unless clear evidence indicates an accidental move. Do not silently undo it because older Daily Memory/source text disagrees. When later writing interactively, normalize checkbox/metadata where reliably possible without inventing dates.

### `revisit`

`revisit` is a follow-up trigger, not status and not completion.

A future `revisit` date snoozes **routine Morning reminders** until that local date. On that date and thereafter, routine reminders resume unless the card is Closed or re-snoozed. Material new evidence may surface during the snooze as a state change; it does not make the card routine-eligible early.

### Yesterday handoff

For the next Morning only, suppress a routine repeat when yesterday's **approved Daily Memory** records that the user explicitly acknowledged an open issue and decided its next step (including waiting or deferring without a date). Do not infer acknowledgement from a mere mention or an unapproved draft. Keep the Ledger card open and resume normal daily reminders afterward. A due action today, an explicit request to remind this morning, or material new evidence overrides this one-morning suppression. A confirmed later `revisit` continues to follow the normal snooze rule. Closed/no-action items stay excluded under their existing rules.

### Dates

- `opened` is immutable.
- `closed` records the reliably known date the loop ended; do not invent it.
- `due` is a genuine deadline/committed date; it does not determine status.
- `revisit` controls when routine follow-up resumes; it does not determine status.

## 5. Financial Safeguard and Reliability

Financial items require a higher standard before closure. Do not assume another person handled it, payment is automatic, or a transfer probably happened.

Close/record no-action only with explicit/reliable evidence such as paid, transferred, settled, confirmed direct debit/automatic payment, or explicit user confirmation that no manual action is required.

If a standing automatic-payment precedent exists, routine matching notices remain quiet unless payment fails, becomes overdue, requests manual action, the arrangement changes, or another material exception appears.

Do not state behavioural patterns without evidence. Default minimums:
- repeated unfinished → unresolved in at least 2 relevant daily records;
- repeated deferral → at least 2 explicit deferrals/carry-forwards;
- stale waiting → explicitly waiting and at least 3 days old unless naturally longer;
- recurring Calendar pressure → at least 3 occurrences;
- repeatedly mentioned but unscheduled → at least 2 explicit mentions/carry-forwards and no current dated commitment or evidence scheduling is unnecessary.

Do not invent continuity; absence is not completion; inference is not stored fact; current state is not proof of how it changed.