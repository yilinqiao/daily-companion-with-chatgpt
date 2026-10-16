---
type: companion-policy
schema_version: 2
scope: artifacts
---

# Daily Companion Artifact Rules

Canonical owner of saved Daily Briefing / Daily Memory representation, approval and persistence safety. State/evidence/Action Ledger meaning belongs to `policies/rules.md`; Morning/Evening own content retrieval, sequence, filtering and conversational selection.

## 1. Artifact Boundary

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
<Sunday only: completed Monday–Saturday recap from approved Daily Memories; show covered dates/gaps>

## Something You May Not Have Noticed
<Sunday only and conditional: specific evidence-grounded tentative observation; omit if unsupported>

## Daily Flavour
<one brief non-weather item per Morning Briefing when enabled; omit only when all non-weather categories are disabled>

## Source Status
<optional; only material limitations/uncertainty>
```

Required: date; configured-timezone generation time; available Calendar events/conflicts; max 3 priorities; explicit Email result whenever Gmail is approved; complete coverage of Visible Now active Ledger items; one non-weather Daily Flavour item each Morning when enabled; weather is independently permission-gated. Eligibility/classification criteria come from Morning + `rules.md`, not this schema.

### Slot observability

- **Calendar** - Calendar approved and the read succeeds: show the included events for the configured local day chronologically, with conflict/timing notes. Calendar approved, read succeeds, but no events exist on any included calendar: say explicitly that Calendar was checked and nothing is scheduled; never present an empty read as "Calendar not connected". Calendar approved but the enumeration/read fails: state that Calendar coverage is incomplete; never imply an empty day from a partial or primary-only read. Calendar not approved: do not read or enumerate it; the Calendar section may be omitted or explicitly say Calendar is not connected; never imply there are no events.
- **Email** - when Gmail is approved the Email section always states the actual result (selected items, an explicit checked-and-clear confirmation, or an unavailable/failure statement); when Gmail is not approved, do not read it, the Email section may be omitted, and never imply Gmail was checked.

### Hidden Calendar identity metadata

When Calendar is approved and the connector exposes stable event identity, the saved Daily Briefing may carry one hidden HTML comment immediately after the corresponding human-readable Calendar event line in this exact logical form:

```markdown
<!-- dc-calendar: {"calendar_id":"<calendar id>","event_id":"<event id>"} -->
```

**Preview rule:** never render this comment, `calendar_id`, `event_id` or equivalent machine identity in the scheduled Morning preview, approval artifact or surrounding user-facing conversation. Morning keeps the event-to-identity mapping internal to the same run/conversation while presenting only the human-readable Calendar content.

**Save-time injection rule:** after explicit Morning approval, inject the hidden comment into the saved Briefing from the connector identity already frozen during the approved Morning generation whenever that mapping is still available. If the frozen mapping did not survive the scheduled-to-interactive handoff, a **narrow identity-only Calendar refresh is allowed at save time**: re-read the approved local day across the same included calendars and match each approved Calendar event against current Calendar data using the approved event's original title plus original start/end time. Accept the refreshed identity only when the match is unique across the included calendars; use location or other already-approved visible details only as additional disambiguation, never to loosen the match. If the event has moved, disappeared, changed title/time, the Calendar read fails, or more than one candidate matches, omit metadata for that event rather than guessing. This refresh is for machine identity only and must never update, reinterpret, reorder or regenerate the approved visible Briefing. Never invent, normalize, hash or infer an ID.

Verify after save that the user-visible Briefing still matches the approved preview and that any injected identity values exactly match the connector values selected through the permitted frozen-mapping or identity-refresh path. The metadata exists only for Morning-to-Evening reconciliation so Evening can distinguish the same event being rescheduled from a merely similar future event; it is not Action Ledger state and must not itself create, close or change a task.

## 3. Daily Memory Schema

```markdown
---
type: daily-memory
date: YYYY-MM-DD
---

# Daily Memory — <date>

## Done Today
<Evening-selected confirmed completions + meaningful things that happened today>

## Carry Forward from Today
<Evening-selected today-scoped unresolved matters>

## Saved Today — Slurped Pages
<optional; every approved Slurped Page captured today, using the title plus one short context line; omit if none>

## Things I Explored Today
<conditional; required if one or more meaningful, reliably same-day cross-chat highlights or first-party-confirmed exploration highlights were surfaced in Evening; merge related topics, preserve distinct highlights, omit if none>

## Day Summary
<2–5 natural synthesis sentences>

## Reflections
<optional: emotions, concerns, joys or unresolved personal questions expressed today, including reliably dated cross-chat context; draft subject to user approval>

## Tomorrow — Gentle Heads-up
_As things stand tonight:_
<optional preparation advice from tomorrow Calendar + relevant approved/available weather>

