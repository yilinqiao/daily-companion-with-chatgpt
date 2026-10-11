---
type: companion-setup
schema_version: 2
---

# Daily Companion Setup

*Package revision: 2026-10-11 - GitHub/GitSync architecture, Action Ledger schema v6, read-only Companion Surprise engine with interactive cadence approval.*

This folder is the clean Daily Companion installation package. All runtime files are intentionally generic and contain no user-specific personal information before setup. It is the canonical clean installation package: maintainers must keep it structurally and behaviourally aligned with the current Daily Companion system without copying any user's personal configuration or state into it.

Use this file only for onboarding, setup verification and initial Scheduled Task creation. After all required state files have passed verification and `profile.md` has `setup_complete: true`, the daily Scheduled Tasks start from the Morning/Evening workflow entrypoints and the Companion Surprise engine. Each runtime file then loads `instructions.md` and the shared policies; normal runs do not use this setup file.

## 0. Getting started — first-run bootstrap

This setup file is the entry point for a new user, but Markdown does not run itself. It must be read from `System/setup.md` inside the user's own Daily Companion GitHub repository, with the starter folder structure preserved. Do not personalize a shared/reference copy of the clean bundle in place.

For a new installation:

1. create a private GitHub repository for the user's Daily Companion vault (recommended: the repository root is the Obsidian vault root);
2. copy the contents of `Daily Companion Starter` into that repository, preserving the `System/`, `Daily/`, `Archives/`, `Area/`, `Projects/` and `Resources/` structure, then commit and push;
3. clone/sync that repository to each device and open the local repository folder as the Obsidian vault. On phones use GitSync; on desktop use GitHub Desktop or another normal Git client;
4. connect ChatGPT to GitHub and grant it access to the intended repository;
5. start setup with a prompt such as:

```text
Read `System/setup.md` from GitHub repository `<owner>/<repo>` and start Daily Companion setup.
```

If the package is still in the shared/reference clean-package location rather than the user's own repository, stop and ask the user to install/copy it first. Do not personalize the shared `Daily Companion Starter` source in place.

In the shared "User instructions" bundle, the clean package folder is named `Daily Companion Starter` so it cannot be mistaken for a live runtime vault. The user's GitHub repository becomes the canonical remote copy and version history. Each device keeps a local working copy for Obsidian; GitSync (mobile) or a normal desktop Git client synchronizes local edits with GitHub. ChatGPT reads and, after explicit interactive approval, writes the configured GitHub repository directly. Device sync and ChatGPT repository access are separate paths that converge on the same GitHub repository.

GitHub repository access is a required platform prerequisite because profile, Action Ledger state and Daily artifacts live in that repository. Google Calendar and Gmail are optional runtime sources, but are recommended for the full Daily Companion experience and must be both user-approved and technically verified before they are treated as available. Device-specific GitSync guidance is provided by the user-facing setup guide and `Resources/Obsidian GitHub GitSync Setup.md`.

## 1. Check setup state

Read `profile.md` and check the required package, not `setup_complete` alone. The required files are:

- `setup.md`;
- `instructions.md`;
- `profile.md`;
- `action_ledger.md`;
- `daily_companion_extra.md`;
- `workflows/morning.md`;
- `workflows/evening.md`;
- `policies/rules.md`;
- `policies/artifacts.md`.

- If all required files exist/read correctly and `profile.md` has `setup_complete: true`, also validate the Action Ledger and Companion Surprise state before treating setup as complete. Scheduled Task activation is a separate verified step. If state is valid, ask whether to continue, review selected settings, or intentionally re-run onboarding.
- If `setup_complete: true` but one or more required files are missing/unreadable, treat the installation as incomplete/repairable rather than claiming setup is complete. Preserve existing files and offer to restore only the missing/incomplete package pieces.
- Do not overwrite a completed setup without explicit approval.
- When reviewing or re-running onboarding, preserve the existing `action_ledger.md` by default. Never erase operational or Closed history merely because profile settings are being changed.
- Never modify or regenerate historical Daily Briefing / Daily Memory files as part of onboarding or re-onboarding.
- If setup is incomplete, continue onboarding or repair as appropriate.

## 2. Onboarding style

Set expectations early: the user answers a short set of questions, then setup performs harmless connector checks, then it shows one summary and changes files only after explicit approval. GitHub repository access is required; any approved Calendar/Gmail sources must also be enabled in the ChatGPT connector settings. If a preflight fails, setup explains what to connect or authorize and lets the user retry or revise.

Run setup conversationally. At the beginning, tell the user there are only a handful of questions and setup should normally be quick.

