# Get started with Daily Companion

This repository is a **public, generic template**, not a place for your real life data.

## 1. Create your independent private vault

On the public source repository choose **Use this template → Create a new repository**. Choose **Private** visibility. Do **not** Fork this public repository for personal notes: public forks remain public. Ensure your copy contains System/setup.md and System/profile.md with setup_complete: false. Never publish your filled-in profile, daily notes or action ledger.

## 2. Connect ChatGPT

Connect the GitHub app in ChatGPT and give it access to the new private repository, not just this public source. Verify a read from the exact owner/repo. Reading does not prove that writes are permitted. Gmail and Google Calendar are optional and may be accessed only with your permission, followed by a harmless connector test.

Paste in ChatGPT:

    Read System/setup.md from GitHub repository <OWNER>/<PRIVATE_REPO> and begin Daily Companion onboarding, one question at a time. Do not write my files or create Scheduled Tasks until I approve the summary.

## 3. Complete setup

The setup asks about normal location/timezone, work pattern, language, communication and preferred-name usage, optional extras and approved information sources, paths and Daily filenames, and Morning/Evening times. It must ask one question per turn. It must show a complete summary and receive explicit approval before writing. It updates System/profile.md with `setup_complete: false`, then initializes and reads back each state file through separate commits. Only after all required files and source checks pass should it set `setup_complete: true` in a final verified commit. If a write is blocked, stop and report which files are saved versus pending; do not work around a safety block.

## 4. Scheduling

Only after repository setup verification and a separate activation confirmation, set up the three Scheduled Tasks using the stable prompts in System/setup.md. Scheduled runs generate output only. They do not save Daily notes or update the Ledger: approve each intended save interactively and verify the committed file. If scheduled GitHub reads or notifications fail, use manual check-ins rather than claiming a task ran.

## 5. Obsidian is optional

Clone your private repo and open it as an Obsidian vault, using GitHub Desktop or Git on desktop. Kanban and Slurp are optional community plugins. On mobile, see Resources/Obsidian GitHub GitSync Setup.md. Test sync in both directions. Do not run two sync tools on the same vault simultaneously.

## First-use checklist

- Confirm System/profile.md belongs to the private repo and has no unresolved placeholders once setup completes.
- Confirm the Action Ledger has empty Action, Waiting, Upcoming and Closed lists before you add your own data.
- Run Morning manually and check Calendar/Gmail gaps are reported accurately.
- Approve a harmless Daily artifact and verify it exists in GitHub.
- Run Evening manually and verify that unobservable cross-chat topics are not fabricated.
- Confirm task names, timing/timezone and availability before relying on notifications.

## Troubleshooting

**Repo inaccessible:** recheck owner/repo and installation permissions. Never substitute this public template.
**Write unavailable:** stop at the failed stage; report the exact error, committed changes and pending changes. Do not mark setup complete or activate tasks until all required writes are independently read back and verified.
**Highlights missing:** ChatGPT cross-chat availability can be incomplete; add a missed topic manually.
**Duplicate obligations:** Closed/standing Ledger history prevents repeatedly treating the same already-handled obligation as new.