## Good Night
<one concise warm/playful/calming sign-off>
```

Tomorrow is optional. `Saved Today — Slurped Pages` is conditional: if Evening surfaced one or more approved Slurped Pages captured on this date, the Daily Memory must preserve that complete set under this section and may not drop items during synthesis. Keep each item concise, normally the page title plus one short context line. Omit the section only when no Slurped Pages were captured today.

`Things I Explored Today` is conditional but **mandatory when at least one qualifying highlight was surfaced in the Evening Check-in or confirmed by the user**. Preserve every distinct qualifying theme into the approved Daily Memory; merge related discussions concisely and avoid duplicating `Done Today` or `Carry Forward from Today`. It may contain only personal/exploration highlights that Evening can reliably assign to this local date using thread/conversation timestamp metadata, or that the user explicitly confirms belong to today. The conversation text need not say `today` when reliable metadata establishes the date. Topic-only recall, ChatGPT native Memory, or vague `recently` context is insufficient for date assignment: omit it or ask for confirmation rather than guessing. Omit the section only if no qualifying highlights remain after user corrections. This section is not a transcript, must never be described as complete coverage of the user's chats, and cannot by itself authorize or imply Action Ledger changes. Retrieval coverage/failure remarks belong in the Evening Check-in, not the saved Daily Memory. User corrections during the Evening check-in take precedence.

`Reflections` is optional. Proactively include concise, reliably same-day emotional/personal reflections surfaced from approved conversation context or the Evening check-in, even without a separate user prompt. Preserve the user's meaning, avoid diagnosing emotions or inventing motives, and allow correction/removal in the normal full-preview approval. Omit if nothing qualifies; neither native ChatGPT Memory alone nor an undated recollection establishes a same-day reflection. Sunday weekly slots use saved Daily Memories as primary evidence; native Memory is optional background, never sole proof of a weekly event or pattern.

If nothing from today carries forward, say so briefly rather than importing older untouched Ledger items. Do not repeat facts or create routine long-term-memory sections.

## 4. Scheduled Run Write Boundary

Scheduled Morning/Evening execution is **read-and-output only**. It must not create, update, delete or commit Daily artifacts, `action_ledger.md`, or any other repository file. It also must not modify Gmail or Calendar.

Within Morning/Evening, a repository write may happen only after an interactive follow-up and applicable authorization/approval. Extra's separate engine permits only its own expressly authorized scheduling/delivery state writes; that exception never permits Daily artifacts or Ledger changes.

## 5. Approval and Save Protocols

### Preferred interactive approval panel and text fallback

When the client supports interactive controls, **prefer one compact approval panel outside the Markdown artifact** instead of asking for a prose-only `approve` reply. Present the complete Daily artifact and every concrete inferred/source-derived Ledger change proposal **before** the panel; users must be able to inspect exactly what each approval covers. Use the output language in `profile.md` for labels. This is a presentation preference, **not** a guaranteed client capability or a relaxation of approval requirements.

- **Morning:** independent options `Save Daily Briefing` and `Apply Action Ledger changes`. **Evening:** after the user's check-in answers and the complete Memory/proposal preview, independent options `Save Daily Memory` and `Apply Action Ledger changes`.
- For each *applicable, ready-to-approve* option, show a separately labeled checkbox, **selected by default** for convenience. A checked default is only a draft interface state: **no authorization exists until the user explicitly submits the choices in an interactive follow-up turn**. An unchecked option means **withhold/skip this write**, not `discard`, `CLOSE`, or agreement that its content is correct.
- Show the Ledger option **only when a specific proposed Ledger delta exists and has been displayed**. Do not use a generic Ledger checkbox to pre-authorize unknown future changes, silently admit candidates included only in the Briefing, or bypass fresh-Ledger/concurrent-change checks. If no Ledger changes are proposed, show only the artifact option and say no Ledger update is proposed when useful. If a prerequisite for one write is unavailable, disable/omit that option with a concise explanation; do not imply it is approved.
- Include an optional free-text `Changes / comments` input and one clearly labeled final `Confirm selected approvals` action. Selection/toggling or typing is not submission. The final action must **send the exact per-item selections and comments into the normal interactive conversation**, where the assistant interprets and executes only selected, eligible operations under this policy. Do not implement a visual-only button that claims to have committed a file, or let the UI directly bypass connector authorization, fresh-read, reconciliation and verification.
- If the comment requests a substantive edit or is ambiguous about the content being approved, **do not save the affected artifact or apply the affected inferred Ledger proposal in the same submission**. Resolve the comment, show a complete revised artifact and/or explicit revised Ledger delta, and request a **fresh approval**. A clear correction that affects both blocks both. Never assume a default checkmark authorizes a revision the user has not seen.
- **Independent results:** artifact selected / Ledger unselected → save only the exact approved artifact; Ledger selected / artifact unselected → apply only the displayed, approved Ledger delta; both selected → attempt both separately, fresh-read current Ledger, verify each result, and report per-item success or failure. Neither selected → no writes. Do not describe a partial failure as full success. Previously explicit first-party state instructions retain their existing direct-authorization rule; the panel does not silently revoke or expand that distinct authority.
- **Text fallback is mandatory:** when interactive widgets are unavailable, unreliable, unsupported in Scheduled Tasks, or the user prefers text, present a concise paired text decision such as `Briefing/Memory: approve | change | skip; Ledger: approve | change | skip` (omit Ledger when no explicit delta). Accept equivalent natural-language replies such as `approve both`, `approve Memory only`, or specific corrections, but map each approval only to a fully presented, identifiable proposal. If anything is unclear, ask the minimum clarification before writing.
- Keep the panel, response summary, citations, buttons and UI metadata **outside saved Markdown**. A Scheduled Task may display a preview and, when available, the panel, but it must never commit Daily artifacts or Ledger state itself. Actual saving happens only in an authorized interactive follow-up and must respect this installation's backing store (a configured private GitHub repository). Never save private daily artifacts or Ledger data to the public template repository.

### Shared

Before approval, do not save Daily artifacts or **inferred/source-derived** Action Ledger changes. Requested artifact edits are shown again without saving. If the user explicitly refreshes live sources, the refreshed proposal needs new approval.

An explicit first-party instruction about a specific existing card's state (for example “this is done”, “we're waiting”, “keep this open”, “move this to Upcoming”) is itself authorization for that specific Ledger state change in an interactive turn; do not require a redundant second approval. A manual Kanban move already present in the file is likewise authoritative state, not a proposal.

On an approved/authorized write:
- start from a current Ledger when changing operational state;
- freeze exact approved **user-visible** Daily artifact content before saving;
- do not re-retrieve/re-analyse/rewrite approved visible content for saving; only explicitly defined hidden machine metadata may be injected under its own contract;
- apply only authorized/approved Ledger changes and preserve unrelated state/order/plugin settings where possible;
- verify filename/location/type/non-zero/exact intended content and no conversation/citation leakage;
- return the GitHub file or commit link outside the artifact when relevant.

Never silently overwrite or duplicate an existing Daily filename. If `action_ledger.md` changed after a proposal was generated, reconcile against the newer file instead of overwriting it.

### Morning

Scheduled Morning only presents the human-readable Briefing; hidden Calendar IDs/comments are never shown in the preview. After explicit approval, save the approved user-visible Briefing exactly and inject only the hidden `dc-calendar` comments defined above. Prefer the frozen Morning identity mapping when available; if it did not survive the handoff, use the narrow identity-only Calendar refresh defined above. The refresh may recover IDs only for exact uniquely matched approved events and may not change approved visible text. If no confident unique identity is available, omit the comment for that event rather than guessing. Briefing approval does **not** implicitly admit new candidates to the Ledger; a source-derived candidate needs a separate interactive Ledger proposal/approval unless the user directly instructs the state change.

### Evening

Scheduled Evening only presents the check-in. After the user answers:
1. require a successful `action_ledger.md` read for authoritative inferred changes;
2. apply any explicit first-party state instructions under the direct-authorization rule above;
3. use Evening + `rules.md` to draft the complete Daily Memory and any remaining inferred Ledger change proposal;
4. ask approve/change/discard for the Daily Memory and inferred proposal;
5. on approval, save the exact Memory and apply only the approved/authorized state changes;
6. verify the Daily Memory and authorized Ledger writes completed successfully.

## 6. Interactive Action Ledger Persistence

Start from a `action_ledger.md`; never reconstruct current state from Daily Memory.

- Determine Ledger operation, card identity/history, status/lifecycle meaning, manual-Kanban meaning and any reliable metadata normalization only through `policies/rules.md`; do not redefine those semantics here.
- Source-derived/inferred Ledger changes require explicit approval; direct first-party state instructions for a specific card follow the direct-authorization rule above.
- Apply only the approved/authorized operation to the fresh Ledger and preserve unrelated state, Kanban headings/order where possible, plugin settings, hidden `dc` metadata and historical records.
- Write only values that are reliably supported under `rules.md`; never invent missing operational metadata merely to normalize the file.
- On an authorized interactive Ledger write, stamp the file frontmatter `updated_at` per the file contract in `rules.md` Section 2 (`File frontmatter`); scheduled runs never stamp it.
- Do not silently create/rewrite Daily Memory outside its own approval flow.
