# Changelog

## 0.5.31 — 2026-11-26

- Retire the optional saved-page capture source from new onboarding, profile, Evening retrieval and both storage adapters. Remove the dedicated Saved Today / Slurped Pages slot from new Daily Memories; retain five Diary-first sections, the three evening questions and user-shared links within ordinary content.
- Align setup guides, runtime policies, upgrade, BC-01/09 and static regressions. Existing private capture settings are ignored by upgraded rules, not deleted; preserve historical Daily records and external collections. No required data migration, new source permission or Scheduled Task changes.
- BC-01/09 scenario review: both backends skip the retired source, including legacy configured profiles; no additional setup question or source reads; user-provided links and meaningful links in revised legacy Memories remain preserved. Fresh-account and scheduled client execution remain unverified.


## 0.5.30 — 2026-11-26

- Reorder new setup into About You, Your Data Sources, Your Storage, Your Daily Routine, Review & Launch. Finish Calendar (including exclusions), Gmail and other optional sources in their own topics; then finish storage account/destination selection and scoped checks before schedules. Preserve the existing optional capture source only when requested; no new mandatory question or database.
- Add a compact current-stage header and thin five-segment progress bar to the Intelligent UI preference, initial prompts and user guides. One question per turn; progress represents stage position, not successful completion. Preserve separate installation and activation approvals; no assistant installation writes during preflight.
- Align setup, README, guides, upgrade, BC-01 and regressions. No migration, private state, schema or task changes. BC-01/02/03 review: both backends, declined/failed optional sources, resume and missing source bodies retain existing safety boundaries; no repeated successful checks or reopened confirmed choices. Actual fresh-account UI and connector execution remain unverified.


## 0.5.29 — 2026-11-26

- Prefer ChatGPT's native Intelligent UI throughout onboarding whenever useful, including interactive choices, time selectors and confirmation controls. Keep the fixed questionnaire, one question per turn and separate installation/task approvals unchanged. UI availability is not a prerequisite.
- Align the initial prompt in README, setup and HTML guide, the onboarding rule, getting-started documentation, BC-01 and a static regression sentinel. Both storage choices use the same onboarding rule; no migration, private state, permission or scheduled task changes.
- BC-01 scenario review: fixed question order and approval boundaries remain unchanged for Notion and GitHub; where interactive UI is unavailable ordinary questions still work. Static regression checks do not prove actual UI rendering or selection handling in a new client; live onboarding remains unverified.


## 0.5.28 — 2026-11-26

- Publish the original 2172 × 724 PNG sunrise-lake cover without recompression. New Notion setups use the PNG URL; keep the old WebP for existing covers. Allowlist both exact assets and mirror them in Pages; no other binary file types are allowed.
- Use normal database creation and, when supported, one combined targeted parent-page Markdown update for the three new database icons. Preserve all existing custom appearance, database/source identities, titles, schemas and views. No extra onboarding question, readiness gate, decoration verification or retries. No migration, private state or task changes.
- BC-03 scenario review: real Notion test confirmed external cover and native page icon rendered in the client, a native database icon persisted, and two additional database icon changes succeeded in one call. New full-resolution PNG bytes match the original; client rendering of the PNG is checked separately. Static tests cover asset publication and rule consistency, not other accounts' tool availability.


## 0.5.27 — 2026-11-26

- Add the approved AI-generated sunrise-lake artwork as a 1500 × 500 optimized WebP public asset. New Notion Suite parent pages use 🌿 and the public Cover, System/Daily/Action Ledger database icons are ⚙️/📖/📋 where native fields exist, System pages use 📄 (Profile 👤, Index 🗂️), and new Morning/Evening pages use ☀️/🌙.
- Apply optional decoration within existing approved create operations, including batch creation. No extra onboarding question, repeated verification, readiness gate, schema changes or duplicate retries. Preserve existing custom appearance, titles, IDs, history and schedules; no migration or bulk restyling. GitHub storage unchanged.
- Update setup, Notion adapter, upgrade, docs, BC-03/11, and regression checks; explicitly allowlist only the approved public binary cover and mirror it in Pages. Static tests verify the asset and defaults; actual Notion cover rendering and database icon support remain unverified.


## 0.5.26 — 2026-11-26

- Add an optional ChatGPT mobile app suggestion to the final notification handoff for both storage choices: install the official iOS or Android app if desired, sign in to the same account, and allow mobile notifications according to preference. Skip if already installed or the user prefers web/email. No additional onboarding question, setup gate, or requirement for task activation.
- Align setup, README, getting-started/HTML guide, BC-01 and notification regression tests. Existing notification preferences and scheduled tasks remain unchanged; no private migration, schema or permission changes. Actual notification delivery remains subject to first-run and device verification.


## 0.5.25 — 2026-11-26

- Notion setup only: create all missing System pages with full approved bodies in one supported native batch create-pages call, reusing returned page IDs for the index. Use smaller calls only when the actual tool cannot accept the batch. Reconcile partial/ambiguous results before retrying missing items.
- Reduce repeated verification: reuse successful creation/configuration results, avoid routine full-body read-back of every confirmed System page, and check essential Profile/Index/runtime readability, final setup status and unresolved evidence. Do not claim an independent full-body comparison from creation receipts. Preserve completed work across tool limits.
- Align setup, Notion onboarding, user-facing guides, upgrade guidance and BC-03 regression checks. No schema, permissions, task prompts, runtime verification, GitHub backend or version-check changes. No migration for completed installations. Actual batch payload support and new-account installation remain to be verified; CI cannot prove live connector behavior.


## 0.5.24 — 2026-11-26

