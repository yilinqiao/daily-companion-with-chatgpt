# Get started with Daily Companion

This repository is a **public, generic template**, not a place for your real life data.

## 1. Create your independent private vault

On the public source repository choose **Use this template → Create a new repository**. Choose **Private** visibility. Do **not** Fork this public repository for personal notes: public forks remain public. Ensure your copy contains System/setup.md and System/profile.md with setup_complete: false. Never publish your filled-in profile, daily notes or action ledger.

## 2. Connect ChatGPT

Connect the GitHub app in ChatGPT and give it access to the new private repository, not just this public source. Verify a read from the exact owner/repo. Reading does not prove that writes are permitted. Gmail and Google Calendar are optional and may be accessed only with your permission, followed by a harmless connector test.

Paste in ChatGPT:

    Read System/setup.md from GitHub repository <OWNER>/<PRIVATE_REPO> and begin Daily Companion onboarding, one question at a time. Do not write my files or create Scheduled Tasks until I approve the summary.

## 3. Complete setup

The streamlined setup asks about name, location/timezone, work pattern, language, communication style, approved information sources and Morning/Evening times together. Preferred-name usage defaults to occasionally; all Daily Flavour categories are enabled by default, with one rotating non-weather item in each Morning Briefing. Storage paths and Daily filenames use template defaults without extra questions. All defaults are disclosed for final approval; weather retrieval still requires permission. It must ask one question per turn. It must show a complete summary and receive explicit approval before writing. It updates System/profile.md with `setup_complete: false`, then initializes and reads back each state file through separate commits. Only after all required files and source checks pass should it set `setup_complete: true` in a final verified commit. If a write is blocked, stop and report which files are saved versus pending; do not work around a safety block.

## 4. Scheduling

Only after repository setup verification and a separate activation confirmation, set up the three Scheduled Tasks using the stable prompts in System/setup.md. Morning/Evening scheduled runs generate output only. They do not save Daily notes or update the Ledger: approve each intended save interactively and verify the committed file. If scheduled GitHub reads or notifications fail, use manual check-ins rather than claiming a task ran.

**One-time completion notification check:** after creating or reusing the tasks, go to **ChatGPT Settings > Notifications** and enable Scheduled Task Push and/or Email as desired; allow the app/browser permission on your device. Then open **Scheduled** (or **Settings > Notifications > Manage tasks**), inspect **Morning Companion**, **Evening Companion** and **Daily Companion Extra** separately, and enable **Notify when complete** for all three *if the switch is available*. This default prioritizes receiving a notification when Extra generates a Surprise. Its scheduled daily checks are intended to be silent before the due date, but some clients may still notify on no-output task completion. Try the default first; if ordinary checks generate unwanted alerts, review actual runs before revising the setup. If the switch is absent, use available notification controls. Ask for one confirmation and report each task as verified, user-confirmed, or unverified. Never assume task creation enabled notifications. Notifications do not verify GitHub writes or Daily approvals.

Surprise starts with one saved next_due_date in the week after setup. Daily Extra is silent before it, eligible on/after it, and chooses and verifies a date in the week after the attempt before the final response. No Python/hash or weekly approve; pause surprises pauses it. Activating Extra grants a narrow standing permission to update only its own engine scheduling/delivery fields. Morning/Evening remain read-only. Task creation and scheduled write verification are separate: report configured/enabled with persistence unverified until its actual due run demonstrates the writes. A pending claim blocks repeats and needs interactive recovery after interruption; see the engine's Interactive Controls and Recovery. Existing v5 copies require the approved migration and removal of the old read-only task-prompt clause through upgrade.md; do not rerun setup.

The blank-template CI check runs only in the public source repository. An initialized private copy automatically skips that job; the source template still rejects personal configuration and initialized state.

## 5. Obsidian is optional

Clone your private repo and open it as an Obsidian vault, using GitHub Desktop or Git on desktop. Kanban and Slurp are optional community plugins. On mobile, follow [the Obsidian/GitSync guide](../Resources/Obsidian%20GitHub%20GitSync%20Setup.md), including the shared-vault folder and verified sync steps. Test sync in both directions. Do not run two sync tools on the same vault simultaneously.

## First-use checklist

- Confirm System/profile.md belongs to the private repo and has no unresolved placeholders once setup completes.
- Confirm the Action Ledger has empty Action, Waiting, Upcoming and Closed lists before you add your own data.
- Run Morning manually and check Calendar/Gmail gaps are reported accurately.
- Approve a harmless Daily artifact and verify it exists in GitHub.
- Run Evening manually and verify that unobservable cross-chat topics are not fabricated.
- Confirm task names, timing/timezone and availability. For Morning, Evening and Extra, manually check `Notify when complete` when offered, ChatGPT Settings > Notifications (Push/Email), and device permission. Extra no-output daily runs may also alert in some clients; observe before refining. Do not assume a created task can notify you.

## Updates after setup

The current public template version is in root `VERSION`; [CHANGELOG.md](../CHANGELOG.md) describes each release. Your verified installed version/source commit are recorded in your private profile. New public releases do not automatically update that private copy.

Use [System/upgrade.md](../System/upgrade.md) for “check for updates” or “upgrade Daily Companion”. It compares a pinned source commit, preserves personal configuration, notes, Ledger/history and custom rules, and proposes any state migration before approved writes. Older copies without this file can use the public-entrypoint prompt in [README](../README.md#upgrade-an-existing-private-copy). No new onboarding is required just to update template rules.

Root `AGENTS.md`, maintenance docs and CI are copied intentionally. Public-release requirements apply to the canonical public repository; private personalization does not bump the upstream version or run the public blank-template gate. `.gitignore` excludes untracked temporary files, not files already included in the template.

## Troubleshooting

**Repo inaccessible:** recheck owner/repo and installation permissions. Never substitute this public template.
**Write unavailable:** stop at the failed stage; report the exact error, committed changes and pending changes. Do not mark setup complete or activate tasks until all required writes are independently read back and verified.
**Highlights missing:** ChatGPT cross-chat availability can be incomplete; add a missed topic manually.
**Duplicate obligations:** Closed/standing Ledger history prevents repeatedly treating the same already-handled obligation as new.
