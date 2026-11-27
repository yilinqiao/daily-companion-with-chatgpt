# Daily Companion with ChatGPT

An open starter kit for a personal daily companion built with ChatGPT. **Notion is recommended**; a private GitHub repository with optional Obsidian is an alternative. Both use the same workflows and operational rules. Choose one private live store.

Current version: [VERSION](VERSION) · [Changes](CHANGELOG.md) · [Upgrade](System/upgrade.md).

The public GitHub repository is the canonical source for all rules and version history. Connect GitHub in ChatGPT for setup, update checks and upgrades, whether you store your private companion in Notion or GitHub. A free account is sufficient when public repository read access is supported; [sign up](https://github.com/signup) using Google if offered. The [public Pages mirror](https://yilinqiao.github.io/daily-companion-with-chatgpt/) provides documentation and a fallback, not a required reading route. No public-template writes or private repository are needed for Notion.

| Feature | What it does |
| --- | --- |
| Morning | Calendar, email, follow-ups, weather, Sunday recap and grounded observations |
| Evening | Conversational check-in, Diary-first memory, three questions and user-approved revisions |
| Action Ledger | Action, Waiting, Upcoming, Closed; durable handling history |
| Extra | Weekly surprise, no weekly approval, pause anytime |
| Update Watch | Read-only VERSION check; concise changes and Update now option when newer |

## Quick start

Open a new ChatGPT chat and select **High** thinking if available (otherwise use the strongest available thinking setting). Paste:

```text
Remind me to select High thinking if available. Help me connect GitHub in ChatGPT (if I have no account, help me sign up with Google). Use the GitHub connector to read System/setup.md from yilinqiao/daily-companion-with-chatgpt, then guide me through setup one question at a time. Do not invent questions. If the connector is unavailable, try the public repository files. If the setup text still cannot be read, stop and explain how to restore access; do not ask me to upload files. Ask for my approval before installation or scheduled task activation, separately. Prefer ChatGPT's native Intelligent UI throughout onboarding whenever it improves the user experience. Use interactive choices, time selectors and confirmation controls where appropriate. At each setup question, show a compact current-stage header (e.g. Step 2 of 5 · Your Data Sources, 40%) and a thin five-segment progress bar when supported; avoid a full checklist or large progress card.
```

Setup follows five stages: About You → Your Data Sources → Your Storage → Your Daily Routine → Review & Launch. Answer the personal questions (including the whole-day planning window), then finish each optional data source's permissions, accounts and read-only checks, then choose/connect/verify storage, set Morning and Evening times, and review and launch. A compact stage header and progress bar show where you are. Only the setup instructions are needed to start; the assistant reads all required installation files and verifies access before requesting approval. After approval it installs directly using the retrieved files.

You can ask questions at any point during setup and resume where you left off. ChatGPT reads each required file with the GitHub connector and reuses complete content; public GitHub/Raw/Pages are fallback options. No user file upload, commit SHA, version-history check or manifest is required. If required rules cannot be read, pause before private writes and retain answers.

| | Notion (recommended) | Private GitHub + optional Obsidian |
| --- | --- | --- |
| Storage | One private Daily Companion Suite page with three independent databases: System, one shared Daily Companion source (Morning and Evening), and Action Ledger (Plan / tasks / projects) | Private repository containing Markdown |
| Morning | Auto-save with protected Notion-only Calendar ID section | Approve save; hidden Calendar metadata |
| Evening | Auto-save and show full provisional Memory in chat; approve revision of same page | Approve full Memory before any save |
| Ledger | Status board, unfiltered audit incl. Closed | Kanban Markdown board |
| Surprise | Read-only weekly pattern | Same read-only weekly pattern |
| Setup | [Sign up with Google](https://app.notion.com/signup) if needed; connect Notion; approve automatic private Suite creation and allow required operations on it (no existing page needed by default) | Use this template → Create a new repository → Private; never use public fork |

Notion users connect GitHub for public template reads only; no personal GitHub repository is needed. Connector availability and actual public read access must be tested. Before Notion setup begins, ChatGPT reminds you that if the “Allow ChatGPT to use Notion?” popup appears, select **Always allow** (usually the leftmost button) rather than Allow once, if offered and you agree to ongoing access. This helps reduce repeated permission prompts; installation, auto-save and task approvals remain separate. The setup creates and verifies private data sources and views where supported, batches System page creation in one supported call, and reuses successful results instead of repeatedly reading every page. It checks essential configuration and unresolved items, or explains any missing connector operation. New Notion pages use the [full-resolution sunrise-lake cover](assets/daily-companion-cover.png) and native icons where supported; appearance is optional and does not block installation. No cross-store failover. Calendar and Gmail are optional read-only sources; select one or multiple verified accounts where supported. Cross-chat context is incomplete and opt-in.

After verified setup, separately approve Scheduled Task activation. Recommended tasks: Morning, Evening, Extra and Update Watch. Optional: install the official ChatGPT mobile app (iOS or Android), sign in to the same account and allow mobile notifications if desired. The app is not required for setup or task activation. Confirm notification switches (Settings > Notifications, Notify when complete); silent Extra/Watch checks may still trigger platform alerts. First real scheduled run and persistence must be verified separately. If the connector or client lacks required capabilities, don't assume they work. See [Getting started](docs/GETTING_STARTED.md) or [setup guide](docs/setup-guide.html).

## Privacy

This public repository contains only generic templates. Never write personal details into it. A GitHub personal copy must be private (not a public fork); Notion personal pages and IDs must remain private. See [Privacy](docs/PRIVACY.md). No credentials in profile files or public commits.

## Directory and core rules

- [Setup](System/setup.md), [profile](System/profile.md), [instructions](System/instructions.md)
- [Notion adapter](System/storage/notion.md), [GitHub adapter](System/storage/github.md)
- Onboarding only: [Notion installation](System/setup/notion.md), [GitHub installation](System/setup/github.md)
- [Morning](System/workflows/morning.md), [Evening](System/workflows/evening.md)
- [Shared operational rules](System/policies/rules.md), [artifact/approval rules](System/policies/artifacts.md)
- [Extra](System/daily_companion_extra.md), [upgrade](System/upgrade.md)
- [Obsidian GitSync guide](Resources/Obsidian%20GitHub%20GitSync%20Setup.md) (GitHub alternative only)

The Action Ledger is authoritative for operational state; daily notes are historical context, never evidence of completion by themselves. Notion's provisional notes are not user confirmed. No scheduled Ledger mutation. Independent approval for inferred changes. Notion only permits initial Daily auto-save with consent; revisions and other writes require explicit approval. GitHub uses interactive note saves.

## Maintain or customize

**Getting started.** Try your first Morning and Evening runs, reply to Evening's questions and check notifications and actual saved records according to your storage choice. If a Scheduled Task repeatedly skips required tool calls while the connectors and the same workflow work in regular chat, try pausing the affected task and recreating it with the same verified prompt, schedule and timezone. Check notification settings and observe a real run. This is an optional troubleshooting step, not a proven fix; preserve the old task/history and avoid two active copies. Never recreate tasks automatically or without approval.

**Make it your own.** Tell ChatGPT what to add, remove or change over time. For example, ask it to summarize relevant newsletters in your Morning Briefing (with approved Gmail access), adjust the length or tone, reflect on patterns in saved Daily Memories, look up past records or give Surprise style feedback. ChatGPT can propose and apply approved changes to your private System rules; no need to edit code.

**Good to know.** Once Daily Companion is running reliably, you may delete the optional 06:00 Daily Companion Update Watch in Scheduled to free a task slot; the other three tasks are independent. You can still say “Check for updates” anytime, read a short summary and choose Update now while preserving your customizations. When an editable Markdown preview is available, double-click text to make small edits, then review and approve the final version before saving.

**You don't need to get everything perfect during setup. Your Daily Companion can evolve with you.**

Say “Check for updates” for a read-only version check and short summary of available changes, then choose Update now (or reply with the version). ChatGPT handles file comparison; exceptional changes need specific approval. Read the latest public System/upgrade.md using the GitHub connector (or the [public upgrade guide](https://yilinqiao.github.io/daily-companion-with-chatgpt/upgrade.html) as fallback). Check VERSION first; read release notes only when newer. Actual upgrades compare current file contents internally, without requiring historical commits or SHA verification. Preserve your profile, notes, Ledger, history and custom rules; publication never updates private copies automatically.

Public maintainers must read [AGENTS.md](AGENTS.md) and [System/maintenance.md](System/maintenance.md) before editing. Use a versioned PR and verified CI, never publish private state.

Community starter / experimental, not an official OpenAI, Notion or GitHub product. Scheduled delivery and complete source retrieval are not guaranteed.