- Remove the final .md suffix from newly created Notion System page display titles, preserving directory prefixes (for example, System/workflows/morning). Keep GitHub filenames and canonical .md paths in the System index unchanged, resolving by exact page IDs. This avoids misleading automatically linked titles.
- Preserve existing installations and support explicitly approved in-place title-only cleanup without changing bodies, IDs, index keys, revision numbers, scheduled tasks or personal data. No compulsory migration, new schema or additional version-check gate.
- Align setup, Notion storage, upgrade, BC-03 and regression tests. No change to the three-database layout or GitHub-first access. Actual Notion client rendering and scheduled execution remain to be verified.


## 0.5.23 — 2026-11-26

- Proactively remind Notion users before the first connector call and again before approved writes if needed (including resumed onboarding) to select Always allow, usually the leftmost option, rather than Allow once when the permission popup appears, if offered and they agree to ongoing access. Keep tool permission distinct from explicit installation, initial auto-save and scheduled-task consent; respect user choice. Do not wait for a blocked tool call to show the reminder.
- Align setup, Notion onboarding, README, getting-started/HTML guide, BC-03 and regression checks. No change to database layout, private state, task prompts, permissions already granted or upgrade migrations. Actual client permission UI and persistence remain to be observed.


## 0.5.22 — 2026-11-26

- Change new Notion installations to one private Daily Companion Suite parent page containing three independent databases (System, Daily Companion, Action Ledger). A fresh-account preflight reported the connector could create databases and views but did not expose adding sources to an existing database. Normal database creation now replaces the multi-source requirement; no manual multi-source construction. Morning and Evening still share one Daily database, no separate Plan database, no legacy Drive field.
- Preserve existing completed single-database or separate-database installations and configured IDs, views, history and tasks. No schema/data migration or new task. Paused onboarding can resume using retained answers and the updated approved plan. Explicitly distinguish database and source IDs in the index and keep runtime resolution based on verified private mappings.
- Align setup, Notion adapter, upgrade, README, getting-started/HTML guide, BC-03 and regression checks. Correct the generic setup date identity to the user's configured local timezone. GitHub-first reads, simple version checks, permissions, daily workflows and v0.5.21 retry rules remain unchanged. Static checks do not establish live database creation, query quota availability or scheduled persistence; verify a fresh-account install.


## 0.5.21 — 2026-11-24

- Add bounded Notion read retries (two after the first attempt), initial System-fetch retry in both new task prompts, and safe exact-identity reconciliation before at most one conclusively uncommitted write retry. Report failed stage, available error, attempts and verified/failed/unverified persistence; preserve the full draft and Evening's mandatory three questions.
- Affected rules: storage/notion, instructions, setup, upgrade and behavioral contracts. BC-08/10/11/13/17 scenario review preserves complete body, separate approval, no duplicate or overwrite, Calendar identity and independent scheduled tasks. GitHub scheduled writes remain forbidden; Extra and Update Watch unchanged. No private schema/state migration, consent changes or automatic backfill. Existing task prompts may need separately approved targeted repair.
- Static contract review only; actual scheduled connector faults and recovery require observation. Release CI validates the candidate separately.

## 0.5.20 — 2026-11-24

- Simplify new Notion setup: one Daily Companion Suite database containing exactly three data sources (System, shared Daily Companion, Action Ledger). Remove the alternative separate-database setup. If multi-source creation is unavailable, guide manual completion of the same structure and verify it before marking ready or activating tasks.
- Remove Legacy Drive URL from the new Daily Companion schema and current runtime field requirements. Preserve existing private properties, historical links, database layouts and mappings; no automatic deletion or schema migration. No changes to GitHub private setup, daily workflows, task schedules or version-check requirements.
- Align setup, Notion storage adapter, upgrade, README, Getting Started, HTML setup guide, BC-03 and regression assertions. Static checks cover the new structure and field removal; actual new-account multi-data-source creation and verification still need a live test.


## 0.5.19 — 2026-11-24

- Make the GitHub connector the default public-source read path for both Notion and GitHub onboarding, update checks and interactive upgrades. Guide free GitHub signup (Google if available) and connection before reading Setup; Notion users need no private repository. Read exact current default-branch files directly, reuse complete bodies and keep public GitHub/Raw/Pages as simple fallbacks. No manual file uploads.
- Simplify version handling: Watch and interactive check compare installed version to public VERSION alone; CHANGELOG is optional. Manual upgrades compare actual latest public and existing private file bodies, with no mandatory immutable candidate or baseline SHA, tags, history, manifest, three-way merge or repeated version verification. Unknown metadata does not block reviewed rule changes; installed version/optional commit recorded only if known. Preserve known downgrade/incompatibility checks, independent approvals, actual read completeness and private conflict-safe write/read-back protections.
- Update Setup/task template, upgrade, README, getting-started/HTML/Obsidian guides, privacy and BC-01/14/15 with regression tests. No private schema, history, profile state, task identity/cadence or permission changes; selective repairs require user approval and do not stamp a full installation version. Older Pages-first notes are historical. New-account connector access and actual scheduled read/notification behavior still require live observation; CI is not proof of those capabilities.


## 0.5.18 — 2026-11-23

- Fix a live-observed Evening omission: the complete provisional Notion Memory appeared, but the three standard capture questions did not. The setup-created Scheduled Task prompt now explicitly demands all three numbered questions at the end after **successful** autosave as well as failed/blocked runs, with no generic-invitation substitute.
- Strengthen Evening workflow, BC-08, regression tests and private-upgrade guidance; affected files: setup, evening, upgrade, behavioral contracts, test_evening_handoff, VERSION and CHANGELOG. No changes to data models, user permissions, private notes, status, Ledger, backend write boundaries or task cadence.
- Existing private tasks require a separately approved prompt repair only if their current prompt can omit the questions on the success path. No automatic task or data migration. BC-08/09/10/13 review: full initial Notion body and question handoff on success/failure; approval of revisions/Ledger remains independent; GitHub scheduled writes remain forbidden and Extra independent. Static/CI checks cannot guarantee actual model output, so verify a real scheduled occurrence.

## 0.5.17 — 2026-11-23