- ask one topic per turn and wait for the answer before continuing; the paired Morning/Evening times are deliberately collected together in one schedule question;
- briefly explain why a question matters when useful;
- accept natural-language answers and do not force the user into fixed-choice answers;
- keep setup friendly and lightweight rather than making it feel like a long form;
- suggest sensible defaults when appropriate, but require user confirmation for collected user configuration;
- do not ask about or preview the built-in Companion Surprise feature during onboarding. It is enabled by default and initialized during the approved setup write; the user first learns of it if and when a surprise arrives, and that delivery ends with an approve/stop prompt; users can also pause it at any time by explicitly asking to stop/disable surprises;
- do not infer missing onboarding answers from Gmail, Calendar, native ChatGPT Memory or other sources.

## 3. Collect required configuration

Collect and confirm the fields below. Use the specified defaults without separate questions, disclosing them in the final approval summary. The suggested questions are reference wording, not a rigid script: keep the meaning stable while adapting naturally to the conversation. Ask exactly one user-facing question per turn and wait for the answer before continuing. Never present multiple onboarding questions in one message or present the whole list as a form.

1. **Preferred name**  
   Collect `preferred_name`.  
   Suggested question: **“What would you like me to call you?”**

2. **Normal location / region / timezone / weather location**  
   Suggested question: **“Where are you normally based?”**  
   Resolve the appropriate IANA timezone from the confirmed location when confident; do not ask for a timezone string separately. If location is ambiguous enough that timezone cannot be resolved reliably, clarify the location. Resolve and explicitly confirm the relevant state/province/region when public holidays or other local rules can differ; allow `region: null` where no subdivision is useful. Default `weather_location` to the confirmed normal location unless the user wants a different weather lookup location.

3. **Regular work schedule**  
   Suggested question: **“Do you have a regular work schedule I should keep in mind — fixed hours, variable shifts, or no regular schedule?”**  
   If fixed, follow with: **“What days and hours do you usually work?”**  
   New onboarding must resolve to `fixed`, `variable` or `none`. During migration/repair, an existing `unknown` may be preserved temporarily until the user confirms the real pattern. Never infer the schedule from Calendar, Gmail or planning gaps.

4. **Normal output language**  
   Suggested question: **“What language should Morning and Evening Companion normally use — English, Chinese, another language, or follow the language of your current message?”**  
   Do not infer a fixed language from the language used during setup.

5. **Communication style**  
   Suggested question: **“How would you like the Companion to sound? For example warm, direct, concise, gentle, playful, detailed or practical — or describe it in your own words.”**

6. **Default personalisation (no separate questions)**
   Set `preferred_name_usage: occasionally`. Enable all Daily Flavour categories by default: `weather`, `weather_tied_to_plans`, `humour`, `fun_fact`, `inspiration`, `tiny_challenge`. Treat weather as separately permission-gated, and select exactly one non-weather Daily Flavour item in each Morning Briefing according to `workflows/morning.md`. The user may change or disable any category later. Show these defaults in the final summary for approval, but do not ask individual questions about them.

8. **Runtime data-source permission**  
   Explain first that the configured GitHub repository is required as Daily Companion storage and is separate from optional information sources. Then collect optional source permissions **one question per turn**, in this order:
   - First ask: **“For the full experience, I recommend Google Calendar and Gmail as well. Are you comfortable allowing Daily Companion to read both, only one, or neither?”**
   - After the user answers, ask in the next turn: **“Would you like Daily Companion to use web and weather information when useful?”**
   - After the user answers, explain the optional conversation-context feature and ask in the next turn: **“For Evening Daily Memory, would you like me to use ChatGPT conversation context that is already surfaced to the current run to remember meaningful things you explored across chats? It can be incomplete, and I will only record an item as today when its surfaced conversation metadata reliably dates it to today or you confirm it.”**  
   Record these answers as provisional source permissions only. User permission and technical connector access are separate requirements for connected sources; do not read Gmail or Calendar merely to infer consent. Never assume permission for an unapproved source. `ChatGPT surfaced conversation context` is not a complete chat-history connector and has no account-wide enumeration guarantee; approval only permits the runtime to use conversation context that ChatGPT actually surfaces. Other relevant sources may include recent Daily Memory, Projects/Area/Resources, Slurped Pages and future connected sources.

9. **Calendar scope, when Calendar permission is granted**
    The default scope is include-all with no exclusions; no exclusion question is asked during the configuration phase. Exclusions are collected in Section 4.2 only after the Calendar preflight enumeration succeeds.

