# Changelog

Versions describe the reusable template, not a user's personal vault contents. The current source version is in `VERSION`; a private installation records its verified installed version and public-source commit in `System/profile.md`. File `schema_version` fields describe individual data formats and are not template versions.

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