- Remove the new-user ZIP download/upload fallback: ChatGPT must fetch complete Setup and selected Notion/GitHub installation rules directly over public web routes. Try the GitHub Pages Setup and bundle/individual HTML/MD files, then public GitHub Raw/HTML and independently served jsDelivr CDN; an existing GitHub connector is optional, not a prerequisite. Explicitly keep confirmed onboarding answers and stop before private writes if every public source is blocked/truncated.
- Update the copy-paste prompt in README, Setup and HTML setup guide, the Getting Started guide, BC-01, upgrade retrieval fallback and regression tests. User should never have to download/upload repository files for onboarding or interactive template upgrade.
- No changes to private storage schemas, Daily/Memory/Action Ledger behavior, approval gates, scheduled times or user's Live Notion. BC-01/03/14 reviewed: source completeness and consent still gate writes; users are not asked to manually replace inaccessible source text. GitHub CI verifies rules, not a live ChatGPT browser; public website access remains browser/provider-dependent and is not guaranteed for every new account.


## 0.5.16 — 2026-11-23

- Clarify the intended Notion terminology: **Plan means Action Ledger**, the existing task/project planning source, not an optional fourth database. A standard private Daily Companion Suite has just three data sources: System, combined Daily Companion (Morning + Evening) and Action Ledger. Scheduled Ledger writes remain prohibited.
- Correct the public Notion setup, common setup, user guides, behavioral contract, upgrade guidance and regression assertions. No change to Live Notion, private profiles, schemas, views, notes, task state, approvals, schedules or GitHub alternative. Existing proper three-source private installations need no migration; never delete a separate custom source someone already created automatically.
- BC-01/03/11/12 reviewed: setup requires verified source mappings, one Daily date+Category identity and independent Ledger approval. CI checks are static; live new-account installation and scheduled persistence are not claimed.


## 0.5.15 — 2026-11-23

- Improve GitHub Pages deployment reliability by allowing artifact metadata indexing to settle between a successful upload and the deploy-pages API lookup. A short indexing race caused initial 0.5.14 Pages deployment failure; re-running the same job created duplicate named artifacts in the same run and was not a viable repair. A fresh release run is required.
- Deployment workflow, VERSION and CHANGELOG only. The 0.5.14 Notion shared-Daily-source onboarding instructions remain unchanged. No private data/schema/task or user migration; a scheduled run or real-account setup still needs independent observation. Standard CI is used to verify the complete release.


## 0.5.14 — 2026-11-23

- Align new Notion onboarding with the observed Live Suite: System, one combined Daily Companion source for both Morning Briefing and Evening Memory (Category single-select), and separate Action Ledger. Correct the live Daily properties, source naming and saved views, plus Ledger baseline fields. Plan is an optional separate private database requiring its own approval, not a Daily category or scheduled destination.
- Update Notion setup/adapter, shared setup, README/guides, behavioral contracts, upgrade notes and regression tests. No new mandatory profile fields, private writes, historical rewrites, automatic new Plan database, schema migration or task changes. Existing private sources with working custom types remain intact until explicitly approved repair.
- BC-01/03/11/12 reviewed: date + Category unique identity, paginated unfiltered searches, scoped Daily writes and independently approved Ledger updates preserved. Live Suite schema inspected, but no private identifiers or data copied into public release; CI cannot prove actual new-client setup or scheduled persistence.


## 0.5.13 — 2026-11-22

- Make the validated public GitHub Pages mirror the default reading route for Setup, required installation files, Update Watch, release notes and interactive upgrade guidance. Retain GitHub page/Raw/connector and applicable public ZIP fallbacks. GitHub remains canonical source and history; automatic deployment is unchanged.
- Align README, setup, upgrade, both getting-started guides, Obsidian guide, BC-01/14 and static regression checks. Existing private copies require an approved upgrade or selective watch-rule/prompt repair; preserve all state, permissions, task times and pause status. No schema or data migration; no new task or automatic private upgrade.
- BC-01/14/15 review: successful Pages reads allow onboarding/watch without GitHub connector; unavailable/incomplete content uses fallbacks and existing stop/approval gates; optional notes and missing watch SHA do not block valid version alerts. Interactive candidate bodies must match version/source commit, with pinned-source fallback if inconsistent, and existing baseline verification remains mandatory when known. Prior fresh-account version/setup reads, automatic deployment and a one-time scheduled version read succeeded on 0.5.12; full private installation/upgrade and ongoing Watch notifications from the new route remain unverified.

## 0.5.12 — 2026-11-22

- Notion Evening now displays the same complete provisional Daily Memory body as the verified auto-saved page in ordinary chat, then status/link and all three capture questions. No separate recap or editable approval preview until answers; on save failure/denial show the full safe draft with honest status.
- Align Evening workflow, Notion adapter, artifact policy, BC-08, README, getting-started and regression checks. No schema, state, permission, schedule or task changes; no data migration. Existing private copies need a separately approved rules upgrade. GitHub backend remains interactive-only for saves.
- BC-08/09/10 review: full initial body and section order, failure/denied save, three-question handoff, no duplicate writes, and separately approved same-page revision/Ledger delta. Static checks do not establish actual scheduled rendering or connector behavior; verify the next real occurrence.

## 0.5.11 — 2026-11-22

- Add an experimental GitHub Pages mirror generated from a validated public `main` checkout: version, setup, changelog, upgrade, complete System bundle and individual exact Markdown/HTML files. An explicit allowlist excludes Daily, Archives, personal configuration and repository metadata. GitHub retains canonical source and historical versions.
- Add the mirror builder, regression tests, README and automatic deployment job. Repository Pages must first use GitHub Actions as its source. No changes to default Setup/Update Watch routes, private state, schemas, schedules or upgrade verification; no private migration required.
- BC-01/14/15 review: mirror is read-only; existing completeness and approval boundaries remain unchanged. Static build verifies source parity and excluded paths; actual public deployment and fresh-account/scheduled retrieval remain to be tested before changing the default routes.

