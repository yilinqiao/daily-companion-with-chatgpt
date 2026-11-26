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

### v0.5.33 Default private Notion Suite creation

- Fresh Notion setup creates the private workspace-level Suite after installation approval without asking for an existing parent page. Resume incomplete setup with confirmed answers and any verified existing Suite; no duplicate creation, relocation or change to private permissions without approval. No migration, schema or task changes for existing installations.

### v0.5.31 Retire optional saved-page capture source and PARA

- New installations omit `capture_source`; Evening no longer reads that separate source or generates its dedicated Saved Today section. The five Diary-first sections and the three evening questions remain; user-shared links can still be included naturally.
- For existing installations, apply the updated setup, workflow, artifact/rules and adapter guidance together under the normal approved upgrade. Legacy `capture_source` values and any related source labels are inert; do not access them or require reauthorization. Preserve private profile values, historical Daily records and external collections; removal of legacy configuration or external data requires separate approval. Preserve meaningful user-approved legacy saved-page links if revising a Memory. No required data migration or Scheduled Task changes.
- Morning and Evening no longer retrieve PARA or separate long-term project notes as a routine source. New public template copies omit the empty Projects, Area and Archives directories; System, Daily, Action Ledger tasks/projects and the Resources installation guide remain. Existing private folders, databases, notes and customizations are preserved; never delete or relocate private content during upgrade. Daily history and approved conversation context remain available under their existing rules.

### v0.5.30 Five-stage onboarding

- For new or incomplete setups, follow About You → Your Data Sources → Your Storage → Your Daily Routine → Review & Launch. Preserve confirmed answers and verified connections; finish only pending checks in their corresponding stages. The former optional saved-page source is retired from v0.5.31. Use compact stage progress when supported.
- No migration, task changes or rerun for completed installations. The same independent installation and activation approvals, write boundaries and state preservation apply.

### v0.5.28 Full-resolution cover and database icons

- New Notion setups use the original 2172 × 724 PNG artwork, without recompression, via a stable public URL. The legacy WebP URL remains available for existing installations; do not replace their custom covers automatically.
- New databases use the optional native icons (⚙️/📖/📋) through a single targeted parent-page update of exact database tags when the connector supports it, retaining identities, schema, views and titles. No additional verification, retry loop or readiness requirement. Live test confirmed page cover URL and icon rendering, a database icon, and a combined update of two additional database icons; the full-resolution cover rendering should be checked in the client. No migration or bulk restyling.

### v0.5.27 Notion visual defaults

- New Notion setups apply the public sunrise-lake Cover and native icons where supported, within existing creation calls. No new onboarding question or readiness gate; skip unsupported or failed decorative fields without additional verification or duplicate writes. New Morning/Evening pages use ☀️/🌙 respectively in their existing authorized create operation.
- Existing installations retain all custom appearance, title/ID mappings, state, history, schedules and consent. No migration or bulk restyling. After an approved rule upgrade, newly created Daily pages can use the defaults; any restyling of existing pages is a separate user-approved cosmetic operation. GitHub storage unchanged.

### v0.5.25 Notion setup efficiency

- New or paused Notion onboarding uses one supported batch create-pages call for missing System pages, and reuses confirmed operation results rather than requiring repeated per-page full-body comparisons. Read back essential configuration and resolve any uncertain or failed operations; reconcile partial batches before retrying missing pages only. Continue an incomplete installation without repeating approved successful work.
- No migration or task changes for completed installations. This is a setup-only optimization, not a relaxation of normal runtime saves or approved private upgrade read-back and conflict protections.

### v0.5.24 Notion System display titles

- New Notion System page titles use the full canonical logical path without its final `.md` suffix to avoid misleading automatic links. GitHub filenames and the System index's canonical paths (including `.md`) remain unchanged. Both existing and new title formats resolve through the verified index/page IDs.
- For an existing or partially installed Notion suite, offer a scoped title-only cleanup as part of the approved setup/upgrade or on explicit request. Identify pages by verified index/page IDs, check for conflicting titles, rename the same pages in place and verify titles, unchanged IDs, bodies, index mappings and task destinations. Do not create replacement pages or change canonical paths, links, personal data, page revision numbers or scheduled task prompts for a title-only change. Preserve custom titles unless explicitly approved. A declined or unavailable cleanup is not an upgrade blocker for completed installations. No required data/schema migration; a title-only cleanup does not stamp a full installed version.

### v0.5.22 Three independent Notion databases

