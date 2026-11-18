# Changelog

## 0.5.3 — 2026-11-18

- Restore bounded Calendar recovery on incomplete coverage/unsolved candidates (even after Auto-Saved Memory), reconcile all examined dates, and preserve independent financial recovery. Restore explicit Notion runtime field mapping and optional protected Calendar account provenance (old two-ID records remain valid).
- Keep all three Evening questions when auto-save fails; defer preview, preserve diary voice, fresh-read Ledger after answers and private rules/consent before interactive writes. Distinguish Extra no-op silence from actionable failure, and clarify combined-task notification trade-off.
- Tighten pinned setup and upgrade integrity, semver/SHA markers and partial-failure task suspension. No mandatory schema or state migration; private installs may adopt updated instructions and prompts through approved upgrade, preserving existing data.
- Add maintenance-only behavioral contracts (BC-01–16), release review and static regression sentinels. Review BC-04/05/07–15 for this release; unchanged onboarding/planning, dedupe and weekly/flavour contracts remain covered by existing regressions. Actual onboarding, scheduled access and approval behavior remain unverified in a live client.

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