## 0.5.10 — 2026-11-22

- Simplify scheduled Update Watch to compare the installed version with the canonical public VERSION; try Raw, GitHub page and available connector. CHANGELOG is optional and no SHA is required to notify. Equal/older versions and public read failures are silent; alert once only if three consecutive daily failures can be verified from available history. No persistent counters, scheduled writes or automatic upgrade. Interactive upgrade verification and approval remain unchanged.
- Align upgrade, setup task entrypoint, README, getting-started guides, BC-14 and static regression sentinels. Existing installations need an approved private watch-rule/prompt repair or upgrade; no schema, schedule, data or profile-marker migration for a selective repair.
- BC-14/15 review: a missing changelog or installed SHA does not block a known newer-version alert; unknown installed version never implies a new release; malformed/unreadable public VERSION retries, and unavailable run history does not fabricate a streak. Both backends remain read-only; immutable candidate and approved diff still required for actual upgrades. Static checks do not establish live task history visibility, public retrieval or notification delivery.

## 0.5.9 — 2026-11-22

- Require `This Week` in every Sunday Morning Briefing, with all six preceding Monday–Saturday dates accounted for, available saved Memory bodies read, and confirmed, provisional and missing/inaccessible coverage distinguished. Even zero readable Memories requires an honest gap statement. The personal observation remains optional and weekdays omit both weekly slots.
- Align Morning, artifact schema, BC-16 and static regressions for Notion and GitHub. No schema, task prompt, schedule, authorization or private state migration; no historical Briefing rewrite.
- BC-16 review: complete, partial and empty/inaccessible weeks require a recap; unsupported observations are omitted, provisional records do not prove completion, and ordinary weekday output and backend-specific save permissions remain unchanged. Static validation does not establish actual scheduled execution.

## 0.5.8 — 2026-11-20

- Recommend High thinking at the start of onboarding, if available. When direct public file retrieval fails, guide the user to download and upload the canonical public repository ZIP and read required files from it. Answer user-initiated questions and resume the pending setup stage, preserving confirmed answers.
- In Notion onboarding, recommend Always allow if the tool permission prompt offers it and the user consents; installation, auto-save and task activation approvals remain independent. Align setup, Notion guide, README, getting-started guides, BC-01/03 and static regressions.
- No schema, runtime workflow, task prompt, metadata requirement or private state migration. BC-01/03 review: ZIP fallback preserves completeness and source safety; missing files still block installation, user questions do not imply approval, and one-time/declined tool permissions remain respected. These are onboarding instructions; UI availability and actual connector execution require client verification.

## 0.5.7 — 2026-11-20

- Try the canonical Raw URL or available GitHub connector when a public file page cannot be read. Load all required selected-backend installation files and verify access before asking for installation approval; after approval, reuse verified contents, proceed directly and retain approval for the unchanged plan if source retrieval is interrupted.
- Align `System/setup.md`, README, both getting-started guides, BC-01 and regression sentinels. No new metadata checks, schema/runtime/task changes or private state migration; completed installations need not rerun setup.
- BC-01/03 review: incomplete source still stops writes, fallback success preserves confirmed answers, approval follows complete preflight for both backends, and unchanged approved initialization does not repeat source reads or approval. Private read-back and separate task activation remain mandatory; live client retrieval and connector behavior require a real account test.

## 0.5.6 — 2026-11-20

- Simplify onboarding to one complete canonical setup file and the original closed questionnaire. Version checks are not required; installation checks actual required source content, scoped access, explicit approval and read-back. Missing or inconsistent version metadata alone never blocks readiness; record reliably attributable installed markers or leave them null.
- Align setup, both installation guides, README and both getting-started guides; clarify unknown-baseline handling in upgrade/watch, update BC-01/14 and regression sentinels. Strict immutable upgrade candidate verification and publication CI remain unchanged. No schema, runtime workflow, task prompt or private state migration; existing installations need not rerun setup.
- BC-01/03/14/15 review: missing setup text stops questions; stale/missing metadata alone permits both installs after actual file/permission/approval checks; missing/conflicting required content or failed read-back stops; unknown version does not justify a newer-release claim or automatic upgrade. Static checks cover contracts, not actual client onboarding or scheduled execution.

## 0.5.5 — 2026-11-20

- Stage source verification: complete current setup and consistent version metadata are enough for the closed, conversation-only questionnaire if only the commit SHA is unavailable. Require a verified immutable release before connector preflight or private installation writes; retain confirmed answers and revalidate changed questions on resume. Missing or inconsistent setup/version still blocks onboarding. Task activation and upgrade verification remain strict.
- Align `System/setup.md`, README, both getting-started guides, BC-01 and static regressions. No runtime, schema, schedule, task prompt or private state migration; completed installations need not rerun onboarding.
- BC-01/03/14/15 review: consistent source without SHA permits questions but neither backend can install; missing/conflicting setup or metadata stops; restored verification reuses valid answers, then normal permission and approval checks apply. Existing private upgrades retain immutable candidate/baseline checks. Static release and regression checks cover explicit contracts; live ChatGPT onboarding and connector/task execution require separate observation.

## 0.5.4 — 2026-11-18

- Require independent Evening and Extra Scheduled Tasks, removing the optional combined occurrence router. If task capacity is limited, explicitly choose and report partial activation. Evening with an uncertain target date still reports the issue and asks all three capture questions, without writes; Extra retains its independent read-only engine.
- Update setup, upgrade and BC-13 plus static regression coverage. For existing combined tasks, propose an explicitly approved split preserving local times, pause status, notification preferences, history and Extra cadence/feedback; already separate tasks need no migration. No schema or data migration; both storage adapters and approval boundaries are unchanged.
- Regression review: BC-08 and BC-13 cover date/connector failure, independent workflow identity, task limits and legacy split approval; local privacy/structure, release-version and static regression checks are required. Actual scheduled activation, output, notifications and connector persistence remain client validation.