- New Notion installations create a private Daily Companion Suite parent page with exactly three independent child databases (System, Daily Companion, Action Ledger), each with its own source. No add-data-source operation or manual multi-source construction is required. This supersedes the single-database installation rule in v0.5.20.
- For paused, incomplete onboarding, retain confirmed answers and verified connections, refresh the current setup guide and proposed structure, reuse unambiguous compatible partial objects if present, and obtain approval for the updated installation plan. Never duplicate or silently delete partial data.
- Existing completed installations keep their working layouts (including a single database with three sources), IDs, properties, views, personal state, permissions and tasks. No schema or data migration and no compulsory restructure. The notion_suite_id refers to the actual configured parent page or legacy suite; query by verified source IDs. Any relocation requires a separate approved proposal. Legacy Drive URL stays absent from new installs.

### v0.5.21 Notion scheduled retry and recovery

- Refresh the Notion storage adapter and shared instructions. Compare existing Morning/Evening task prompts with setup.md; propose a separately approved, targeted bootstrap retry addition only if absent. Preserve task identity, schedules, timezone, enabled/paused states, preferences, consent and all private history. No schema/state migration, new tasks, auto-backfill or GitHub scheduled write changes.
- Verify the installed policy and any approved prompt updates by readback. Real transient-failure recovery remains unverified until observed in a scheduled run. A selective repair does not stamp a full installed version.

### v0.5.20 Notion starter schema simplification

- Historical v0.5.20 layout (superseded for new installations by v0.5.22): one Daily Companion Suite database containing exactly three data sources: System, Daily Companion and Action Ledger. Preserve this layout for existing completed installations; do not require it for new setups.
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

- New setup/notion.md and setup/github.md are onboarding only. Add selected file to mapped System if needed; update index, verify required runtime routes. No rewriting historical Daily pages. For Notion, inspect current schema and views; propose any needed Category select / numeric version changes (do not force-convert working customized multi-select categories) without losing existing values. Existing correct mappings may be retained explicitly. Resolve missing planning window interactively, never default null. The historical capture mapping requirement is superseded by v0.5.31; preserve legacy private values but do not use them.
- Already valid Notion 104-week anchor/pattern: preserve exactly; map old field names if required, retain enabled/feedback. No redraw, including on no-op.
- Legacy GitHub v6 (or older) cadence: disclose removal of scheduled writes, overdue catch-up and delivery claims; archive full prior state privately, including pending claims and reliable attempt history, without interpreting a claim as delivery. Obtain explicit approval to replace cadence with anchor_monday and weekday_pattern valid per engine; use first complete local week after migration, preserve enabled/feedback and custom rules. Remove obsolete scheduled authorization/claim fields only in approved migration. No silent replay or reset. Align new provisional anchor if migration crosses a week boundary. Suspend only previously enabled affected Extra with approval before coordinated engine/prompt change; if task inventory or required prompt change cannot be verified, stop before migration. No new tasks without separate approval.
- Earlier release migration notes: see the immutable v0.4.0 release's System/upgrade.md and CHANGELOG; historical instructions are context only, superseded by current read-only engine and write boundaries. For old Ledger schemas preserve data, reconcile Pending Admission/pending_close interactively and never invent closure dates. Optional reflection/weekly slots do not require rewriting history; retain notification guidance.

## 3. Apply approved changes

Obtain explicit approval of concrete diff, schema changes, task changes and any migration. Fresh-read affected private sources; if changed since preview, reconcile and obtain fresh approval. Before non-atomic writes that could leave active workflows inconsistent, suspend affected enabled tasks with approval; if required suspension is unavailable, leave upgrade unapplied. Notion snapshot each previous System body under Versions and verify, then patch, increment numeric version and verify. GitHub use fresh SHA for each approved file or verified atomic commit; preserve unrelated state, read back. Stop on any access, safety, conflict or verification failure; report partial results and leave installed markers unchanged until other changes verified. No bypass or broad rollback. A repair/rollback needs a new concrete proposal preserving intervening edits.

Once rules, mappings, chosen schema, state and authorized task prompts are verified for a full approved upgrade, update installed_template_version to the verified candidate semver if known, otherwise record null (unknown) and explain that content was updated but its release number could not be established. installed_template_commit is optional: record a reliable commit identifier only if already available for the applied source, otherwise null; never require its lookup. For GitHub update private VERSION when the new semver is known; otherwise leave the existing VERSION file unchanged and explain it may be stale. Read back the markers and any changed label. A selective rule repair alone must not stamp a full installed-template version. Missing metadata alone is not a failed upgrade. If a label/marker write fails, report partial, leave suspended tasks suspended and retry only pending state. Keep setup status separate. Resume only previously enabled tasks suspended for approved upgrade after verification; never enable user-paused or absent tasks. Actual scheduled persistence and notifications require observed runs, not static checks or interactive access. Report per-task configuration/activation/observed status separately.

No approval/no changes means no writes. If access is unavailable, prepare a reviewable proposal and report what remains unapplied.
