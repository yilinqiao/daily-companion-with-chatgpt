# Daily Companion with ChatGPT

An open starter kit for a personal daily companion built with **ChatGPT, a private GitHub repository, and optionally Obsidian, Google Calendar, and Gmail**.

Current template version: see [VERSION](VERSION). See [release changes](CHANGELOG.md) and the [upgrade entrypoint](System/upgrade.md).

Daily Companion can help you preview your day, review your evening, maintain an action ledger, and keep approved daily notes. When the ChatGPT client supports it, Morning and Evening prefer a small interactive approval panel with separate choices for the daily note and proposed Ledger changes. A text approval fallback always remains available, and nothing is saved by merely showing or checking a box. Its instructions are plain Markdown files that you can inspect and change. **This public repository is a clean template. Do not put your personal data here.**

> **Privacy first:** Choose **Use this template → Create a new repository → Private**. **Do not Fork this public repository to store your personal information.** GitHub forks of public repositories are public, and their visibility cannot be changed independently.

## What it does

| Feature | Description |
| --- | --- |
| Morning Companion | A short, source-aware day briefing with calendar, mail, actionable follow-ups, and useful weather when enabled |
| Evening Companion | A conversational review that drafts a Daily Memory for your approval; includes tomorrow preparation and available same-day discussion highlights |
| Action Ledger | An Obsidian Kanban board tracking Action, Waiting, Upcoming, and Closed with lasting handling history |
| Daily Companion Extra | A random surprise each week from the week after setup; continues without approval until paused |
| Private vault | Your own independent private GitHub repository stores the configuration and Markdown notes |

## Quick start

1. Sign in to GitHub. On **this public template repository**, select **Use this template → Create a new repository**. Choose a new name and **Private** visibility. Do not include all branches or copy any Git history; the default branch is sufficient.
2. In ChatGPT, connect the GitHub app, granting it access to **your newly created private repository**. The app's availability and exact permissions depend on your account and connection settings.
3. Open a ChatGPT conversation and paste this (replace the placeholder):

   ```text
   Read System/setup.md from my GitHub repository <YOUR_USERNAME>/<YOUR_PRIVATE_REPOSITORY> and guide me through Daily Companion setup, asking only one question at a time. Do not change files or create scheduled tasks before I approve the summary.
   ```

4. Answer the streamlined onboarding questions. Preferred-name usage, Daily Flavour, vault folders and Daily filenames have editable defaults, so they are not asked separately. Morning includes one short rotating non-weather Daily Flavour item when enabled; weather requires source permission. Calendar and Gmail are **optional**. Grant each only if you want it used. ChatGPT must verify a source is accessible before treating it as connected.
5. Review the proposed configuration, then explicitly approve setup writes. ChatGPT commits the profile first with `setup_complete: false`, initializes and verifies each state file in a separate commit, and only then changes `setup_complete` to `true`. Confirm the post-write read-back checks for each file.
6. After the repository setup is verified, separately confirm whether to activate Scheduled Tasks. If supported, create/verify Morning, Evening and Extra checks according to `System/setup.md`. **After creating Morning, Evening and Extra, recommend `Notify when complete` for all three (where the client offers it), plus Settings > Notifications and device permissions.** Prioritize a notification when Extra actually generates a Surprise. Depending on the client, no-output daily Extra checks may also trigger completion alerts; test before adjusting. ChatGPT must not claim it automatically enabled a switch without verification. Morning/Evening are **read-and-output only**; note/action changes keep their interactive approval rules. Extra may update only its own scheduling state after explicit standing consent.
7. Optional: clone your **private** repository into Obsidian and configure desktop Git / mobile sync using [the Obsidian/GitSync guide](Resources/Obsidian%20GitHub%20GitSync%20Setup.md).

**Start without Obsidian:** ChatGPT can use the Markdown files in your private GitHub repository. Obsidian is an optional, useful editor, not a requirement for the first setup conversation.

## Prerequisites and limitations

- A GitHub account and a **private** repository generated from this public template.
- A ChatGPT account with a GitHub connection capable of reading and writing your own repository. Connector permissions must be confirmed in practice; some connections are read-only or limited to selected repositories.
- Scheduled Tasks, Gmail, Calendar, cross-chat context, and file writes may differ by ChatGPT plan, platform, runtime and permission. **Do not assume they work merely because they are described here.** If a capability is unavailable, follow the reduced-source/manual workflow; the setup must not claim success it cannot verify.
- Surprise stores one next_due_date in its private engine file. Setup chooses a date next week; daily Extra is silent before it and may deliver on/after it, select a date in the week after the delivery attempt, verify that save, then render the final response. No Python/hash or weekly approve. Extra needs private GitHub read/write access and explicit standing consent limited to its own state. An enabled task is not proof that scheduled writes work; report persistence unverified until observed. A claim-and-advance-before-final-output protocol reduces duplicate attempts, but interruption may miss output or need interactive recovery and notification receipt is not guaranteed.
- Automated chat runs cannot guarantee complete access to all previous conversations. Evening notes should disclose material gaps and ask you for missing details rather than inventing them.
- Version control is not a replacement for backup. Keep an independent backup of private personal information.