## 0.5.3 — 2026-11-18

- Restore bounded Calendar recovery on incomplete coverage/unsolved candidates (even after Auto-Saved Memory), reconcile all examined dates, and preserve independent financial recovery. Restore explicit Notion runtime field mapping and optional protected Calendar account provenance (old two-ID records remain valid).
- Keep all three Evening questions when auto-save fails; defer preview, preserve diary voice, fresh-read Ledger after answers and private rules/consent before interactive writes. Distinguish Extra no-op silence from actionable failure, and clarify combined-task notification trade-off.
- Tighten pinned setup and upgrade integrity, semver/SHA markers and partial-failure task suspension. No mandatory schema or state migration; private installs may adopt updated instructions and prompts through approved upgrade, preserving existing data.
- Add maintenance-only behavioral contracts (BC-01–16), release review and static regression sentinels. Independent rule walkthrough of BC-04/05/07–15 identified and resolved the older-date recovery gap and paused Extra precedence; unchanged onboarding/planning, dedupe and weekly/flavour contracts remain covered by existing regressions. Actual onboarding, scheduled access and approval behavior remain unverified in a live client.

## 0.5.2 — 2026-11-18

- Enforce a closed onboarding questionnaire, verify and identify the public release before asking questions, and resume from valid confirmed answers without invented preferences. Align startup prompts across setup, README and HTML; update the getting-started guide.
- Reword the daily planning window as the full day to plan (e.g. 07:00–21:00, including work); keep the existing start/end fields, explicit confirmation, occupancy rules and opt-out. No runtime, schema, schedule or private migration required. Static regression checks cover the prompt contract; actual ChatGPT onboarding behavior requires interactive testing.

## 0.5.1 — 2026-11-18

- Offer Google-account Notion signup at the storage-choice question; guide new Notion users through their own signup before connection and scoped permission verification. GitHub remains optional.
- Update setup, Notion onboarding, README and both getting-started guides. No runtime, schema, schedule or private migration required; signup and connector access are confirmed by the user. Static release and regression checks cover the onboarding contract.

## 0.5.0 — 2026-11-18

- Support one or multiple explicitly approved Gmail and Google Calendar accounts through the same Morning/Evening workflows. Verify each account, combine and deduplicate results, retain source identity, and report partial coverage without falling back to an unapproved account.
- Setup, profile (v6), shared rules, Morning/Evening source routing, upgrade guidance, README and getting-started guide updated. Private upgrades confirm existing account scope before enabling multi-account reads; preserve all Calendar exclusions, notes, Ledger and other settings. No task, schedule, storage or approval-flow change. Public account fields remain empty; new static privacy checks reject populated or missing fields.
- Static release and regression checks validate template consistency and blank account state. Actual multi-account access, identity routing and scheduled reads must be verified in the user's client; no private installation is automatically changed.

## 0.4.2 — 2026-11-18

- Document the optional direct-edit tip for editable Markdown previews in `docs/GETTING_STARTED.md`. Clarify in `System/policies/artifacts.md` that only the final user-approved edited content may be saved; request a revised preview and approval if edits are inaccessible.
- No new mandatory preview, approval-flow, schema, state, permission or task change; no private migration required. Direct editing and access to edited text depend on the ChatGPT client. Static release and regression checks verify repository contracts, not client editing behavior.

## 0.4.1 — 2026-11-17

- Reduce runtime dependencies: separate Notion/GitHub onboarding from adapters, move Kanban representation into GitHub adapter, consolidate shared artifact and approval rules, shorten upgrade and workflow instructions.
- Morning retrieves missing saved Memory dates (including Auto-Saved as a retrieval checkpoint, never confirmation); Evening accepts a saved Morning baseline. Retain independent financial look-back, Ledger reconciliation and all three fallback capture questions.
- Use six Diary-first sections without duplicate completion/exploration slots. Notion queries paginated saved views, verifies exact date/category, preserves Calendar ID, uses fresh Ledger schema/options and numeric System revisions with snapshots. Capture dates use backend-specific reliable metadata.
- Both backends use one read-only 104-week Surprise pattern; no scheduled claims, catch-up, or state updates. Legacy date/claim state is preserved privately and migrated only with explicit approval; existing valid patterns are retained. Historical records and personal configuration remain unchanged.
- Updated setup, selected storage adapters, shared policies/workflows, Extra, upgrade, README, release review and static regression/privacy checks. No private installation or tasks are changed by this release. Static tests verify contracts, not actual scheduled connector execution.

## 0.4.0 — 2026-11-17

- Notion-first setup with private System/Daily/Ledger data sources, views, connection/read-back verification and selected-backend routing. GitHub/Obsidian remains optional; no dual live stores.
- Notion auto-saves Morning and provisional Evening, protecting the Notion-only Calendar ID section, then supports interactive same-page revisions. Diary-first Memory and independent Ledger approvals. Explicit personal planning window includes before/after work, independent of work hours.
- Short scheduled entrypoints, actual occurrence routing, independent Extra and Update Watch, read-only Notion Extra pattern; GitHub retains v6 claim protocol.
- Updated setup, profile, instructions, storage adapters, workflows, artifact/rules policies, upgrade and docs; public checker rejects initialized Notion IDs or missing configuration placeholders. Existing installations preserve history and explicitly resolve missing planning window; no automatic backend migration.
- Verification: static release gate and regression suite; real connector permissions and scheduled persistence require first-run user verification.

## 0.3.8 — 2026-10-17

### Changed

- Run the public privacy/structure and regression checks for pull requests and pushes to `main`, while the strict version/changelog comparison checks the entire pull request against its base. In-progress commits on a feature branch no longer trigger failing release checks or email noise.
- Verify on every CI run that the checked-in VERSION has one valid, dated CHANGELOG entry, even when no version bump is demanded for a work-in-progress push. Keep the strict PR check that requires a monotonic new version and updated release notes.
- Align the Extra-notification regression test with the existing setup wording. The notification recommendation itself is unchanged.
- Update contributor instructions to allow sequential GitHub file edits on a branch followed by a tested squash merge, which produces one complete release commit on `main`.

