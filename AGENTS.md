# Daily Companion repository instructions

Read `System/maintenance.md` before changing the public template. These instructions apply to Codex and other coding agents working in this repository. GPT web users should explicitly ask their assistant to read the same maintenance entrypoint before editing.

## Identify the destination

- The canonical public template is `yilinqiao/daily-companion-with-chatgpt`.
- A private copy belongs to its user. Use the configured System path there, preserve all configuration, notes and operational history, and follow `System/upgrade.md` for template upgrades. Private personalization does not bump the upstream template version or stamp a new installed version.
- Never send private files, credentials, configuration or test-user state to the public source. Do not infer the destination from a matching filename alone.

## Public template changes are releases

- Every public template update must include an appropriate monotonic `MAJOR.MINOR.PATCH` bump in root `VERSION` and a dated entry in `CHANGELOG.md`, in the same commit as the final changed files. The first versioned release starts at 0.1.0; earlier copies are unversioned.
- Describe the actual behaviour, affected files, compatibility, state migration and verification. Do not use `schema_version` as the template version or reuse a shipped release number for new instructions.
- Read and update `System/upgrade.md` whenever the change affects migration, file ownership, preserved state or required capabilities. Preserve its routing from `System/instructions.md`, and keep README/setup/upgrade instructions consistent.
- Keep `System/profile.md` unconfigured with installed metadata null, the Ledger empty and Surprise state uninitialized with scheduled-write consent false. Update reusable rules without copying personal values into them.
- Run `python -B scripts/check_public_release.py`, applicable tests, and `python -B scripts/check_release_version.py --base <previous-public-commit>` on the staged release commit. Verify CI and remote read-back before reporting publication complete. A read-only pre-commit review may inspect the same proposed files; the version gate checks committed changes.
- Use a normal versioned commit with a verified expected branch head. Never force-push, replace Git history or bypass a write/safety block.

## Existing private installations

“Check for updates” is read-only. “Upgrade Daily Companion” prepares a specific private upgrade under `System/upgrade.md`; preserve custom rules and state, obtain the applicable approval, and verify the result before updating installed markers. Do not rerun onboarding, create duplicate tasks or enable paused tasks as a side effect.

Markdown contracts require the assistant to read them. Do not claim these rules were followed by a chat that never retrieved this repository or its maintenance entrypoint.
