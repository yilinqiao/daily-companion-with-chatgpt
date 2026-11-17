# GitHub storage (alternative)

Use only the confirmed private repository, never the public template. Onboarding: Use this template → Create a new repository → Private (default branch only; do not fork). Connect GitHub with read/write access to that repository; confirm visibility, read the full required package, and obtain approval before personal writes. Obsidian is optional; see Resources/Obsidian GitHub GitSync Setup.md. No Notion access required. All logical System paths resolve to the configured system_folder; Daily filenames use the configured daily_folder.

Read-only Morning and Evening; save exact approved Markdown interactively, including hidden Calendar metadata under artifacts.md. The Ledger is the Kanban file under rules.md; preserve list order, plugin settings and card metadata. Extra uses the v6 engine and requires separate standing consent for its five scheduled write fields. The Update Watch is read-only.

## Approved setup initialization

For this backend follow the staged steps below after the shared setup approval. Section 4/5 references mean the shared connector checks/approval in System/setup.md; Section 8 refers to readiness below. Include both storage adapters and upgrade.md in the required package. Set storage_backend: github and approved planning window; leave Notion identifiers null and notion_daily_autosave_authorized false. No tasks until readiness and separate activation.

## 6. Commit profile configuration, without completing setup

After the user explicitly approves the summary, update **only** `profile.md` in the user's private repository. Replace every applicable `<SETUP_REQUIRED...>` placeholder with the approved configuration and populate the fixed work-schedule days/hours. Keep:

```yaml
setup_complete: false
```

This value means the full installation is not verified yet, even if the personal profile is complete. Never turn it true as part of the initial profile write.

For a fresh install, leave `installed_template_version` and `installed_template_commit` null until Section 8 verifies the complete package. A resumed initialized installation preserves any previously verified markers; never replace them with an assumed latest release.

Do not insert personal configuration into `instructions.md`, workflow files or policy files. `profile.md` is the single source of truth for user-specific runtime configuration. Save the confirmed canonical `github_repository` together with the repository-relative vault paths. Populate `approved_data_sources` only from the user's approved source choices after any applicable connector preflight has succeeded; `ChatGPT surfaced conversation context` requires explicit permission but no connector preflight. A source the user declined or that remains technically unverified must not be listed as approved. Save the confirmed location as `normal_location`, the confirmed state/province/region as `region` (or null when not useful), the resolved timezone as `timezone`, and the weather lookup location separately as `weather_location`. Runtime regional-holiday decisions must use `normal_location` / `region`, not infer location from `weather_location`. For Calendar scope, use `calendar_scope.mode: include_all` and save only explicitly excluded stable calendar IDs under `calendar_scope.excluded_calendar_ids`. Newly visible calendars are therefore included automatically unless the user later excludes them. Calendar discovery is configuration plumbing, not permission to read Calendar when Google Calendar is absent from `approved_data_sources`. Add other stable profile fields only when the user explicitly provided them and they materially help planning; do not infer them from connected sources.

**Write and verify boundary:** Fetch the current file and blob SHA; update this single file with the supported GitHub file-update operation and an informative commit message. Fetch it again from the same repository and branch. Confirm the saved fields match the approved summary, no required placeholders remain, and `setup_complete` is still false. Record the verified commit SHA only in the session report, not in stable profile preferences. Never assume success from a prepared Git blob/tree alone.

On a write error, safety block, read-back mismatch or concurrent SHA conflict, **stop** and report the exact failed stage. Do not claim that data was saved, change method to evade a safety block, initialize other state, or create tasks. A later user-authorized retry may resume from the current verified files without duplicating completed writes.

## 7. Initialize and verify state, one file at a time

- Initialize `action_ledger.md` as an Obsidian Kanban Markdown file using the fixed lists `Action`, `Waiting`, `Upcoming`, `Closed`, the schema/card format in `policies/rules.md`, and clean Kanban plugin metadata/settings.
- Keep all four lists empty unless the user explicitly asks to seed current/historical operational items.
- If seeded, use human-readable cards with stable IDs and hidden `dc` metadata under `policies/rules.md`.
- For an older installation using `open_items.md`, preserve the file/state first, then migrate it to `action_ledger.md` without losing active cards, order, metadata or historical evidence. Update the profile path key from legacy `open_items_file` to `action_ledger_file`.
- Schema-v3/v4/v5 migrations add/retain the fixed `Closed` list and migrate to Action Ledger schema v6. A legacy non-empty `Pending Admission` section must be reconciled interactively before removal; unresolved items become proposed open cards, while reliably resolved/no-action/cancelled items may become Closed history. Never silently discard an entry.
- Legacy `pending_close` metadata is not part of the new model. Reconcile each affected card: confirmed ended → move the same card to `Closed`; otherwise keep the appropriate open status. Remove legacy fields only through an authorized/approved migration.
- `memory.md` is no longer a required runtime file. For an older installation with non-empty `memory.md`, preserve it as legacy/reference material until the user explicitly chooses to archive/delete/migrate its useful domain context. Do not silently discard user data. A clean new installation does not create `memory.md`.
- Initialize `daily_companion_extra.md` under schema v6. Preserve the engine body; set `enabled: true` unless opted out and `scheduled_writes_authorized: false` until the explicit activation consent in shared activation section in setup.md. Choose one arbitrary valid local date in the complete Monday–Sunday week after current setup, storing only `next_due_date`. Initialize `delivery_status: idle`, `delivery_due_date: null`, `delivery_claimed_at: null`, `last_attempt_date: null` and blank feedback for a fresh installation. No seed, Python, hash, executable script or future-date list. Read back and validate the date/state. Explicit pause disables Auto; Manual stays available. Finalize the provisional date against the actual completion week in Section 8; keep the chosen date hidden from normal setup output.