### Files, migration and limitations

- `.github/workflows/public-template-check.yml`, `scripts/test_setup_notifications.py`, `scripts/test_release_version.py`, `AGENTS.md`, `System/maintenance.md`, `VERSION`, `CHANGELOG.md`.
- No runtime instruction, profile/state schema, permissions, scheduled-task prompt or notification change. Existing private installations need no migration.
- A direct push to `main` still bypasses the *version-increase* comparison; use a PR and optional branch protection for reliable release enforcement. GitHub Actions alone does not block unprotected direct pushes.

### Verification

- CI runs the static privacy heuristic, regression tests (including current metadata consistency) and strict version/changelog comparison on the complete pull request. Static checks cannot prove actual scheduled-task or mobile-notification behavior.

Versions describe the reusable template, not a user's personal vault contents. The current source version is in `VERSION`; a private installation records its verified installed version and public-source commit in `System/profile.md`. File `schema_version` fields describe individual data formats and are not template versions.

## 0.3.7 — 2026-10-16

### Changed

- Evening Daily Memory can optionally preserve personally meaningful emotions, joys, worries and open questions, including approved cross-chat context with reliable same-day dates. Keep the three existing questions and user approval of the final note.
- Sunday Morning reviews the preceding Monday–Saturday through saved Daily Memories. It may offer specific, tentative, evidence-grounded personal observations; ChatGPT native Memory is optional background, not proof of the week's events.
- New installations offer a fourth Scheduled Task: **Daily Companion Update Watch**, a read-only 06:00 local condition-watch that checks the official public VERSION and release notes against the private installed markers. On verified new versions, invite the user to start a separate interactive, diff-reviewed upgrade. Never write or auto-upgrade from the scheduled check.
- Update quick-start and setup guides; add regression tests for new slots, approval boundaries and watch configuration.

### Files, migration and limitations

- `System/workflows/morning.md`, `System/workflows/evening.md`, `System/policies/artifacts.md`, `System/setup.md`, `System/upgrade.md`, `README.md`, `docs/GETTING_STARTED.md`, `docs/setup-guide.html`, `scripts/test_reflections_update_watch.py`, `VERSION`, `CHANGELOG.md`.
- No profile/state schema change, no Ledger migration or rewriting existing notes. Existing private installations retain their tasks and data; a newly offered update-watch task requires independent activation approval. Existing task prompts are not silently changed.
- Cross-chat context and native Memory may be incomplete; exact 06:00 execution, GitHub availability and silent no-change notifications depend on the platform. A change in the public repo without a verified release entry is not automatically an upgrade candidate.

### Verification

- Static regression tests cover Sunday scope, optional approved reflections, the three-question handoff and read-only update watch; real scheduled execution, update notification delivery and private upgrades still require observed end-to-end tests.

## 0.3.6 — 2026-10-16

### Changed

- Align Evening handoff wording and the existing regression assertions with the mandatory final-block heading from 0.3.5. The three capture questions and scheduled-task prompt are unchanged.

### Files, migration and limitations

- `System/workflows/evening.md`, `scripts/test_evening_handoff.py`, `VERSION`, `CHANGELOG.md`. No schema, state, permissions, notification, schedule or task migration; existing private copies still require a separately approved selective upgrade.

### Verification

- Check old and new three-question handoff regression expectations together; actual scheduled-run compliance still requires observing a real run.

## 0.3.5 — 2026-10-16

### Changed

- Make the Evening three-question handoff the mandatory final block on every scheduled run, including when external sources yield no results. Any Closing Thought must appear before the questions, and no farewell/status may replace them.
- Put all three capture questions directly in the new Evening Scheduled Task prompt as a short fail-safe; keep the current read-only scheduled boundary and post-answer interactive approval/save flow.
- During upgrades, explicitly check the **existing** Evening task prompt as well as repository files. Propose a prompt-only repair with separate approval when missing or stale, without changing schedule, task enablement or notifications.

### Files, migration and limitations

- `System/workflows/evening.md`, `System/setup.md`, `System/upgrade.md`, `scripts/test_evening_handoff.py`, `VERSION`, `CHANGELOG.md`.
- No state/schema, personal configuration, Ledger, Daily notes, consent or schedule migration. Private installations and previously created tasks do not automatically receive the new instructions. If a task cannot be inspected or updated, report that independently from repository upgrade status.

### Verification

- Regression checks require the three questions in the task prompt, the missing-source final-block rule and an explicit existing-task upgrade check. Future Scheduled Task behavior needs a real run to verify.

## 0.3.4 — 2026-10-14

### Changed

- Complete the previously pushed Morning repeat-suppression update: yesterday's approved Daily Memory suppresses unchanged handled decisions and informational mail (including non-Ledger items) for one Morning; previous Briefings also prevent stale FYI/email replays. Mere mentions of unresolved Ledger cards do not silence ordinary reminders. Today's due/revisit actions, requested reminders, material new evidence and required Calendar/source status still surface.
- Align Morning's full-Briefing deduplication, Evening's recording of confirmed handling decisions, and the Daily Briefing Visible Now coverage contract. Keep existing operational state and approval boundaries.
- Run Regression checks even if the independent version/release-notes CI gate fails, so release mistakes do not hide regression results; add focused static contract tests.

### Files, migration and limitations

- `System/policies/rules.md`, `System/workflows/morning.md`, `System/workflows/evening.md`, `System/policies/artifacts.md` (included from four previously pushed commits); `System/upgrade.md`, `.github/workflows/public-template-check.yml`, `scripts/test_morning_repeat_suppression.py`, `VERSION`, `CHANGELOG.md`.
- No state/schema, permissions, scheduled-task prompt/timing, private profile, Action Ledger or Daily artifact migration. Existing installations require a separately approved selective merge of source-owned instructions; private data and active tasks remain unchanged. This public template release does not update them automatically.

