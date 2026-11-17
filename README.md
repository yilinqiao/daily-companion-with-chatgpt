# Daily Companion with ChatGPT

An open starter kit for a personal daily companion built with ChatGPT. **Notion is recommended**; a private GitHub repository with optional Obsidian is an alternative. Both use the same workflows and operational rules. Choose one private live store.

Current version: [VERSION](VERSION) · [Changes](CHANGELOG.md) · [Upgrade](System/upgrade.md).

| Feature | What it does |
| --- | --- |
| Morning | Calendar, email, follow-ups, weather, Sunday recap and grounded observations |
| Evening | Conversational check-in, Diary-first memory, three questions and user-approved revisions |
| Action Ledger | Action, Waiting, Upcoming, Closed; durable handling history |
| Extra | Weekly surprise, no weekly approval, pause anytime |
| Update Watch | Read-only public release check, optional interactive upgrade |

## Quick start

Paste into ChatGPT:

```text
Read System/setup.md from yilinqiao/daily-companion-with-chatgpt and guide me through Daily Companion setup, one question at a time. Do not write personal data or activate tasks until I approve the respective summary.
```

Answer the questions about name, location, work schedule, personal planning hours (including before/after work), language, style, storage, optional sources and scheduled times. Setup will guide connector access, summarize and request approval before creating the private installation.

| | Notion (recommended) | Private GitHub + optional Obsidian |
| --- | --- | --- |
| Storage | Private Daily Companion Suite with System, Daily and Ledger databases/views | Private repository containing Markdown |
| Morning | Auto-save with protected Notion-only Calendar ID section | Approve save; hidden Calendar metadata |
| Evening | Auto-save provisional Memory; approve revision of same page | Approve full Memory before any save |
| Ledger | Status board, unfiltered audit incl. Closed | Kanban Markdown board |
| Surprise | Read-only weekly pattern | Same read-only weekly pattern |
| Setup | Connect Notion and allow required read/create/update/query/schema/view operations on private suite | Use this template → Create a new repository → Private; never use public fork |

No personal GitHub repository is needed for Notion, but setup and update checks need read access to the public template. The setup creates and verifies private data sources and views where supported, or shows the missing connector operation and guides you through it. No cross-store failover. Calendar and Gmail are optional read-only sources; cross-chat context is incomplete and opt-in.

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

Say “Check for updates” for a read-only comparison, or “Upgrade Daily Companion” for an approved private upgrade. Preserve your profile, notes, Ledger, history and custom rules; publication never updates private copies automatically.

Public maintainers must read [AGENTS.md](AGENTS.md) and [System/maintenance.md](System/maintenance.md) before editing. Use a versioned PR and verified CI, never publish private state.

Community starter / experimental, not an official OpenAI, Notion or GitHub product. Scheduled delivery and complete source retrieval are not guaranteed.
