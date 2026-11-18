---
type: companion-policy
schema_version: 2
scope: artifacts
---

# Daily Companion Artifact Rules

Canonical owner of saved Daily Briefing / Daily Memory representation, approval and persistence safety. State/evidence/Action Ledger meaning belongs to `policies/rules.md`; Morning/Evening own content retrieval, sequence, filtering and conversational selection.

## 1. Artifact Boundary

Select the private storage adapter before any save. Notion initial automatic records are explicitly authorized at setup, provisional Evening is not user-confirmed, and initial chat is ordinary text rather than a full Markdown approval preview. GitHub follows the interactive-only protocol below. The following approval requirements apply to revisions and inferred Ledger changes on both backends.

The artifact shown for approval is one clean Markdown block containing exactly the **user-visible content** that will be saved if approved. Hidden machine metadata explicitly defined in this file is excluded from the approval preview and may be inserted only at save time under its own contract; apart from that narrow exception, saved user-visible Markdown must match the approved artifact exactly. Keep citations/UI markers, approval prompts, tool commentary, machine IDs and status text outside the user-facing artifact. Requested visible-content edits require the complete revised artifact to be shown again; refresh live sources only when explicitly requested.

## 2. Daily Briefing Schema

```markdown
---
type: daily-briefing
date: YYYY-MM-DD
generated_at: "<local ISO-8601 datetime>"
---

# Daily Briefing — <date>

<1–3 sentence natural opening>

## What Matters Today
<up to 3 highest-value items>

## Calendar
<today chronologically; conflicts/timing notes>

## Email
<Morning-selected Email result; classification comes from rules.md>

## Open Loops / Carry Forward
<remaining Visible Now Action Ledger items>

## Weather
<optional; only when useful and approved>

## This Week
<Sunday only: completed Monday–Saturday recap from saved Daily Memories, distinguish provisional and confirmed; show covered dates/gaps>

## Something You May Not Have Noticed
<Sunday only and conditional: specific evidence-grounded tentative observation; omit if unsupported>

## Daily Flavour
<one brief non-weather item per Morning Briefing when enabled; omit only when all non-weather categories are disabled>

## Source Status
<optional; only material limitations/uncertainty>
```

GitHub includes YAML and H1; Notion uses native properties and body without duplicate H1/YAML. Required: date; configured-timezone generation time; available Calendar events/conflicts; max 3 priorities; explicit Email result whenever Gmail is approved; complete coverage of Visible Now active Ledger items; one non-weather Daily Flavour item each Morning when enabled; weather is independently permission-gated. Eligibility/classification criteria come from Morning + `rules.md`, not this schema.

### Slot observability

- **Calendar** - Calendar approved and the read succeeds: show the included events for the configured local day chronologically, with conflict/timing notes. Calendar approved, read succeeds, but no events exist on any included calendar: say explicitly that Calendar was checked and nothing is scheduled; never present an empty read as "Calendar not connected". Calendar approved but the enumeration/read fails: state that Calendar coverage is incomplete; never imply an empty day from a partial or primary-only read. Calendar not approved: do not read or enumerate it; the Calendar section may be omitted or explicitly say Calendar is not connected; never imply there are no events.
- **Email** - when Gmail is approved the Email section always states the actual result (selected items, an explicit checked-and-clear confirmation, or an unavailable/failure statement); when Gmail is not approved, do not read it, the Email section may be omitted, and never imply Gmail was checked.

### Calendar identity (both backends)

Freeze exact connector calendar_id + event_id and stable approved account_id when available for each approved Calendar line during Morning. Older two-ID records remain valid; resolve access through approved accounts only. Never show IDs, `dc-calendar` comments or the protected identity section in any user-facing preview. The selected adapter owns serialization. If frozen mapping is unavailable, re-read only the original local day across the same included calendars; match original title plus exact original start/end uniquely, with already-approved visible details only as disambiguation. If moved, disappeared, changed, incomplete or ambiguous, omit identity rather than guessing. Never refresh approved visible text. Preserve original linkage during revisions; verify exact connector IDs, visible content and original linkage after save. Identity is for Evening reconciliation, not Ledger state.

## 3. Daily Memory Schema

GitHub includes this YAML and H1; Notion stores title/date in properties and saves the section body only. Same visible content is used for the full approval preview.

```markdown
---
type: daily-memory
date: YYYY-MM-DD
---

# Daily Memory — <date>

## Today's Journal
<User's narrative in their own voice, or evidence-supported provisional account>

## Other Updates & Explorations
<distinct meaningful events, confirmed outcomes, lessons or explorations not in Journal>

## Carry Forward from Today
<today-scoped unresolved matters and next steps>

## Saved Today — Slurped Pages
<all surfaced approved captured pages, original links and one short context line per page>

## Reflections
<optional emotions, concerns, joys, personal questions; reliably dated cross-chat context>

## Tomorrow — Gentle Heads-up
_As things stand tonight:_
<material preparation advice>
```