### Verification

- Static tests cover handled FYIs without Ledger cards, unchanged unresolved reminders, exceptions, whole-Briefing deduplication, Evening recording and independent CI regression execution. They cannot establish actual future scheduled-run compliance; that needs production observation.

## 0.3.3 — 2026-10-13

### Changed

- Strengthen the Evening check-in stop gate: every scheduled Evening check-in ends by asking the three capture questions and inviting a reply. The task must not sign off before that handoff; after the answers, the existing Memory/Ledger preview, approval and interactive save contract applies.
- Add the same concise handoff guard to the new-user Evening Scheduled Task setup prompt and a focused regression test. No change to independent approvals or read-only scheduled execution.

### Files, migration and limitations

- `System/workflows/evening.md`, `System/setup.md`, `System/upgrade.md`, `scripts/test_evening_handoff.py`, `VERSION`, `CHANGELOG.md`.
- No state/schema, permission, task timing, notification, Ledger or Daily file migration. Updating an already-created Evening task's prompt is a separate, explicitly requested action; this source release does not auto-upgrade private installations. Scheduled execution and notifications remain platform-dependent.

### Verification

- Static regression guards the three questions, explicit reply handoff and post-answer approval flow; real scheduled-run compliance still requires a future production check.

## 0.3.2 — 2026-10-13

### Changed

- Default new-user recommendation now enables `Notify when complete` on Daily Companion Extra (when available), as well as Morning and Evening, to prioritize a proactive alert when a Surprise is generated.
- Keep the engine's pre-due-day silence. Note that ChatGPT may nevertheless deliver completion notifications for silent daily checks; observe unwanted alerts before changing the design.

### Files, migration and limitations

- `System/setup.md`, `System/upgrade.md`, `README.md`, `docs/GETTING_STARTED.md`, `docs/setup-guide.html`, `scripts/test_setup_notifications.py`, `VERSION`, `CHANGELOG.md`.
- Setup guidance and tests only: no schema, permissions, task prompts, schedules, private profiles, Ledger or Daily artifact migration. Existing private installations retain notification preferences and task states; the source update does not automatically apply to private copies.
- Task-level notification controls may be absent or manual. Completion alerts and surprise receipt remain platform-dependent and are not proof of successful persistence.

### Verification

- Regression tests cover the on-by-default recommendation, silent pre-due-day engine behavior, and uncertainty about no-op platform alerts; static CI cannot verify device notification delivery.

## 0.3.1 — 2026-10-13

### Changed

- Add a one-time post-activation notification handoff for new installations: check the task-level `Notify when complete` control (where available) on Morning and Evening separately, ChatGPT Scheduled Task Push/Email preferences, and device/browser permissions.
- Require status reporting as observed, user-confirmed or unverified. Creating/enabling a task does not mean its per-task completion notifications are on; unsupported controls are handled with manual instructions. Do not recommend routine completion alerts for silent Daily Companion Extra checks.

### Files, migration and limitations

- `System/setup.md`, `System/upgrade.md`, `README.md`, `docs/GETTING_STARTED.md`, `docs/setup-guide.html`, `scripts/test_setup_notifications.py`, `VERSION`, `CHANGELOG.md`.
- Guidance-only release. No schema/permissions/task-prompt/schedule/notification-state migration, no automatic changes to existing tasks, and no effect on users' private Ledger, Daily artifacts or profile. Private copies require a separately approved selective upgrade, and task-level controls may be absent depending on client and plan.
- A successful task or a completion notification does not prove GitHub persistence or successful approvals.

### Verification

- Added regression checks for the notification handoff and consistency across starter guides. Public privacy/release checks and remote CI remain distinct from end-to-end mobile notification delivery, which cannot be certified by static tests.

## 0.3.0 — 2026-10-13

### Changed

- Prefer an interactive approval panel after a complete Morning Briefing or post-check-in Evening Memory. Independent default-selected choices apply to the Daily artifact and an explicitly previewed Action Ledger delta; a checkbox is not approval until submitted in the interactive conversation.
- Add optional correction feedback, partial approvals, per-item result verification and a mandatory text-only fallback when interactive controls are unsupported. No Ledger checkbox is shown without a specific proposed change.
- Preserve exact user-visible artifact save semantics, explicit state-change authorization, fresh Ledger review, concurrency checks, and scheduled Morning/Evening read-only boundaries. Private users' Daily data and Ledger belong only in their private GitHub repository, never this public source.

### Files, migration and limitations

- `System/policies/artifacts.md`, `System/workflows/morning.md`, `System/workflows/evening.md`, `System/upgrade.md`, `README.md`, `VERSION`, `CHANGELOG.md`.
- No schema, permission, scheduled-task, profile, Surprise-engine or stored-data migration. Existing private installations may apply the new approval instructions selectively under the normal interactive upgrade process, preserving custom behavior/history. Older Surprise migrations still apply where needed.
- UI rendering depends on ChatGPT client and scheduled-task capabilities; falling back to paired text is required. Publishing source does not automatically upgrade any private copy or validate an actual future task.

### Verification

- File-level approval/regression invariants and scoped public-state/privacy review; automated public CI/release checks and live production UI behavior are tracked separately.

## 0.2.1 — 2026-10-12

### Changed

- Rewrite Resources/Obsidian GitHub GitSync Setup.md around creating one private template copy, completing ChatGPT setup first and optionally adding Obsidian devices. Existing installations keep their setup/data and use the upgrade entrypoint.
- Align System/setup.md bootstrap and guide links; document current Extra-only scheduled state writes, device sync versus template upgrades, existing ignore rules, conflict handling and private-state preservation.
- Correct iOS cloning to a newly created empty Obsidian-accessible local vault, and reference the GitSync author's current mobile/app-trigger instructions. Automation is not proof of completed sync.