## Directory layout

```text
.
├── README.md
├── .gitignore
├── Daily/                       # approved daily notes (empty in public template)
├── Area/                        # optional personal notes (empty)
├── Projects/                    # optional personal notes (empty)
├── Resources/
│   └── Obsidian GitHub GitSync Setup.md
├── Archives/                    # optional personal notes (empty)
├── System/
│   ├── setup.md                  # first-run entry point
│   ├── profile.md                # unconfigured placeholder only
│   ├── instructions.md           # companion routing and boundaries
│   ├── action_ledger.md          # empty Kanban state
│   ├── daily_companion_extra.md  # surprise engine, no personal history
│   ├── workflows/
│   │   ├── morning.md
│   │   └── evening.md
│   └── policies/
│       ├── rules.md              # state and reconciliation semantics
│       └── artifacts.md          # approval and save contracts
└── docs/
    ├── GETTING_STARTED.md
    ├── PRIVACY.md
    └── RELEASE_REVIEW.md
```

## Example commands

**Morning:** `Run my Morning Companion using the configured private repository.`

**Evening:** `Run Evening Companion. Include meaningful things I explored in ChatGPT today only where reliable date evidence is available.`

**Save:** `Approve the displayed Daily Memory and save it to my configured private repository; verify the committed file.`

**Track an action:** `Add the confirmed follow-up to my Action Ledger as Waiting, then verify the GitHub write.`

## Safety model

The public template contains **no populated profile, actual personal ledger cards, daily notes, account IDs, credentials, personal emails, phone numbers, home addresses or private-vault URLs**. It contains only generic workflows and unfilled configuration placeholders. The GitHub owner and commit author name/email are separate public metadata and need their own privacy review. Publication should still be reviewed by the repository owner before going live; automated scans reduce risk but cannot guarantee that every type of personal information is detected.

Every personalized copy must be **private**. Never commit `.env` files, tokens, private keys or credentials. Never make your personalized repository public. Read [`docs/PRIVACY.md`](docs/PRIVACY.md) before enabling sync or sharing.

## Make the public source a template

After uploading this clean package to the public repository, the repository owner must open **Settings → General → Template repository** and enable the template option. Only then will visitors see **Use this template**. Test that a new private repository can be generated successfully.

## Maintain or customize

- Change stable preferences in your private `System/profile.md` after confirming those changes.
- Update reusable behavior in `System/instructions.md`, workflow files and policies, keeping role boundaries consistent.
- The Action Ledger is the single source of truth for operational state; approved Daily Memory is historical context, not evidence an action was completed.
- Saved daily notes must match the user-approved visible Markdown. Hidden metadata may be added only where expressly permitted by the artifact policy.
- New releases of this public template do **not** automatically update private copies. Review changes before selectively applying them.

### Upgrade an existing private copy

Say **“Check for updates”** for a read-only comparison, or **“Upgrade Daily Companion”** to prepare a specific upgrade through [System/upgrade.md](System/upgrade.md). It preserves configuration, notes, Ledger/history and custom rules; it shows proposed changes and migrations before applying an approved upgrade. `profile.md` records the verified installed template version and public-source baseline commit. Individual `schema_version` fields are separate data-format versions.

Older copies without that entrypoint can paste:

```text
Read System/upgrade.md from the public template repository
yilinqiao/daily-companion-with-chatgpt and help upgrade my private
Daily Companion repository <owner>/<private-repo>.
Show the version comparison and proposed changes before writing.
Preserve my configuration, notes, Ledger, histories and custom rules.
```

### Maintain the public template through Codex or GPT web

Follow root [AGENTS.md](AGENTS.md) and [System/maintenance.md](System/maintenance.md). Every public update includes a version bump, dated changelog entry and any required upgrade migration; CI checks version/release-note changes. For GPT web, start with:

```text
Before changing yilinqiao/daily-companion-with-chatgpt,
read AGENTS.md and System/maintenance.md and follow the release rules.
```

These files are intentionally included in template copies so users retain upgrade guidance. The maintenance rules distinguish the public source from a private vault; private settings/notes/customizations do not require an upstream release, and private copies skip public-template CI. `.gitignore` protects untracked secrets, caches and temporary upgrade files; it cannot exclude already tracked documentation from a GitHub template copy. Installed metadata and private notes remain tracked in the user's private vault by design.

A browser-friendly [HTML setup guide](docs/setup-guide.html) is also included. See [`docs/GETTING_STARTED.md`](docs/GETTING_STARTED.md) for the full onboarding path and troubleshooting, and [`docs/RELEASE_REVIEW.md`](docs/RELEASE_REVIEW.md) for the pre-publication checklist.

## Project status

Community starter / experimental. This is an independent personal workflow, **not an official OpenAI or GitHub product**. Review and adapt it for your account, privacy needs and available capabilities. No warranty of uninterrupted scheduled runs or complete source retrieval is made.
