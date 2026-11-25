---
type: companion-setup
schema_version: 3
---

# Daily Companion Setup

Recommend starting a new ChatGPT chat with Thinking set to High, if available; otherwise use the strongest available thinking setting. This is guidance, not a setup prerequisite.

## 0. Connect GitHub and read the setup

Use the **GitHub connector first** for the public template for BOTH storage choices. If not connected, guide the user to ChatGPT Settings > Plugins (or the GitHub connection offered in chat), and let them authorize GitHub themselves. If the user has no account, offer free [GitHub signup](https://github.com/signup) using their Google account if offered. Do not request credentials, tokens or verification codes. Notion users need only read access to the public repository, never a private GitHub repository or access to unrelated private repositories. Read the actual `System/setup.md` from `yilinqiao/daily-companion-with-chatgpt` on the current default branch (main) to confirm access; a repository name, search result or file preview is not a successful full read.

Start by reading the complete System/setup.md only. Do not require or check release metadata to start the conversation-only questionnaire (no private writes, connected-account reads other than the public template or task activation). Do not request VERSION, CHANGELOG, a commit SHA, tag, historical baseline, hash, manifest or release verification for ordinary source reads. If the connector is unavailable, help connect/reconnect; if the user declines or access is unavailable, try the public GitHub file/Raw URL or Pages as a simple fallback: https://yilinqiao.github.io/daily-companion-with-chatgpt/setup.html . Full source access, not a particular connection or metadata, is the prerequisite. Do not ask for file download/upload or pasted source. If Setup still cannot be read, retain answers and pause; do not invent questions. Never personalize the public source.

A new user can start with:

```text
Remind me to select High thinking if available. Help me connect GitHub in ChatGPT (if I have no account, help me sign up with Google). Use the GitHub connector to read System/setup.md from yilinqiao/daily-companion-with-chatgpt, then guide me through setup one question at a time. Do not invent questions. If the connector is unavailable, try the public repository files. If the setup text still cannot be read, stop and explain how to restore access; do not ask me to upload files. Ask for my approval before installation or scheduled task activation, separately.
```

## 1. Onboarding

This is a closed questionnaire: ask only the listed onboarding questions in order, the specified connector/setup/approval questions, and necessary clarifications of those fields. Adapt wording, not meaning. Do not add preference surveys (weekend activities, briefing topics, news, learning, fitness or long-term goals); do not turn defaults into questions. User-requested customization is separate from setup. Ask exactly one question per turn and wait for the answer. On resume or drift, use the verified setup (re-read if no longer available or known changed), preserve valid confirmed answers, ignore unrequested extra fields and continue with the next unanswered required question. Do not infer answers from connected sources. Explain defaults and obtain confirmation. If an existing installation is detected, preserve it and use upgrade.md; never reset or duplicate state. Do not preview surprise dates. Collect in this order:

Tell the user they may interrupt: the user may ask questions at any point. Answer their question, then return to the pending unanswered question or current setup stage unless they ask to pause. Never treat a clarification as an answer or installation approval.

1. Preferred name: What would you like me to call you?
2. Normal location: Where are you normally based? Resolve/confirm region and IANA timezone; weather_location defaults to normal_location.
3. Regular work schedule: fixed hours, variable shifts, or no regular schedule? For fixed, separately ask usual working days/hours. Never infer work times.
4. Daily planning window: From what time to what time would you like Daily Companion to help you plan your day? For example, 07:00–21:00. This covers the whole day, including work and before/after work, not just free time. Obtain an explicit local HH:MM start/end (start before end); store `planning_window_start` and `planning_window_end`, never default either to null. Only if the user explicitly declines planning suggestions, save both null. Fixed working hours and Calendar commitments still occupy time; all actual Calendar events are shown regardless of window. For variable/unknown shifts don't assume availability.
5. Output language: Which language should I normally use?
6. Communication style: How would you like the Companion to sound?
7. Storage choice: Would you like to use Notion (recommended) or GitHub? Explain Notion's auto-save, its combined Daily Companion source for Morning Briefing and Evening Memory, and separate Action Ledger vs private GitHub's interactive Markdown saves and optional Obsidian. If the user has no Notion account, offer signup with a Google account; guide them through setup/notion.md in §2. Follow only the selected onboarding guide. If GitHub selected, explain private template copy (never fork); if Notion chosen, explain the private parent/suite. Defer connection, creation and access checks to §2. No dual writes.
8. Optional sources, one topic per turn: Calendar/Gmail read permission (both, either, neither); web/weather permission; surfaced ChatGPT conversation context permission (only reliably dated/current surfaced material; no full-history guarantee). If the user wants captured pages included, identify and approve the exact private capture source and reliable capture-date field (defer any connector lookup to §2); otherwise skip it.
9. Schedule: What local times should Morning and Evening run? Suggest 08:00 and 20:00; confirm both times in separate questions.
10. Defaults (no questions): occasional name usage, all Daily Flavour categories enabled, one non-weather item/day, weather separately permission-gated; storage-specific defaults, Extra around 19:00, Update Watch 06:00. Show these in summary without revealing surprise dates.

## 2. Check connectors and approve setup

After storage choice, retrieve the complete contents of the selected installation guide, its required files and adapter before requesting installation approval and before any private installation write. Use the GitHub connector to read each required logical path from the canonical public repository's current default branch (main), including System/setup/notion.md and System/storage/notion.md for Notion or their GitHub equivalents. Reuse complete bodies already read in this setup; fetch only missing or invalidated content. Read exact files, not snippets, and report any missing path. If a connector read fails, retry that file or guide reconnection; use public GitHub file/Raw URL or Pages as fallback if accessible. Do not require the user to download/upload files, paste source content, or retrieve a commit identifier. No SHA, release history, manifest, metadata reconciliation or matching commit check is required to read/install; missing or inconsistent release metadata alone does not block setup. A known actual content conflict or missing required body must be resolved before private writes; no writes or task activation if required content remains unavailable. Preserve valid confirmed answers; resume only the pending step. Follow the selected guide to connect, identify the private destination and verify access. For Notion, proactively show the user-visible Always allow permission reminder in setup/notion.md before the first Notion connector call; repeat before the first approved write if the reminder has not already been acknowledged, including resumed setup. This is guidance, not a separate mandatory permission or approval question.

For each approved Gmail/Calendar service, ask whether to connect or include other accounts (one question per turn). Guide additional connections where supported. Let the user select accounts, verify each selected account's stable authenticated profile ID and the read below, and record only verified, explicitly approved IDs as quoted strings in the private `gmail_account_ids` / `calendar_account_ids` lists. Never store session tokens, credentials or verification codes. One account works identically; declined services use empty lists. Never silently include newly connected accounts. Show the selected accounts and any failed access in the final approval summary; verify coverage per account on the first real scheduled run.

### Google Calendar — only after user permission

- Perform a harmless read by enumerating calendars across each selected account. This access check and Calendar-scope discovery are the same operation.
- On success, collect exclusions here (this is the only place they are collected): present all visible calendars grouped by account, including primary, shared/family and contextual calendars such as holidays when visible. Explain that all calendars within approved accounts are included by default and ask: **"Which calendars, if any, would you like Daily Companion to exclude?"** Accept numbers, names or natural-language answers such as `none`. Record exclusions by stable calendar ID, not display name; newly visible calendars within approved accounts are included automatically unless excluded.
- On failure, do not infer scope or approve the failed account. Help connect/authorize and retry, or ask the user to explicitly continue with a reduced account scope.
- Never create/change Calendar events during setup merely to test access.

### Gmail — only after user permission

- On each selected account, perform a harmless metadata-level read such as listing Gmail labels (or an equivalently minimal read supported by the connector). Reading message content is not required merely to prove access.
- On failure, do not approve the failed account. Help connect/authorize and retry, or ask the user to explicitly continue with a reduced account scope.
- Never send, draft, archive, label, delete or otherwise modify mail during setup merely to test access.

### ChatGPT surfaced conversation context — only after user permission

- This is an optional runtime context source, not a connector that exposes or enumerates the user's complete ChatGPT history. There is no separate account-access preflight analogous to Calendar/Gmail.
- If the user approves it, record the exact source label `ChatGPT surfaced conversation context` in final `approved_data_sources`. If the user declines it, do not list it and Evening must not use cross-chat context for Daily Memory.
- Lack of surfaced cross-chat context during setup is not an access failure. Runtime availability is opportunistic: Evening may use only conversation context actually surfaced to that run and must follow its strict same-day timestamp/confirmation rules.
- Do not infer this permission from the user's ChatGPT Memory setting, project membership, account plan, or the mere fact that some conversation context happens to be available.

### Other connected sources

When the user approves another connected source that Morning/Evening will rely on, use the least-invasive available read to verify it before treating it as available. Sources such as web/weather that do not require a user account connector do not need account-access verification, though their use still requires whatever permission/configuration the runtime defines.

### Reduced-source setup

Google Calendar and Gmail are recommended, not mandatory. If the user explicitly declines either one, the system may continue in reduced-source mode because the runtime already handles unapproved sources conditionally. Do not include a declined or failed source in final `approved_data_sources`. If the user wants a source but its access check fails, pause that source's setup until they either fix access or explicitly revise their source choice. Never silently drop an intended source just to finish setup.


Verify selected storage access as specified by its onboarding guide; no unauthorized writes during preflight. User permission and connector capability are distinct. Show all configuration, selected private destination, required data sources/views or repository paths, source status, and planning window. Ask for explicit approval of actual setup writes including standing permission (record notion_daily_autosave_authorized true only after explicit consent) for Notion Morning/Evening initial auto-saves (only their own Daily pages); if declined, offer GitHub/manual flow or pause setup. In private profile persist the approved capture_source as backend, exact locator and reliable capture-date field; use null if declined/unconfigured. Keep optional Calendar/Gmail read-only. No public private data.

## 3. Initialize selected storage and verify readiness

After explicit installation approval, reuse the verified source contents and proceed directly without repeating approval unless the approved plan changes. Fetch only missing or invalidated public content on resume; if it cannot be recovered, pause, retain answers and approval for the unchanged plan, and make no further writes until resolved. Private destination checks and read-back remain required. Follow System/setup/notion.md or System/setup/github.md exclusively, with its selected runtime adapter. Save all approved settings in private profile; setup_complete false initially, true only after the selected backend's required verification of schema, state and destination. For Notion use the batch creation and efficient verification rules in setup/notion.md: create all missing System pages in one supported batch, reuse successful results and avoid routine per-page read-back comparisons. Read back essential Profile and Index configuration and resolve actual uncertainties before readiness. GitHub retains its own existing read-back requirements. Read the public VERSION once if available and record installed_template_version if reliably attributable to the installed source. installed_template_commit is optional provenance only; record it only if already returned as a reliable commit identifier by the connector, otherwise leave it null. Do not look up or verify a SHA for installation. Unknown markers may remain null without blocking readiness. For GitHub use the staged approved setup initialization in setup/github.md; for new Notion installations create ONE private Daily Companion Suite parent page with exactly three independent databases under it: System, ONE shared Daily Companion source in its own database for BOTH Morning Briefing and Evening Memory (single-select Category), and Action Ledger, with their views and index; initialize private Extra pattern. For Notion System page titles, remove the final `.md` suffix as specified in setup/notion.md, while preserving the canonical `.md` paths in the index. Apply the best-effort native cover and icon defaults in setup/notion.md during the existing create operations; appearance is not a readiness gate. Create each database through the normal connector operation; do not require adding multiple data sources to one database or ask the user to build that structure manually. Preserve an existing verified installation's layout and mappings; use upgrade.md for existing installations. Plan refers to the existing Action Ledger task/project planning source, not an additional database. Do not create a fourth Plan database; scheduled Ledger writes remain prohibited. If blocked, state exact pending stage and resume only after authorized repair; do not create duplicate data sources or tasks. Do not assume scheduled connector access is proven by interactive verification.

## 4. Activate Scheduled Tasks

After reporting verified readiness, obtain separate explicit task activation approval. Inspect existing tasks and reuse correct matches with same private destination/entrypoint. Do not duplicate, enable paused tasks, or claim enabled equals working. Recommended four tasks: Morning at confirmed time; Evening at confirmed time; Daily Companion Extra daily 19:00 local condition-watch; Daily Companion Update Watch daily 06:00 local condition-watch. Confirm actual time zones and schedules. Never combine Evening and Extra: each task has one fixed workflow identity. If slots are limited, ask the user which independent tasks to activate and report partial activation. Resolve the target local date from the scheduled occurrence, not delayed start time; do not write on an uncertain date. No dependency on successful earlier task: Morning reads prior Daily history/Ledger; Evening reads today's Morning snapshot if available; missing snapshot means use current evidence, not invent it. Extra and Watch run independently of either. Never run an automatic catch-up that overwrites a saved date.

For Notion, only with persisted autosave consent, initial Morning Briefing and Evening provisional Memory autosave are authorized scheduled writes; no Ledger or Calendar/Gmail writes. Verify first actual runs and page read-back; report scheduled persistence not yet verified until observed. For GitHub all scheduled runs remain read-only. For either backend, Extra and Update Watch never write. No fabricated pre-activation scheduled write test. If an intended scheduled capability is denied, stop that affected task and report; unrelated tasks may proceed after approval.

### Minimal task instruction patterns

Substitute actual private identifiers, never placeholders. Notion prompts pin exact private System instructions, profile and corresponding entrypoint page URLs; GitHub prompts pin exact private repository and configured System path. Resolve actual scheduled occurrence in profile timezone, not delayed start. Morning/Evening load current instructions/profile and selected workflow. Extra reads only engine/profile, Watch only upgrade watch/profile and public version metadata. No duplicate policy text, no public live storage.

### Morning Companion task instruction

Run Morning Companion from the configured private workflows/morning.md. Follow its current artifact and storage rules, including fresh-read before interactive writes. For a Notion installation, retry a transient initial workflow/System fetch at most twice after the first attempt; report the failed logical dependency and available error if exhausted, make no writes without verified required rules, and retain any safe draft. Once loaded, follow the Notion adapter recovery contract.

### Evening Companion task instruction

Run Evening Companion only from the configured private workflows/evening.md. Follow its current artifact and storage rules and the independent approval protocol, including fresh-read before interactive writes. On a successful Notion Auto-Saved initial Memory, display the entire verified user-visible body in ordinary chat, with the verified page URL/status outside it; if save fails or is unauthorized, show the full safe draft and an honest unsaved notice. GitHub Scheduled Evening remains read-only. For a Notion installation, retry a transient initial workflow/System fetch at most twice after the first attempt; report the failed logical dependency and available error if exhausted, make no writes without verified required rules, and retain any safe draft. Once loaded, follow the Notion adapter recovery contract.

**Mandatory ending for EVERY run, success AND failure:** After the complete Memory/check-in, all source/status/link notes, and any Closing Thought, the final user-visible section MUST ask all three required capture questions below, in the configured output language and in the exact order. This also applies after a successful full-body Notion Auto-Saved display, a long Memory, missing sources, or an unverified scheduled date. A generic invitation cannot replace any question. Always ask these three questions in the numbered list below, then add only one invitation to reply here:

1. What got done today that may not be visible in Calendar, Gmail or your saved notes?
2. Did anything new open, close, get cancelled, get scheduled, or otherwise change today that I may not know about?
3. Anything else from today worth capturing, including personal feelings or reflections?

Before sending, check the final lines for all three numbered questions; repair any omission. Do not add source/status notes or a sign-off after them. If the target date cannot be verified or required private instructions cannot be fetched, make no writes, report the issue briefly, retain any safe draft in this conversation and still ask all three questions. After answers, show a complete revised draft, invite reply, and seek independent approval before any Notion or Ledger write. Never execute Extra from this task.

### Daily Companion Extra task instruction

Fetch private daily_companion_extra.md and profile only; follow shared read-only Auto Mode. If Auto Mode stops silently, do not notify the user.

### Daily Companion Update Watch task instruction

Fetch private upgrade.md and profile; follow §0 Scheduled update watch (read-only). Use the GitHub connector to read the canonical public VERSION on the default branch; no commit SHA or CHANGELOG is required. Never upgrade on schedule.

### Task verification and notification handoff

Verify identifiers, schedule, enabled state, exact prompt and destination; list uncreated/paused/blocked tasks separately. Report first-run verification pending when actual execution cannot be observed. No-change checks are silent at workflow level, but platform alerts vary.

**First-run completion-notification handoff (after task creation, not an onboarding preference question):** Task activation, output, and notification delivery are separate outcomes. After creating or reusing any of Morning, Evening, Extra and Update Watch, give one checklist:
1. **Optional: ChatGPT mobile app.** If the user wants convenient mobile access and push notifications, suggest installing the official ChatGPT app on iOS or Android if not already installed, signing in to the same ChatGPT account and allowing mobile notification permission if desired. Users may skip this, keep using web/email, or do it later. It is not a setup completion or task activation requirement, and needs no separate onboarding question. In **ChatGPT Settings > Notifications**, enable Scheduled Task **Push**, **Email** or both as desired; allow device/browser notification permission.
2. In **Scheduled** (or **Settings > Notifications > Manage tasks**), inspect **Morning Companion**, **Evening Companion** and **Daily Companion Extra** separately. If `Notify when complete` exists, **recommend turning it on for all three, including Extra**. For **Daily Companion Update Watch**, enable update alerts where supported, but explain that completion notifications may also fire on no-change checks. Use actually visible alternative controls if the per-task switch is absent. Never claim ChatGPT automatically changed a switch unless a supported task control verifies that change.
3. Ask **one** confirmation after users check controls, not a new onboarding question per task. Record **notifications confirmed by user**, **verified from an available task setting**, or **not verified**, separately for each of the four tasks. Never infer this switch is enabled from task creation alone.

**Extra notification trade-off:** Extra uses a daily `condition-watch`. The Surprise engine is silent on a normal non-eligible check and renders content on an eligible date. Prioritize notification of a real Surprise. But `Notify when complete` is a platform setting: **do not promise suppression of no-op completion alerts**. Some ChatGPT clients may notify even on ordinary silent checks. Start with the switch enabled, observe actual runs, and if unwanted routine alerts occur, investigate before proposing a different setting or schedule. Do not disable Surprise notifications, modify its cadence state, or create duplicate tasks without an explicit follow-up decision. Completion alerts do not guarantee successful persistence, user approval, or delivery. Unsupported/unverified notification controls are a follow-up, not a reason to reset `setup_complete` or misreport activation.

If a task cannot be created or verified, report installation separately from **each task's** activation status. Update Watch must never be counted active based on a planned schedule alone. Its condition-watch targeting 06:00 may not execute at the exact minute, and platform notifications/no-op suppression must be verified in use. Verified Morning/Evening tasks may be reported active while Extra remains inactive; do not claim full activation or label an unverified task active. If Scheduled Task creation is unavailable, provide the exact titles/schedules and stable prompts for another supported environment; do not pretend tasks were created. Preserve the scheduled write boundaries and pending-persistence guidance.


## 5. Setup safety

No personal data in the public template, no duplicate live stores, no automatic Ledger changes, no bypass of permission blocks. Do not re-run completed setup to update rules; follow upgrade.md. Preserve all historical Daily records, ledger cards and custom preferences.
