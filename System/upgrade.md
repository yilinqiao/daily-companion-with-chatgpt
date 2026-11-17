---
type: companion-upgrade
schema_version: 2
---

# Daily Companion Upgrade

Private interactive upgrade only; canonical source is `yilinqiao/daily-companion-with-chatgpt`. Never upload private data or automatically switch backend.

## 0. Scheduled update watch (read-only)

Read installed markers from the verified private profile and public VERSION + matching CHANGELOG at one immutable default-branch commit. The watch must never modify any source or task. Compare semver; notify only verified newer release or material read/metadata failure; unknown baseline requires verification, unchanged means silent. Invite interactive review of a concrete diff, not approval to apply. No persistent notification state; platform completion alerts may still occur.

## 1. Compare

Confirm private backend, scope, identity and access. GitHub verify private visibility/path; Notion verify mapped pages/source identities. Pin candidate and installed upstream baseline by SHA when known; verify VERSION and matching notes. For unknown/unversioned baseline compare files conservatively; no assumed downgrade, no reset. Check for updates stops here. Labels alone don't prove content.

## 2. Propose specific changes

Three-way compare where baseline is verified. Source-owned rules, setup, selected adapter and docs may be merged; preserve customizations, profile settings/consents, Daily history and original Calendar linkage, all Ledger cards/rows/IDs/order/metadata and schemas/views. Preserve Extra history and state except explicit approved migration. Don't overwrite same-named personal files or delete upstream-removed private content without specific approval. Review actual existing task prompts against current minimal templates, including all three Evening fallback questions; propose only necessary changes, separately approved, preserve title/times/timezone/paused state/notification preferences. Existing installations are **not** silently given a new task; offer new tasks separately with explicit task-activation approval. Never rerun setup.

### v0.5.0 migration

- Profile v5 → v6 adds private `gmail_account_ids` and `calendar_account_ids` lists. For each previously approved service, confirm and verify the original account scope interactively using setup's read-only checks; add further accounts only with explicit permission. Declined services keep empty lists. Preserve existing Calendar exclusions, all history and settings. If account identity or access cannot be verified, report the gap and leave that scope unapplied until resolved or explicitly reduced; never broaden access by default. No task prompt or schedule change is required. Apply the new rules and profile together under §3.

### v0.4.1 migration

- New setup/notion.md and setup/github.md are onboarding only. Add selected file to mapped System if needed; update index, verify required runtime routes. No rewriting historical Daily pages. For Notion, inspect current schema and views; propose any needed Category multi-select / numeric version changes without losing existing values. Existing correct mappings may be retained explicitly. Resolve missing planning window interactively, never default null. Preserve existing approved capture source; if missing mapping, confirm exact locator and capture date field interactively, otherwise leave unconfigured.
- Already valid Notion 104-week anchor/pattern: preserve exactly; map old field names if required, retain enabled/feedback. No redraw, including on no-op.
- Legacy GitHub v6 (or older) cadence: disclose removal of scheduled writes, overdue catch-up and delivery claims; archive full prior state privately, including pending claims and reliable attempt history, without interpreting a claim as delivery. Obtain explicit approval to replace cadence with anchor_monday and weekday_pattern valid per engine; use first complete local week after migration, preserve enabled/feedback and custom rules. Remove obsolete scheduled authorization/claim fields only in approved migration. No silent replay or reset. Align new provisional anchor if migration crosses a week boundary. Suspend only previously enabled affected Extra with approval before coordinated engine/prompt change; if task inventory or required prompt change cannot be verified, stop before migration. No new tasks without separate approval.
- Earlier release migration notes: see the immutable v0.4.0 release's System/upgrade.md and CHANGELOG; historical instructions are context only, superseded by current read-only engine and write boundaries. For old Ledger schemas preserve data, reconcile Pending Admission/pending_close interactively and never invent closure dates. Optional reflection/weekly slots do not require rewriting history; retain notification guidance.

## 3. Apply approved changes

Obtain explicit approval of concrete diff, schema changes, task changes and any migration. Fresh-read affected private sources; if changed since preview, reconcile and obtain fresh approval. Before non-atomic writes that could leave active workflows inconsistent, suspend affected enabled tasks with approval; if required suspension is unavailable, leave upgrade unapplied. Notion snapshot each previous System body under Versions and verify, then patch, increment numeric version and verify. GitHub use fresh SHA for each approved file or verified atomic commit; preserve unrelated state, read back. Stop on any access, safety, conflict or verification failure; report partial results and leave installed markers unchanged until other changes verified. No bypass or broad rollback. A repair/rollback needs a new concrete proposal preserving intervening edits.

Once rules, mappings, chosen schema, state and authorized task prompts are verified, update installed_template_version and installed_template_commit to verified public baseline SHA, then read back (GitHub also verify VERSION label). If a label/marker write fails, report partial and retry only pending state. Keep setup status separate. Resume only previously enabled tasks suspended for approved upgrade after verification; never enable user-paused or absent tasks. Actual scheduled persistence and notifications require observed runs, not static checks or interactive access. Report per-task configuration/activation/observed status separately.

No approval/no changes means no writes. If access is unavailable, prepare a reviewable proposal and report what remains unapplied.
