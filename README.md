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
| Update Watch | Read-only VERSION check; optional release notes, separate interactive upgrade |

## Quick start

Open a new ChatGPT chat and select **High** thinking if available (otherwise use the strongest available thinking setting). Paste:

```text
Remind me to select High thinking if available. Help me connect GitHub in ChatGPT (if I have no account, help me sign up with Google). Use the GitHub connector to read System/setup.md from yilinqiao/daily-companion-with-chatgpt, then guide me through setup one question at a time. Do not invent questions. If the connector is unavailable, try the public repository files. If the setup text still cannot be read, stop and explain how to restore access; do not ask me to upload files. Ask for my approval before installation or scheduled task activation, separately.
```

Answer the questions about name, location, work schedule, the daily planning window (e.g. 07:00–21:00, including work), language, style, storage, optional sources and scheduled times. Only the setup instructions are needed to start; the assistant reads all required installation files and verifies access before requesting approval. After approval it installs directly using the retrieved files.

You can ask questions at any point during setup and resume where you left off. ChatGPT reads each required file with the GitHub connector and reuses complete content; public GitHub/Raw/Pages are fallback options. No user file upload, commit SHA, version-history check or manifest is required. If required rules cannot be read, pause before private writes and retain answers.

| | Notion (recommended) | Private GitHub + optional Obsidian |
| --- | --- | --- |
| Storage | One private Daily Companion Suite page with three independent databases: System, one shared Daily Companion source (Morning and Evening), and Action Ledger (Plan / tasks / projects) | Private repository containing Markdown |
| Morning | Auto-save with protected Notion-only Calendar ID section | Approve save; hidden Calendar metadata |
| Evening | Auto-save and show full provisional Memory in chat; approve revision of same page | Approve full Memory before any save |
| Ledger | Status board, unfiltered audit incl. Closed | Kanban Markdown board |
| Surprise | Read-only weekly pattern | Same read-only weekly pattern |
| Setup | [Sign up with Google](https://app.notion.com/signup) if needed; connect Notion and allow required operations on private suite | Use this template → Create a new repository → Private; never use public fork |

Notion users connect GitHub for public template reads only; no personal GitHub repository is needed. Connector availability and actual public read access must be tested. When ChatGPT requests permission to use Notion, **Always allow** is recommended if offered and you agree to ongoing access; installation, auto-save and task approvals remain separate. The setup creates and verifies private data sources and views where supported, or shows the missing connector operation and guides you through it. No cross-store failover. Calendar and Gmail are optional read-only sources; select one or multiple verified accounts where supported. Cross-chat context is incomplete and opt-in.

After verified setup, separately approve Scheduled Task activation. Recommended tasks: Morning, Evening, Extra and Update Watch. Confirm notification switches (Settings > Notifications, Notify when complete); silent Extra/Watch checks may still trigger platform alerts. First real scheduled run and persistence must be verified separately. If the connector or client lacks required capabilities, don't assume they work. See [Getting started](docs/GETTING_STARTED.md) or [setup guide](docs/setup-guide.html).

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

Say “Check for updates” for a read-only comparison, or “Upgrade Daily Companion” for an approved private upgrade. Read the latest public System/upgrade.md using the GitHub connector (or the [public upgrade guide](https://yilinqiao.github.io/daily-companion-with-chatgpt/upgrade.html) as fallback). Check updates with VERSION only; actual upgrades compare current file contents, without requiring historical commits or SHA verification. Preserve your profile, notes, Ledger, history and custom rules; publication never updates private copies automatically.

Public maintainers must read [AGENTS.md](AGENTS.md) and [System/maintenance.md](System/maintenance.md) before editing. Use a versioned PR and verified CI, never publish private state.

Community starter / experimental, not an official OpenAI, Notion or GitHub product. Scheduled delivery and complete source retrieval are not guaranteed.