10. **GitHub repository**  
    Prefer the repository explicitly named in the entry prompt and successfully used to read this setup file. State the detected `owner/repository` and ask for confirmation only if ambiguous; do not ask the user to retype a verified repository. Record it as `github_repository` and include in final approval summary.

11. **Storage defaults (no questions)**
    Use `vault_root: .`, `system_folder: System`, `daily_folder: Daily`, and `action_ledger_file: System/action_ledger.md`. Set filenames to `YYYY-MM-DD Daily Briefing.md` and `YYYY-MM-DD Daily Memory.md`. Only ask about deviations if the detected repository layout makes these defaults invalid or the user requests customization. Include defaults in final summary.

12. **Daily schedule (one combined question)**
    Suggested question: **“What local times would you like Morning and Evening Companion to run? I suggest 8:00 AM and 8:00 PM.”** Collect both times together; do not assume suggested times without approval. Store them separately as `morning_companion_time` and `evening_companion_time`.

There is no separate global `memory.md` onboarding setting. Stable configuration belongs in `profile.md`; operational continuity belongs in the Action Ledger; project/domain context stays with its source/area.

## 4. Verify connector access

Before presenting the final setup summary or writing user-specific configuration, verify that every connected source the user intends to approve is actually accessible. **Permission and connectivity are different:** a user saying “yes” authorizes a source; a successful harmless read proves the connector is usable. Both are required before a connected source becomes final `approved_data_sources`.

### 4.1 GitHub repository — required

- Reading this `setup.md` from the intended `github_repository` proves initial repository read access; verify the other required package files from the same repository.
- Keep all runtime reads inside the configured repository rather than substituting a same-named file from elsewhere.
- Setup later personalizes `profile.md` and initializes/verifies the Action Ledger; those approved interactive commits provide practical confirmation that the intended repository is writable.
- If the intended repository/package cannot be read, or an approved setup write cannot be committed, do not continue to completed setup or Scheduled Task creation. Explain the repository/permission/path problem and let the user fix GitHub access, then retry.

### 4.2 Google Calendar — only after user permission

- After the user grants Calendar permission, perform a harmless read by enumerating the calendars visible to the connected account. This access check and Calendar-scope discovery are the same operation.
- On success, collect exclusions here (this is the only place they are collected): present all visible calendars as a short numbered list, including primary, shared/family and contextual calendars such as holidays when visible. Explain that all visible calendars are included by default and ask: **"Which calendars, if any, would you like Daily Companion to exclude?"** Accept numbers, names or natural-language answers such as `none`. Record exclusions by stable calendar ID, not display name; newly visible calendars are therefore included automatically unless the user later excludes them.
- On failure, do not infer scope, do not record Google Calendar as an approved source, and do not pretend access exists. Ask the user to connect/authorize Calendar and retry, or let them explicitly revise setup to continue without Calendar.
- Never create/change Calendar events during setup merely to test access.

### 4.3 Gmail — only after user permission

- After the user grants Gmail permission, perform a harmless metadata-level read such as listing Gmail labels (or an equivalently minimal read supported by the connector). Reading message content is not required merely to prove access.
- On failure, do not record Gmail as an approved source and do not pretend access exists. Ask the user to connect/authorize Gmail and retry, or let them explicitly revise setup to continue without Gmail.
- Never send, draft, archive, label, delete or otherwise modify mail during setup merely to test access.

### 4.4 ChatGPT surfaced conversation context — only after user permission

- This is an optional runtime context source, not a connector that exposes or enumerates the user's complete ChatGPT history. There is no separate account-access preflight analogous to Calendar/Gmail.
- If the user approves it, record the exact source label `ChatGPT surfaced conversation context` in final `approved_data_sources`. If the user declines it, do not list it and Evening must not use cross-chat context for Daily Memory.
- Lack of surfaced cross-chat context during setup is not an access failure. Runtime availability is opportunistic: Evening may use only conversation context actually surfaced to that run and must follow its strict same-day timestamp/confirmation rules.
- Do not infer this permission from the user's ChatGPT Memory setting, project membership, account plan, or the mere fact that some conversation context happens to be available.

### 4.5 Other connected sources

When the user approves another connected source that Morning/Evening will rely on, use the least-invasive available read to verify it before treating it as available. Sources such as web/weather that do not require a user account connector do not need account-access verification, though their use still requires whatever permission/configuration the runtime defines.

### 4.6 Reduced-source setup

Google Calendar and Gmail are recommended, not mandatory. If the user explicitly declines either one, the system may continue in reduced-source mode because the runtime already handles unapproved sources conditionally. Do not include a declined or failed source in final `approved_data_sources`. If the user wants a source but its access check fails, pause that source's setup until they either fix access or explicitly revise their source choice. Never silently drop an intended source just to finish setup.