### Upgrade and verification

- Documentation only relative to 0.2.0: no runtime schema, permission, task-prompt or schedule migration. Preserve all private configuration, notes, Ledger/history, dates/claims, customizations and paused tasks. Apply only approved source-owned guide/bootstrap changes and normal verified version markers; older runtime versions still follow their applicable migration.
- Public privacy/structure and release-version checks, 21 existing validation tests, documentation links and process consistency reviewed. Mobile procedures were checked against primary documentation; no actual phone sync or private-vault upgrade is claimed.

## 0.2.0 — 2026-10-12

### Changed

- Replace seed/SHA-256 scheduling with Surprise schema v6 and one next_due_date in the private Extra Markdown file. Setup chooses a date in the next complete calendar week; before it Extra is silent, on/after it one delivery is eligible, then the next date is chosen in the week after the local delivery attempt. Its save is verified before the final response, so no tools are required after rendering. No bulk dates, code execution or weekly approve.
- Extra now has an explicitly consented scheduled-write exception for five scheduling/delivery fields in its own private engine. Morning/Evening, Daily notes, Ledger, profile, Gmail and Calendar keep their prior write boundaries. The public scheduled_writes_authorized flag is false.
- Conditional claim plus schedule advancement before final output reduce duplicate attempts. last_attempt_date records an attempted run, not a delivery receipt. Interrupted/uncertain claims stay pending for interactive recovery. A crash after advancing may miss output while preserving the next date; a crash at a pending claim needs recovery. This may miss a delivery; GitHub and chat output are not atomic and exactly-once delivery/notification receipt is not guaranteed. Date choices are conversational, not cryptographic/uniform randomness.
- Remove the mandatory scheduled calculation test. Report configured/enabled versus observed scheduled persistence separately, with actual operation/error diagnostics. A known unavailable writer still blocks Extra.

### Files and upgrade

- Updated engine, setup, global/artifact boundaries, privacy/getting-started docs, README, public checker and release checklist. Removed the obsolete calculator and its tests; added public-starter validation tests.
- Existing v5/older private copies require the approved migration in System/upgrade.md: preserve setup/configuration, pause status, feedback, notes and Ledger/history; initialize one date after migration completion, remove old cadence keys, grant the scoped write permission only with explicit consent, and replace the Extra prompt's old never-write clause. Never automatically enable a paused or previously inactive task or recreate working Morning/Evening tasks.
- Public source publication does not update private copies. Local/static tests and review do not claim actual scheduled private-repository write access; inspect the first due run separately.

### Verification

- Public privacy/structure check, release-version comparison, and 21 validation tests cover blank v6 state, accidental dates/claims/consent, contradictory duplicate state fields, retired schema/seed keys and release consistency. Runtime instruction scenarios are reviewed separately; these tests do not execute a GPT scheduled task.

## 0.1.0 — 2026-10-12

First explicitly versioned experimental template. Earlier copies are **unversioned**, not presumed to be any numbered release.

### Added

- `VERSION`, this changelog, and `System/upgrade.md` for an interactive, state-preserving upgrade.
- Optional `installed_template_version` and `installed_template_commit` metadata in the private profile. They remain null in the public starter and are recorded only after installation/upgrade verification.
- “Check for updates” and “Upgrade Daily Companion” routing, including older copies without a local upgrade entrypoint.
- Root `AGENTS.md` and `System/maintenance.md` for consistent release maintenance through Codex or GPT web, plus a CI version/changelog gate for public updates.

### Current behaviour included in this release

- Surprise schema v5: one pseudorandom day per current calendar week, beginning the week after setup, calculated from one seed and start week. No bulk future-date list or weekly `approve`; explicit pause disables Auto. Scheduled runs remain read-only.
- Setup aligns the provisional Surprise start week when unfinished setup resumes across weeks, preserves the seed, and verifies task activation individually.
- Public blank-template CI runs only in the public source repository; initialized private copies skip it.

### Upgrade notes

- Keep the user's configuration, note folders, Ledger and histories. Never replace initialized state with the blank public starter.
- Older Surprise formats require the explicit schema migration in the engine contract, preserving enabled/pause status and style-feedback history. Existing valid v5 seeds/start weeks must not be redrawn.
- Verify exact calculation capability in the scheduled environment before reporting Extra as operational. Morning/Evening may remain available when Extra cannot be verified.
- A template upgrade does not automatically create tasks, change their times, enable notifications or rerun onboarding. GitHub template copies do not synchronize with the public source automatically.

### Verification

- Public template privacy/structure heuristics and 18 regression tests pass. Git/CLI probes cover the first numbered release, version increases, missing version/notes, initial repository commits and new branches without a reliable comparison baseline.
- No upgrade of a real private vault or execution in a scheduled environment is claimed by these checks. Those require the verification described in setup and the upgrade entrypoint.

## Unversioned — earlier public copies

Earlier public history has no reliable template version marker. Preserve those copies and compare actual files during the first upgrade. Do not infer template versions from commit dates, an engine schema number or `setup_complete` alone. See [the original publication notes](docs/RELEASE_NOTES.md) for historical context.

## Maintaining future releases

- Use `MAJOR.MINOR.PATCH` with no leading `v` in `VERSION`. This package is experimental while the major version is 0.
- Increment the patch for compatible fixes, the minor for features or migrations within the experimental series, and the major for a stable release or breaking changes after 1.0.
- Add a dated release entry describing user-visible changes, affected files, required migrations and capability limitations. A migration must say what is preserved and how failures are handled.
- Commit the version bump, final release notes and release files together. Do not change shipped runtime behaviour under an unchanged version. The upgrade flow pins an immutable source commit; do not rewrite published Git history to replace a release.
- Run the public-source check and applicable regression checks, then verify CI. Template changes must never include private installation data or test-user state.
