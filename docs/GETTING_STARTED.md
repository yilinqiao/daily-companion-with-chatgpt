# Get started with Daily Companion

## 1. Start onboarding

Use the public repository's System/setup.md, not a private copy of someone else's notes. Copy the prompt from the [README](../README.md). Setup asks one question at a time, including your personal planning window separately from work hours, then communication style and storage.

## 2. Choose storage

**Notion (recommended):** connect Notion in ChatGPT and grant the private suite the necessary full read/write and schema/view access. Setup verifies access, requests approval, creates or reuses the System, Daily Briefing & Memory, and Action Ledger data sources and their views, and checks read-back. If the connector cannot create/verify views, setup guides you through the missing operation. You do not need a private GitHub repository.

**GitHub (alternative):** on the public source choose Use this template → Create a new repository → Private. Do not fork the public repository for personal information. Connect GitHub and allow read/write access to your private copy. Obsidian is optional, see the [GitSync guide](../Resources/Obsidian%20GitHub%20GitSync%20Setup.md). Setup verifies each approved private write.

Calendar, Gmail, web/weather and surfaced conversation context are optional and separately approved. Connector read access must be tested before use.

## 3. Approve setup, then activate

Review the full setup summary and separately approve writes and Scheduled Tasks. The profile isn't marked complete until all required state/configuration is verified. Four tasks are recommended: Morning, Evening, Extra, Update Watch. Morning/Evening can run independently if prior notes are unavailable. Notion auto-saves initial Daily records; GitHub requires interactive saves. Both require separate approval for inferred Ledger changes. Extra is read-only and silent on non-eligible days on both backends.

For all three Morning/Evening/Extra, check **Notify when complete** under Scheduled or Settings > Notifications. Check device notification permissions. Watch notifications may be noisy on no-change checks. A silent workflow does not guarantee no platform notification. Verify the first real run and actual saved record; an enabled task does not prove persistence. If access or task capacity is missing, report it and resolve before claiming full setup.

## 4. Daily use

Notion: Morning creates an initial briefing containing a final protected Calendar ID section only in Notion; Evening creates a provisional Memory. Answer the three evening questions, inspect the full revised Memory, and approve it to update the same page. GitHub: inspect and approve Morning and Evening Markdown to save. Independent Ledger approval and text fallback are always available. Do not use provisional notes as confirmation.

Check for updates or ask to upgrade when desired. No automatic private migration or dual writes. See [storage adapters](../System/storage/notion.md), [GitHub](../System/storage/github.md) and [privacy](PRIVACY.md).