## 5. Present setup summary

Before changing files, show a concise summary of all collected configuration **plus source-access status** and ask the user to approve, request changes or cancel. The access portion should distinguish:

- GitHub repository: read verified / blocked (write confirmation occurs through the approved setup commit before task creation);
- Google Calendar: approved + verified / declined / blocked;
- Gmail: approved + verified / declined / blocked;
- ChatGPT surfaced conversation context: approved / declined (no connector preflight; runtime availability is opportunistic and incomplete);
- any other approved connected source: verified / blocked.

Only sources that require connector access may appear as connected sources after both user permission and successful required access verification. `ChatGPT surfaced conversation context` may appear in `approved_data_sources` after explicit user permission because it has no separate connector preflight. Do not include connector IDs, account secrets or unnecessary account metadata in the summary or profile.

Only continue after explicit approval.

## 6. Commit profile configuration, without completing setup

After the user explicitly approves the summary, update **only** `profile.md` in the user's private repository. Replace every `<SETUP_REQUIRED...>` placeholder with the approved configuration and populate the fixed work-schedule days/hours. Keep:

```yaml
setup_complete: false
```

This value means the full installation is not verified yet, even if the personal profile is complete. Never turn it true as part of the initial profile write.

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
- Initialize `daily_companion_extra.md` with the schema-v4 weekly schedule contract. Preserve the engine body; set `enabled: true` unless explicitly opted out; choose one random date independently within each of the next 104 complete Monday–Sunday weeks starting next Monday, and populate `weekly_due_dates` in ascending order. Do not use obsolete `next_due`, `min_gap_days` or `max_gap_days` fields. Verify the full list and each week after committing this file. The existing daily read-only Scheduled Task compares the local date against the dates list; it never advances the list and each subsequent week remains eligible without the user's `approve`. If explicitly opted out, store `enabled: false`; Manual Mode remains available. Keep random future dates hidden from normal setup conversation.

For a clean installation, initialize `action_ledger.md` **first**. Then read it back and verify the four required lists and valid schema, without erasing existing cards. Initialize `daily_companion_extra.md` **second** according to the approved setup contract; preserve the engine body and existing valid state on resumed setups. Read it back and verify `enabled`, cadence/state fields, and the engine body. Neither step may modify `profile.md` or any other file in the same GitHub write.

Use a fresh content SHA for each existing file; one file per commit, followed immediately by a read-back from the intended repository and branch. Skip an already-correct file on resume. Never overwrite an existing personalized or non-empty ledger, surprise state, or historical Daily artifact to force setup forward. Report a blocker and request approval for a specific repair.

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

Confirm `profile.md` has all required approved configuration fields are populated, `github_repository` identifies the canonical runtime repository, `normal_location` / `region` are present as applicable, Calendar scope is present when applicable, and all referenced repository-relative vault/System/Daily/Action-Ledger paths are valid or clearly report any unresolved path issue. For a clean install that has not opted out, verify `daily_companion_extra.md` is enabled, has 104 valid ordered `weekly_due_dates` for consecutive complete Monday–Sunday weeks starting next week, and is configured for read-only Auto Mode; do not surface that date to the user. Reconfirm that each connected source listed in final `approved_data_sources` passed the applicable Section 4 preflight during this onboarding session; do not rely on a stale historical “verified” claim. If `ChatGPT surfaced conversation context` is listed, verify that the user explicitly approved it; no connector preflight or same-day conversation availability is required during setup. When Google Calendar is approved, verify that Calendar scope uses include-all-by-default semantics with only explicit exclusions stored. Do not claim setup is complete until the required runtime package is readable and the intended approved connected sources are verified. Confirm the configured `daily_folder` is a valid, writable location: the folder may not exist yet, but the first approved Daily Briefing or Daily Memory save must be able to create or use it; if there is any doubt, ask the user to create or confirm the folder before finishing setup.

After all the above read-only checks succeed, perform a **separate final single-file update** to `profile.md` setting `setup_complete: true`, changing no other approved settings. Fetch it again and confirm the exact saved flag and approved configuration. This flag means the *repository installation* is complete; it does **not** mean Scheduled Tasks exist or are enabled. If the final update or verification fails, installation remains unconfirmed and tasks must not be activated.

If `setup_complete: true` is found on a resumed or legacy install while state is incomplete, treat it as an inconsistent state: report it and ask before repairing it. Never infer completion from the flag alone.

Show a concise installation report distinguishing (1) profile configured, (2) state initialized, (3) repository verified and finalized, and (4) scheduled task activation pending/verified. Do not conflate these statuses.