Journal first; include only applicable additional sections. Preserve each meaningful, reliably dated highlight exactly once, including all surfaced capture links and distinct explorations, with user corrections taking priority. No separate Done Today, Things I Explored Today, Day Summary or Good Night. Do not import untouched Ledger cards. Keep retrieval diagnostics outside Memory. Reflections preserve the user's meaning, do not diagnose or invent motives, and are subject to user approval of the full revised Memory. Native Memory or undated recall cannot date a highlight. Sunday uses saved records and labels provisional coverage.

## 4. Scheduled Run Write Boundary

Notion: only own initial Daily page auto-save under storage/notion.md and setup consent. GitHub: Morning/Evening read-and-output only; Extra is read-only on both backends. No scheduled Ledger, Gmail or Calendar mutation. Never overwrite user-edited records during scheduled execution.

## 5. Approval and Save Protocols

### Preferred interactive approval panel and text fallback

Prefer a compact interactive approval panel outside the Markdown when supported; otherwise mandatory text fallback. Show complete artifact and specific inferred Ledger delta before asking. Use configured language.

- Separate ready options: Save Daily Briefing/Memory and Apply Action Ledger changes (only when a concrete delta is shown). Default checked is convenience, not permission. Unchecked means withhold this write, not discard or close.
- Optional changes/comments field and one explicit Confirm selected approvals button. Submission must send exact selections/comments into the interactive conversation; no direct UI writes or visual-only claim of success.
- Substantive or ambiguous correction blocks affected write(s); show revised full artifact/delta and seek fresh approval. Unavailable prerequisites disable/omit that option.
- Execute only submitted selected operations, independently; report individual verified results. Neither selected means no writes. Direct first-party instructions remain separately authorized.
- Text fallback: `Briefing/Memory: approve | change | skip; Ledger: approve | change | skip` (omit missing delta). Accept clear natural language; clarify ambiguity. Keep prompts, buttons, citations and status outside saved artifact.

### Shared

Except initial Notion auto-save under standing setup authorization, do not save Daily artifacts or **inferred/source-derived** Action Ledger changes before approval. Requested artifact edits are shown again without saving. If the user explicitly refreshes live sources, the refreshed proposal needs new approval.

An explicit first-party instruction about a specific existing card's state (for example “this is done”, “we're waiting”, “keep this open”, “move this to Upcoming”) is itself authorization for that specific Ledger state change in an interactive turn; do not require a redundant second approval. A manual Kanban move already present in the file is likewise authoritative state, not a proposal.

On an approved/authorized write:
- fresh-read private instructions, profile, relevant workflow, artifact policy, selected adapter and applicable Ledger rules; revalidate destination, current consent and scope, without broad source refresh. If required rules are unavailable, stop affected writes. If current rules, destination, artifact or delta change the approved operation, seek fresh approval before writing;
- start from a current Ledger when changing operational state;
- freeze exact approved **user-visible** Daily artifact content before saving;
- if the user edits an editable preview directly, save only the final approved edited content; if it is inaccessible, request the revised text or changes and fresh approval rather than saving the original;
- do not re-retrieve/re-analyse/rewrite approved visible content for saving; only explicitly defined hidden machine metadata may be injected under its own contract;
- apply only authorized/approved Ledger changes and preserve unrelated state/order/plugin settings where possible;
- verify filename/location/type/non-zero/exact intended content and no conversation/citation leakage;
- return the verified private page or GitHub file/commit link outside the artifact when relevant.

Never silently overwrite or duplicate an existing Daily artifact; Notion uses date + category and exact page identity. If the Ledger changed after a proposal, reconcile against the fresh state before writing.

### Morning and Evening

Initial Notion snapshots follow storage/notion.md; after a successful Morning auto-save offer only an applicable independent Ledger proposal. If auto-save fails or is unauthorized, offer an interactive artifact save. Evening waits for answers before full revision preview. GitHub Morning shows complete Briefing before approval; GitHub Evening waits for answers before complete Memory preview. Follow shared approval panel/text fallback for all interactive saves. No Ledger change is implied by saving a Daily page. Preserve exact Calendar identity per adapter.

## 6. Interactive Action Ledger Persistence

Fresh-read configured Ledger and current schema/state; never reconstruct from Daily Memory. Use rules.md for operation meaning and selected adapter for verified persistence. Preserve unrelated rows/cards/history, apply only approved or direct first-party changes, and do not silently rewrite Daily artifacts.
