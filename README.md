# Daily Companion with ChatGPT

An open starter kit for a personal daily companion built with ChatGPT. **Notion is recommended**; a private GitHub repository with optional Obsidian is an alternative. Both use the same workflows and operational rules. Choose one private live store.

Current version: [VERSION](VERSION) · [Changes](CHANGELOG.md) · [Upgrade](System/upgrade.md).

The [public Pages mirror](https://yilinqiao.github.io/daily-companion-with-chatgpt/) is the default public reading entry: [Setup](https://yilinqiao.github.io/daily-companion-with-chatgpt/setup.html), [latest version](https://yilinqiao.github.io/daily-companion-with-chatgpt/version.html), [release notes](https://yilinqiao.github.io/daily-companion-with-chatgpt/changelog.html), [upgrade](https://yilinqiao.github.io/daily-companion-with-chatgpt/upgrade.html) and complete public System files. It is generated automatically from validated `main` releases; GitHub remains the canonical source and version history. Public GitHub file/Raw URLs, independently served jsDelivr public URLs and an optional connected GitHub connector are retrieval fallbacks; no user file uploads are needed for normal onboarding. No private data is hosted on Pages.

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
Remind me to select High thinking if available. Use web access to read the complete public System/setup.md at https://yilinqiao.github.io/daily-companion-with-chatgpt/setup.html . If that fails, try the Raw URL https://raw.githubusercontent.com/yilinqiao/daily-companion-with-chatgpt/main/System/setup.md , the GitHub public file page, then https://cdn.jsdelivr.net/gh/yilinqiao/daily-companion-with-chatgpt@main/System/setup.md . Follow the closed onboarding one question at a time. For installation, fetch all required files from public Pages bundle.html, individual Pages/Raw URLs or public CDN; verify the full contents. No GitHub connection or manual file download/upload required. Never invent missing rules. If every public source fails, report the missing public URLs and pause with answers retained; do not ask me to upload files. Ask for my approval before installation and separately before Scheduled Tasks.
```

Answer the questions about name, location, work schedule, the daily planning window (e.g. 07:00–21:00, including work), language, style, storage, optional sources and scheduled times. Only the setup instructions are needed to start; the assistant reads all required installation files and verifies access before requesting approval. After approval it installs directly using the retrieved files.

You can ask questions at any point during setup and resume where you left off. After the storage choice, ChatGPT should read the [public bundle](https://yilinqiao.github.io/daily-companion-with-chatgpt/bundle.html), relevant individual Pages files, or public GitHub Raw/CDN URLs itself. If browsing blocks every public route, the assistant must explain the missing source and pause; it must not ask you to download/upload repository files or invent missing rules.

| | Notion (recommended) | Private GitHub + optional Obsidian |
| --- | --- | --- |
| Storage | Private Daily Companion Suite with System, one shared Daily Companion source (Morning and Evening), and Ledger (Plan / tasks / projects) | Private repository containing Markdown |
| Morning | Auto-save with protected Notion-only Calendar ID section | Approve save; hidden Calendar metadata |
| Evening | Auto-save and show full provisional Memory in chat; approve revision of same page | Approve full Memory before any save |
| Ledger | Status board, unfiltered audit incl. Closed | Kanban Markdown board |
| Surprise | Read-only weekly pattern | Same read-only weekly pattern |
| Setup | [Sign up with Google](https://app.notion.com/signup) if needed; connect Notion and allow required operations on private suite | Use this template → Create a new repository → Private; never use public fork |

No personal GitHub repository or connector is needed for Notion; setup and update checks require reliable public template read access. Browser restrictions may still block a particular ChatGPT session. When ChatGPT requests permission to use Notion, **Always allow** is recommended if offered and you agree to ongoing access; installation, auto-save and task approvals remain separate. The setup creates and verifies private data sources and views where supported, or shows the missing connector operation and guides you through it. No cross-store failover. Calendar and Gmail are optional read-only sources; select one or multiple verified accounts where supported. Cross-chat context is incomplete and opt-in.

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

Say “Check for updates” for a read-only comparison, or “Upgrade Daily Companion” for an approved private upgrade. Older copies can start by reading the [latest public upgrade guide](https://yilinqiao.github.io/daily-companion-with-chatgpt/upgrade.html). Preserve your profile, notes, Ledger, history and custom rules; publication never updates private copies automatically.

Public maintainers must read [AGENTS.md](AGENTS.md) and [System/maintenance.md](System/maintenance.md) before editing. Use a versioned PR and verified CI, never publish private state.

Community starter / experimental, not an official OpenAI, Notion or GitHub product. Scheduled delivery and complete source retrieval are not guaranteed.