## 9. Create Scheduled Tasks

Request explicit user confirmation to activate Scheduled Tasks after reporting verified repository readiness. Do **not** create Scheduled Tasks until the user confirms activation and the installation verification above has passed and connector preflight is satisfied for every connected source in final `approved_data_sources`. The configured GitHub repository must be readable and the approved setup commit must have proved interactive write access. Any approved Gmail, Google Calendar or other connected source that Morning/Evening will rely on must have passed its harmless read check. If a desired source remains blocked, let the user fix access and retry or explicitly revise the approved-source set; never silently create tasks that assume unavailable access.

Only after that separate activation confirmation, create three ongoing daily tasks using the timezone from `profile.md`:

- `Morning Companion` — exact-time daily at the approved Morning time.
- `Evening Companion` — exact-time daily at the approved Evening time.
- `Daily Companion Extra` — a daily **condition-watch** read-only check in the evening, using approximately 19:00 local unless the user explicitly requests another time. It stays silent unless Auto Mode is due exactly today.

Scheduled Task instructions are deliberately **minimal and stable**. Morning/Evening point to their workflow entrypoints; the extra check points directly to the canonical Surprise engine. The Morning prompt also carries one stable approval-handoff guardrail so an interactive `approve` reads the artifact policy before saving. Do not copy other evolving runtime rules into task prompts.

By Daily Companion design, all three Scheduled Tasks are read-and-output only and must not mutate the GitHub repository. Persistent repository writes happen only in an interactive turn after the applicable approval/authorization. Surprise weekly dates are generated during interactive setup and renewed during explicit interactive maintenance; the scheduled daily check never writes and no approval is needed to enable next week's planned delivery.

Use the actual configured `github_repository` and `system_folder` from `profile.md` when creating the tasks.

### Morning Companion task instruction

```text
Using GitHub repository `<github_repository>`, read `<system_folder>/workflows/morning.md` and run the Morning Companion exactly as instructed there.
Read files from that configured repository using the stated path; do not substitute a same-named file from another repository.

Interactive approval handoff: if the user later approves the generated Morning Briefing in this task conversation, immediately before any save read `<system_folder>/policies/artifacts.md` from the configured repository and execute its current Morning approval/save protocol. This includes the permitted save-time Calendar identity recovery/injection and required post-save verification, while preserving the approved user-visible Briefing exactly.
```

### Evening Companion task instruction

```text
Using GitHub repository `<github_repository>`, read `<system_folder>/workflows/evening.md` and run the Evening Companion exactly as instructed there.
Read files from that configured repository using the stated path; do not substitute a same-named file from another repository.
```

### Daily Companion Extra task instruction

```text
Using GitHub repository `<github_repository>`, read `<system_folder>/daily_companion_extra.md` and execute Auto Mode exactly as instructed there (read-only: never write any file). If Auto Mode stops silently, do not notify the user.
Read files from that configured repository using the stated path; do not substitute a same-named file from another repository.
```

These instruction patterns are part of the installation contract. If behaviour evolves, update the workflow/engine files rather than expanding the Scheduled Task prompts.

After creating the tasks, verify all three internally: title, enabled status, daily recurrence, local timing/timezone and correct entrypoint. Report only `Morning Companion` and `Evening Companion` to the user; do not announce the extra check or reveal hidden future Surprise dates.

If any task cannot be created or verified, state precisely that repository installation is complete but scheduled activation is incomplete; do not claim tasks are active. If Scheduled Task creation is unavailable in the current environment, provide the exact titles/schedules and stable entrypoint prompts so the user can create them elsewhere; do not pretend they were created.

## 10. Setup safety

- User permission and connector availability are separate; never treat one as proof of the other.
- Use read-only, least-invasive checks for access preflight; access testing must not mutate Gmail or Calendar.
- Never store volatile connector verification status, connector IDs or account secrets as if they were stable profile preferences. Verify access live during onboarding when needed.
- Never silently overwrite an existing initialized System folder.
- Re-onboarding changes only the settings/operational-state changes explicitly approved by the user; preserve unrelated existing configuration and state.
- Never erase Action Ledger active/Closed history as a side effect of setup changes.
- Never modify historical Daily Briefing or Daily Memory artifacts during setup.
- Never populate personal information into the clean policy/workflow/instruction files.
- Keep the entire clean bundle generic: examples, comments, migration fixtures and placeholder text must never copy real names, addresses, property identifiers, account details, exact personal amounts or other live user-state values.
- Keep user-specific configuration in `profile.md` and durable operational state/history in `action_ledger.md`.
