# Changelog

Versions describe the reusable template, not a user's personal vault contents. The current source version is in `VERSION`; a private installation records its verified installed version and public-source commit in `System/profile.md`. File `schema_version` fields describe individual data formats and are not template versions.

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
