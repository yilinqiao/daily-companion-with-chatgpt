# Get started with Daily Companion

## 1. About You

Start a new ChatGPT chat with **High** thinking if available. Connect the GitHub plugin in ChatGPT. If you have no account, [sign up for free](https://github.com/signup) with Google if offered. The assistant reads the exact public `System/setup.md` from `yilinqiao/daily-companion-with-chatgpt` using the connector. Copy the prompt from the [README](../README.md). Notion users do not need a private GitHub repository. If the connector is unavailable, try reconnecting or the public GitHub file/Raw URL/Pages fallback. Never require file uploads, version/commit history verification, or a SHA to read the source.

Setup prefers native Intelligent UI when useful (interactive choices, time selectors and confirmation controls). Setup follows a closed questionnaire, one question at a time, including the full daily planning window (e.g. 07:00–21:00) separately from work hours, then language and communication style. A compact stage header and progress bar show your current stage. Ask questions at any point; resume from the unanswered question or current stage. Only the complete setup instructions are needed to start. Read all complete selected-backend files and verify private access before requesting installation approval; reuse the complete retrieved contents after approval without repeating approval for an unchanged plan. Missing release metadata alone does not block setup or an actual-file upgrade; missing required content pauses private writes.

## 2. Your Data Sources

Calendar, Gmail, web/weather and surfaced conversation context are optional and separately approved. Connect and verify each Gmail/Calendar account you want included; additional accounts require your approval. Connector read access must be tested before use. Finish Calendar (select which calendars to include), then Gmail, then web/weather and surfaced conversation context. Complete each source before moving on.

## 3. Your Storage

**Notion (recommended):** no account yet? [Sign up for Notion](https://app.notion.com/signup) using your Google account. Then connect Notion in ChatGPT. No existing parent page or page link is needed by default: after approval ChatGPT creates the private workspace-level Suite and obtains the necessary scoped read/write and schema/view access. Before the first Notion tool call, ChatGPT reminds you: when "Allow ChatGPT to use Notion?" appears, select **Always allow** (usually the leftmost button) rather than Allow once, if offered and you agree to ongoing access. This helps avoid repeated permission prompts; it does not replace installation, auto-save or scheduled task approval. Setup verifies access, requests approval, creates or reuses ONE private Daily Companion Suite parent page with exactly three independent databases: System, ONE shared Daily Companion source in its own database (Morning Briefing and Evening Memory separated by single-select Category), and Action Ledger, with saved views and essential verification. System pages are created in one supported batch; successful creation results are reused instead of routine per-page full-body read-back. Essential Profile/Index checks and unresolved items are verified before activation. The Suite uses the full-resolution sunrise-lake cover and native icons where supported, with ☀️ Morning and 🌙 Evening records. Database icons use at most one combined parent-page update. Decoration is optional and needs no extra checks. No multi-data-source creation capability or manual construction of that layout is required. Existing installations keep their verified layouts. Plan means the separate Action Ledger task/project planning source. No additional Plan database is created. If the connector cannot create/verify views, setup guides you through the missing operation. You do not need a private GitHub repository.

**GitHub (alternative):** on the public source choose Use this template → Create a new repository → Private. Do not fork the public repository for personal information. Connect GitHub and allow read/write access to your private copy. Obsidian is optional, see the [GitSync guide](../Resources/Obsidian%20GitHub%20GitSync%20Setup.md). Setup verifies each approved private write.

## 4. Your Daily Routine

Confirm Morning and Evening local times separately. Extra and Update Watch retain their existing defaults.

## 5. Review & Launch

Review the full setup summary and separately approve writes and Scheduled Tasks. The profile isn't marked complete until all required state/configuration is verified. Four tasks are recommended: Morning, Evening, Extra, Update Watch. Morning/Evening can run independently if prior notes are unavailable. Notion auto-saves initial Daily records; GitHub requires interactive saves. Both require separate approval for inferred Ledger changes. Extra is read-only and silent on non-eligible days on both backends.

Optional: install the official ChatGPT mobile app (iOS or Android) if you want mobile access and push notifications. Sign in to the same account and allow mobile notifications if desired; skip if you prefer web/email or already have the app. The app is not required for setup or task activation. For all three Morning/Evening/Extra, check **Notify when complete** under Scheduled or Settings > Notifications. Check device notification permissions. Watch uses the GitHub connector to check VERSION and, if newer, summarizes available release notes and offers Update now; failed public reads retry silently unless three consecutive daily failures are verifiable. A silent workflow does not guarantee no platform notification. Verify the first real run and actual saved record; an enabled task does not prove persistence. If access or task capacity is missing, report it and resolve before claiming full setup.

## After setup

**Getting started.** Try your first Morning and Evening runs, reply to Evening's questions and check notifications and actual saved records according to your storage choice.

**Make it your own.** Tell ChatGPT what to add, remove or change over time. For example, ask it to summarize relevant newsletters in your Morning Briefing (with approved Gmail access), adjust the length or tone, reflect on patterns in saved Daily Memories, look up past records or give Surprise style feedback. ChatGPT can propose and apply approved changes to your private System rules; no need to edit code.

**Good to know.** Once Daily Companion is running reliably, you may delete the optional 06:00 Daily Companion Update Watch in Scheduled to free a task slot; the other three tasks are independent. You can still say “Check for updates” anytime, read a short summary and choose Update now while preserving your customizations. When an editable Markdown preview is available, double-click text to make small edits, then review and approve the final version before saving.

**You don't need to get everything perfect during setup. Your Daily Companion can evolve with you.**

## Daily use

Notion: Morning creates an initial briefing containing a final protected Calendar ID section only in Notion; Evening auto-saves a provisional Memory and displays the same full body in ordinary chat, followed by the three questions. Answer them, inspect the complete editable revised Memory, and approve it to update the same page. GitHub: inspect and approve Morning and Evening Markdown to save. Independent Ledger approval and text fallback are always available. Do not use provisional notes as confirmation.

**Pro tip: Edit Markdown directly.** When an editable Markdown preview is available, double-click a word to edit it yourself instead of asking ChatGPT to rewrite minor corrections. Review and approve the final edited version before saving. If ChatGPT cannot access your edits, paste the revised Markdown or describe the changes for a new preview.

Say “Check for updates” to check VERSION, see a short summary of available changes and choose Update now or reply with the version. ChatGPT compares private and public rules internally; only exceptional changes need separate approval. No mandatory SHA or history check. No automatic private migration or dual writes. See [storage adapters](../System/storage/notion.md), [GitHub](../System/storage/github.md) and [privacy](PRIVACY.md).
