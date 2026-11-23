---
type: companion-upgrade
schema_version: 2
---

# Daily Companion Upgrade

Private interactive upgrade only; canonical source is `yilinqiao/daily-companion-with-chatgpt`. Use the GitHub connector first to read the latest public System/upgrade.md and required files on the current default branch (main). If not connected, help the user connect GitHub (offer free signup with Google if needed); otherwise use public GitHub file/Raw URLs or Pages if readable (https://yilinqiao.github.io/daily-companion-with-chatgpt/upgrade.html). No downloads/uploads, no mandatory SHA or history lookup. Scheduled Watch uses §0 only. Never upload private data or automatically switch backend.

## 0. Scheduled update watch (read-only)

Read the installed version from the verified private profile and the canonical public VERSION alone. Use the GitHub connector first to read `VERSION` on the current default branch (main); if unavailable or invalid, try [Raw VERSION](https://raw.githubusercontent.com/yilinqiao/daily-companion-with-chatgpt/main/VERSION), the public GitHub file or https://yilinqiao.github.io/daily-companion-with-chatgpt/version.html . Require a valid semver actually read from the file or page, no commit SHA required; do not infer it from search snippets or memory. Compare numerically; if newer, notify with installed/latest version and invite interactive review of a concrete diff, not approval to apply. CHANGELOG is optional: read the current repository CHANGELOG.md via the connector, or https://yilinqiao.github.io/daily-companion-with-chatgpt/changelog.html if available; inability to read notes never blocks notification. Equal or older version: silent. Unknown installed version: no newer-release claim; invite direct interactive file comparison if the profile is readable. Never fetch every System file merely to check for updates.

If public VERSION is inaccessible or invalid after fallbacks, retry next scheduled day; notify only on three consecutive daily failures confirmed by reliably available run history (once per failure streak); otherwise remain silent. Never invent history, infer failure from missing runs or add persistent counters. Report a private profile/access failure briefly without guessing version. The watch must never modify any source or task, never write state or auto-upgrade. Platform completion alerts may still occur. Interactive upgrades retain the full verification below.

## 1. Compare

For interactive "Check for updates", read the installed version and public VERSION as in §0, report the comparison (or version unavailable) in chat; read matching CHANGELOG notes if convenient. Stop there, with no writes, no mandatory full-file diff, and no requirement to obtain a commit SHA.

For "Upgrade Daily Companion", confirm private backend, scope, identity and access. GitHub verify private visibility/path and profile's configured folders; Notion verify mapped pages/source identities against profile. Read current required public System file bodies directly via the GitHub connector on the default branch and current affected private file bodies. Compare actual contents, not only labels. Read public VERSION if available, and CHANGELOG only when useful. Do not require an immutable candidate SHA, installed baseline SHA, tag, commit history, three-way merge, repeated VERSION reads or historical verification. A known version or optional commit already returned may be recorded, but metadata is not a prerequisite for file retrieval or upgrading. If the installed or latest version is unknown, report it and compare actual files conservatively; the user may still approve the concrete rule changes without a known version. If both versions are known, stop on downgrade; do not infer a downgrade from missing metadata. A known incompatible change or actual unresolved conflict needs a separate safe proposal. If required bodies cannot be read, guide reconnect or retry exact paths via public GitHub/Raw/Pages; report missing paths and pause before writes. No user downloads/uploads. Retain the reviewed complete candidate bodies for the approved change; re-read only affected sources if a material content change is known or a needed body is lost. Never use a changed or guessed body without reviewing it and obtaining fresh approval.

## 2. Propose specific changes

Compare current private and latest public rules directly; use a historical baseline only if already available and genuinely useful, never as a prerequisite. Source-owned rules, setup, selected adapter and docs may be merged; preserve customizations, profile settings/consents, Daily history and original Calendar linkage, all Ledger cards/rows/IDs/order/metadata and schemas/views. Preserve Extra history and state except explicit approved migration. Don't overwrite same-named personal files or delete upstream-removed private content without specific approval. Review actual existing task prompts against current minimal templates, including all three Evening fallback questions; propose only necessary changes, separately approved, preserve title/times/timezone/paused state/notification preferences. Existing installations are **not** silently given a new task; offer new tasks separately with explicit task-activation approval. Never rerun setup.

### v0.5.20 Notion starter schema simplification

- New Notion installations use one Daily Companion Suite database containing exactly three data sources: System, Daily Companion and Action Ledger. Separate databases are not a new-setup fallback; guide the user to complete the same structure in Notion if needed, then verify before activation.
- Remove the legacy Google Drive URL field from the new Daily Companion schema and runtime requirements. Existing installations need no migration: preserve existing properties, historical links and working mappings, even if they have a different previously approved database layout. Never delete a private property or restructure live databases as part of an ordinary upgrade. Any such change requires a separate data-preserving proposal and approval.

### v0.5.19 Connector-first, simple version checks and upgrades

- Use GitHub connector first for both storage choices; a free GitHub account is sufficient for reading the canonical public repository when supported. No private GitHub repository is needed for Notion. Public web files remain an optional fallback; never require file uploads.
- For an existing installation, refresh the private upgrade rules and any Update Watch prompt hardcoding obsolete retrieval routes only under a specific approved change. Use VERSION alone for notifications; compare actual current file bodies for upgrades. Historical SHA verification is not needed. Preserve user customizations, private state, all schedules and permissions; no new task, schema migration or data rewrite. A selective rule/prompt repair alone does not stamp a full installed-template version.
- The v0.5.17 web-first route and v0.5.13 Pages-first route notes below are historical and superseded by connector-first reads. No automatic changes to existing private copies.

### v0.5.18 Evening task final-question repair

- The public Evening task template now explicitly requires three numbered capture questions at the very end of EVERY scheduled response, including a successfully verified Notion Auto-Saved full-body display. A generic invitation is insufficient; link, save status and other commentary precede the questions.
- On existing private installations, inspect the actual Evening task prompt. Where the questions appear only in a failure/fallback branch, propose a separately approved targeted task-prompt repair. Preserve task identity, conversation, time, timezone, enabled/paused state, notifications, historical Diary/Ledger content and private System customizations. Correct prompts need no change. This public release performs no private task or data migration.
- Verify a real subsequent Evening run; static checks do not establish client rendering.

### v0.5.17 Public web-only installation retrieval

- The new-user installation entry and selected-backend preflight now use public Pages bundle/individual documents, public GitHub HTML/Raw URLs, and independent public CDN endpoints. Remove user ZIP download/upload fallback and do not require a GitHub connector for Notion onboarding. Full source bodies and private installation consent are still mandatory: on total public browsing failure, retain answers and pause before writes.
- Existing private installations require no schema, profile, task, Daily, Ledger or migration changes. The source-route update applies only to newly read public setup or an explicitly approved private setup/upgrade-rule refresh. Public endpoints and CDN caches are not assumed coherent; selected source files must actually be read and checked for completeness. Automated tests cannot establish that ChatGPT's web browser can access these hosts in every account.

### v0.5.16 Plan / Action Ledger clarification

- Correct the public Notion setup wording: "Plan" refers to the existing Action Ledger task and project planning source; do not create a fourth Plan database for standard installation. New Notion installs retain exactly three data sources: System, one combined Daily Companion for Morning and Evening, and Action Ledger.
- No migration is required for correct existing three-source installations. Do not create, split, rename, delete or merge any private source automatically. If a user already has a distinct custom Plan database, preserve it and review its use only after a separately approved concrete proposal. Existing task state, notes, permissions, schemas/views, IDs and schedules remain unchanged.

### v0.5.14 Notion setup alignment

- New installs must use a single shared Daily Companion data source for Morning and Evening, single-select Category, and the Live-style fields/views. The 0.5.14 'separate Plan' description was an interpretation error corrected in 0.5.16: Plan here means Action Ledger, the separate task/planning source, not a fourth database.
- Existing private installations are not split, merged or retyped automatically. Inspect real mappings and preserve all Daily pages, Ledger cards/IDs, System revisions, saved views, history and scheduled task destinations. If an existing multi-select Category works with exactly one value per Daily record, preserve it until an explicitly approved data-preserving repair. No automatic Plan creation, new tasks or schema migration.

### v0.5.13 migration

- For an existing Update Watch, propose updating the private upgrade rules and any task prompt that hardcodes the old public URL to use Pages first. Preserve existing task identity, schedule, pause status, preferences, installed markers and all private data. No new task or schema/state migration. A selective route repair alone does not stamp a new installed template version; a full upgrade follows §1–3.

### v0.5.10 migration

- For existing Update Watch, propose replacing §0 in the private upgrade rules and any stale task prompt that requires CHANGELOG/SHA or routine failure alerts. Preserve other rules, installed markers, data, schedule, paused state and notification preferences. No schema or failure-counter migration; no new task. A selective watch-rule repair alone does not stamp a new installed template version; a full upgrade follows §1–3.

### v0.5.4 migration

- For an existing combined Evening + Extra task, propose splitting into two independent tasks under `setup.md`. Reuse the existing task for Evening at its prior Evening time and keep its conversation/history where supported; remove the Extra occurrence and create one separate Extra task at its original local time. Confirm capacity, task identities, times, timezone, notification preferences and explicit task-activation approval before changing either. If capacity is insufficient, seek an explicit choice of independent tasks; do not silently drop a feature or keep combining in new setup. Preserve pause status and preserve Extra state (pattern, enabled flag and feedback); never reset it, replay a missed date or enable a paused task. Avoid overlapping active occurrences, verify each deployed prompt/schedule/enabled state, and report pending steps or failures separately. Already separate correct tasks need no migration.

### v0.5.0 migration

- Profile v5 → v6 adds private `gmail_account_ids` and `calendar_account_ids` lists. For each previously approved service, confirm and verify the original account scope interactively using setup's read-only checks; add further accounts only with explicit permission. Declined services keep empty lists. Preserve existing Calendar exclusions, all history and settings. If account identity or access cannot be verified, report the gap and leave that scope unapplied until resolved or explicitly reduced; never broaden access by default. No task prompt or schedule change is required. Apply the new rules and profile together under §3.

### v0.4.1 migration

- New setup/notion.md and setup/github.md are onboarding only. Add selected file to mapped System if needed; update index, verify required runtime routes. No rewriting historical Daily pages. For Notion, inspect current schema and views; propose any needed Category select / numeric version changes (do not force-convert working customized multi-select categories) without losing existing values. Existing correct mappings may be retained explicitly. Resolve missing planning window interactively, never default null. Preserve existing approved capture source; if missing mapping, confirm exact locator and capture date field interactively, otherwise leave unconfigured.
- Already valid Notion 104-week anchor/pattern: preserve exactly; map old field names if required, retain enabled/feedback. No redraw, including on no-op.
- Legacy GitHub v6 (or older) cadence: disclose removal of scheduled writes, overdue catch-up and delivery claims; archive full prior state privately, including pending claims and reliable attempt history, without interpreting a claim as delivery. Obtain explicit approval to replace cadence with anchor_monday and weekday_pattern valid per engine; use first complete local week after migration, preserve enabled/feedback and custom rules. Remove obsolete scheduled authorization/claim fields only in approved migration. No silent replay or reset. Align new provisional anchor if migration crosses a week boundary. Suspend only previously enabled affected Extra with approval before coordinated engine/prompt change; if task inventory or required prompt change cannot be verified, stop before migration. No new tasks without separate approval.
- Earlier release migration notes: see the immutable v0.4.0 release's System/upgrade.md and CHANGELOG; historical instructions are context only, superseded by current read-only engine and write boundaries. For old Ledger schemas preserve data, reconcile Pending Admission/pending_close interactively and never invent closure dates. Optional reflection/weekly slots do not require rewriting history; retain notification guidance.

## 3. Apply approved changes

Obtain explicit approval of concrete diff, schema changes, task changes and any migration. Fresh-read affected private sources; if changed since preview, reconcile and obtain fresh approval. Before non-atomic writes that could leave active workflows inconsistent, suspend affected enabled tasks with approval; if required suspension is unavailable, leave upgrade unapplied. Notion snapshot each previous System body under Versions and verify, then patch, increment numeric version and verify. GitHub use fresh SHA for each approved file or verified atomic commit; preserve unrelated state, read back. Stop on any access, safety, conflict or verification failure; report partial results and leave installed markers unchanged until other changes verified. No bypass or broad rollback. A repair/rollback needs a new concrete proposal preserving intervening edits.

Once rules, mappings, chosen schema, state and authorized task prompts are verified for a full approved upgrade, update installed_template_version to the verified candidate semver if known, otherwise record null (unknown) and explain that content was updated but its release number could not be established. installed_template_commit is optional: record a reliable commit identifier only if already available for the applied source, otherwise null; never require its lookup. For GitHub update private VERSION when the new semver is known; otherwise leave the existing VERSION file unchanged and explain it may be stale. Read back the markers and any changed label. A selective rule repair alone must not stamp a full installed-template version. Missing metadata alone is not a failed upgrade. If a label/marker write fails, report partial, leave suspended tasks suspended and retry only pending state. Keep setup status separate. Resume only previously enabled tasks suspended for approved upgrade after verification; never enable user-paused or absent tasks. Actual scheduled persistence and notifications require observed runs, not static checks or interactive access. Report per-task configuration/activation/observed status separately.

No approval/no changes means no writes. If access is unavailable, prepare a reviewable proposal and report what remains unapplied.
