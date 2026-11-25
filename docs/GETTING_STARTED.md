# Get started with Daily Companion

## 1. Start onboarding

Start a new ChatGPT chat with **High** thinking if available. Connect the GitHub plugin in ChatGPT. If you have no account, [sign up for free](https://github.com/signup) with Google if offered. The assistant reads the exact public `System/setup.md` from `yilinqiao/daily-companion-with-chatgpt` using the connector. Copy the prompt from the [README](../README.md). Notion users do not need a private GitHub repository. If the connector is unavailable, try reconnecting or the public GitHub file/Raw URL/Pages fallback. Never require file uploads, version/commit history verification, or a SHA to read the source.

Setup follows a closed questionnaire, one question at a time, including the full daily planning window (e.g. 07:00–21:00) separately from work hours, then language, communication style and storage. Ask questions at any point; resume from the unanswered question or current stage. Only the complete setup instructions are needed to start. Read all complete selected-backend files and verify private access before requesting installation approval; reuse the complete retrieved contents after approval without repeating approval for an unchanged plan. Missing release metadata alone does not block setup or an actual-file upgrade; missing required content pauses private writes.

## 2. Choose storage

**Notion (recommended):** no account yet? [Sign up for Notion](https://app.notion.com/signup) using your Google account. Then connect Notion in ChatGPT and grant the private suite the necessary full read/write and schema/view access. When "Allow ChatGPT to use Notion" appears, select **Always allow** if offered and you agree to ongoing access; this does not replace installation or scheduled task approval. Setup verifies access, requests approval, creates or reuses ONE private Daily Companion Suite parent page with exactly three independent databases: System, ONE shared Daily Companion source in its own database (Morning Briefing and Evening Memory separated by single-select Category), and Action Ledger, with saved views and read-back. No multi-data-source creation capability or manual construction of that layout is required. Existing installations keep their verified layouts. Plan means the separate Action Ledger task/project planning source. No additional Plan database is created. If the connector cannot create/verify views, setup guides you through the missing operation. You do not need a private GitHub repository.

**GitHub (alternative):** on the public source choose Use this template → Create a new repository → Private. Do not fork the public repository for personal information. Connect GitHub and allow read/write access to your private copy. Obsidian is optional, see the [GitSync guide](../Resources/Obsidian%20GitHub%20GitSync%20Setup.md). Setup verifies each approved private write.

Calendar, Gmail, web/weather and surfaced conversation context are optional and separately approved. Connect and verify each Gmail/Calendar account you want included; additional accounts require your approval. Connector read access must be tested before use.

## 3. Approve setup, then activate

Review the full setup summary and separately approve writes and Scheduled Tasks. The profile isn't marked complete until all required state/configuration is verified. Four tasks are recommended: Morning, Evening, Extra, Update Watch. Morning/Evening can run independently if prior notes are unavailable. Notion auto-saves initial Daily records; GitHub requires interactive saves. Both require separate approval for inferred Ledger changes. Extra is read-only and silent on non-eligible days on both backends.

For all three Morning/Evening/Extra, check **Notify when complete** under Scheduled or Settings > Notifications. Check device notification permissions. Watch uses the GitHub connector to check VERSION without requiring release notes or a commit SHA; failed public reads retry silently unless three consecutive daily failures are verifiable. A silent workflow does not guarantee no platform notification. Verify the first real run and actual saved record; an enabled task does not prove persistence. If access or task capacity is missing, report it and resolve before claiming full setup.

## 4. Daily use

Notion: Morning creates an initial briefing containing a final protected Calendar ID section only in Notion; Evening auto-saves a provisional Memory and displays the same full body in ordinary chat, followed by the three questions. Answer them, inspect the complete editable revised Memory, and approve it to update the same page. GitHub: inspect and approve Morning and Evening Markdown to save. Independent Ledger approval and text fallback are always available. Do not use provisional notes as confirmation.

**Pro tip: Edit Markdown directly.** When an editable Markdown preview is available, double-click a word to edit it yourself instead of asking ChatGPT to rewrite minor corrections. Review and approve the final edited version before saving. If ChatGPT cannot access your edits, paste the revised Markdown or describe the changes for a new preview.

Say “Check for updates” to compare VERSION using the GitHub connector, or “Upgrade Daily Companion” to compare the latest public System rules with your current private rules, then approve the concrete changes. No mandatory SHA or history check. No automatic private migration or dual writes. See [storage adapters](../System/storage/notion.md), [GitHub](../System/storage/github.md) and [privacy](PRIVACY.md).