For a clean installation, initialize `action_ledger.md` **first**. Then read it back and verify the four required lists and valid schema, without erasing existing cards. Initialize `daily_companion_extra.md` **second** according to the approved setup contract; preserve the engine body and existing valid state on resumed setups. Read it back and verify `enabled`, cadence/state fields, and the engine body. Neither step may modify `profile.md` or any other file in the same GitHub write.

Use a fresh content SHA for each existing file; one file per commit, followed immediately by a read-back from the intended repository and branch. Skip an already-correct file on resume and preserve its valid date/claim/history. For a new installation still incomplete and never activated, only an out-of-week provisional date may be reselected as specified in Section 8 under the original approved setup write. This is not permission to reset a live or legacy installation. Never overwrite an existing personalized or non-empty ledger, surprise state, or historical Daily artifact to force setup forward. Report a blocker and request approval for a specific repair or legacy upgrade under the engine's migration contract.

**Stop gate:** If either state write or verification fails, leave `setup_complete: false`. Report what is committed versus pending; do not activate scheduled tasks. A platform safety block must be surfaced, not bypassed by alternate APIs or repeated writes.

## 8. Verify readiness, then finalize setup status

Verify that this System folder contains and can read:

- `setup.md`;
- `instructions.md`;
- `profile.md` with approved fields populated; keep `setup_complete: false` until final readiness commit;
- `action_ledger.md`;
- `daily_companion_extra.md`;
- `workflows/morning.md`;
- `workflows/evening.md`;
- `policies/rules.md`;
- `policies/artifacts.md`.

Confirm `profile.md` has all required approved configuration fields populated, `github_repository` identifies the canonical runtime repository, `normal_location` / `region` are present as applicable, Calendar scope is present when applicable, and all referenced repository-relative vault/System/Daily/Action-Ledger paths are valid or clearly report any unresolved path issue. Verify Surprise schema v6, valid next_due_date, consistent idle/claimed state, boolean scheduled-write consent and expected enabled/opt-out status under the engine contract; do not surface planned dates. A completed installation may have an overdue date or a pending claim; these are not reasons to reset it. Pending claims need interactive recovery before resuming Auto. Reconfirm that each connected source listed in final `approved_data_sources` passed the shared setup preflight during this onboarding session; do not rely on a stale historical “verified” claim. If `ChatGPT surfaced conversation context` is listed, verify explicit user approval; no connector preflight or same-day conversation availability is required during setup. When Google Calendar is approved, verify include-all-by-default scope with only explicit exclusions stored. Do not claim setup is complete until the runtime package is readable and approved connected sources are verified. Confirm `daily_folder` is writable or can be created on the first approved save; report any unresolved issue before finishing.

Immediately before finalizing a **new, incomplete, never-activated** installation, resolve the local date again. Keep the provisional next_due_date if it lies in the complete week after completion; otherwise choose one date from that next week's seven dates. Change only the date, preserving enabled choice, consent, history and body. On cross-week resume this alignment is covered by the approved setup write. Commit this file alone and verify before the final profile commit. Never redraw a completed/live installation's valid date or clear a pending claim.

After readiness and any authorized date alignment succeed, perform a **separate final single-file update** to `profile.md` setting `setup_complete: true`. For a new versioned install, also record `installed_template_version` from the verified copied `VERSION` and `installed_template_commit` as the verified public-source baseline SHA (or null when unknown); change no user preferences or permissions. Preserve previously verified markers during ordinary setup review. Fetch it again and confirm the flag, metadata, configuration and local completion week. If a new installation crossed a week boundary during finalization, do not activate tasks or declare readiness: under the same setup authorization, first restore the flag to false and clear only newly recorded completion markers, verify, then align only the provisional date while preserving other state, and retry the final verified profile commit. Stop and report a failure at any stage. This flag means *repository installation* is complete, not that Scheduled Tasks exist or are enabled.

If `setup_complete: true` is found on a resumed or legacy install while state is incomplete, treat it as an inconsistent state: report it and ask before repairing it. Never infer completion from the flag alone.

Show a concise installation report distinguishing (1) profile configured, (2) state initialized, (3) repository verified and finalized, and (4) scheduled task activation pending/verified. Do not conflate these statuses.
