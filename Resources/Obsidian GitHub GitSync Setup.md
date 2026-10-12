# Obsidian + GitHub + GitSync Setup

Use this guide to connect optional Obsidian devices to **your existing private Daily Companion repository**. You can complete ChatGPT setup and use Daily Companion before installing Obsidian. The current template version is in [VERSION](../VERSION); release changes are in [CHANGELOG.md](../CHANGELOG.md).

**Already finished setup?** Keep your repository and saved state. Start at Section 3 for device sync, or Section 7 for a template upgrade. Do not create another template copy or rerun onboarding merely to add Obsidian.

## Architecture

```text
Public Daily Companion template
        |
        | Use this template (once)
        v
Your independent PRIVATE GitHub repository
        |                         |
        | GitHub connection       | Git pull / commit / push
        v                         v
     ChatGPT                Local Obsidian vaults
                       Desktop Git / mobile GitSync
```

GitHub holds the shared remote files and history; devices edit local copies. ChatGPT reads GitHub directly, so a phone need not be online for that repository access. Its supported tools and permissions still need verification. GitSync moves files between a mobile device and the same private remote; it does not perform ChatGPT setup or upgrade the template.

Fetch lets you inspect incoming commits; pull brings them into the local working copy. A commit saves a local snapshot, while push uploads it. Wait for the complete sync/pull result before treating local files as current.

Morning/Evening scheduled runs produce previews; note and Ledger saves follow their interactive authorization rules. After explicit standing consent, **Extra alone** may update its own engine's scheduling/attempt fields. It cannot write other notes, the profile, Ledger, Gmail or Calendar. See [setup](../System/setup.md) and the [Surprise engine](../System/daily_companion_extra.md) for the exact scope.

## 1. Create the private copy once

1. Open the [public template](https://github.com/yilinqiao/daily-companion-with-chatgpt).
2. Choose **Use this template → Create a new repository**, select your intended owner, choose a name, and set visibility to **Private**. Copy only the default branch.
3. Check your new repository contains the root package files and the System/Daily/Resources folders. Template creation supplies the starter files; you do not need a separate empty repo plus a manual Starter upload.
4. Keep the repository root as the vault root unless your approved profile uses another layout. Use that same owner/repository and default branch in ChatGPT and each Git client; preserve a different branch only if your existing installation explicitly targets it. Do not switch branches to bypass a sync conflict.

Keep personal configuration and notes only in the private copy, never in the public template or a public fork. Template copies have independent histories; see [GitHub's template instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template). The source's blank-template CI is deliberately skipped in private copies; a skipped job does not validate personal data or prove runtime readiness.

## 2. Finish ChatGPT setup before optional device sync

Connect the GitHub app in ChatGPT to the account that can access **this private repository**. A GitSync or desktop login does not switch the ChatGPT connection. Check the exact owner/repository and verify access to its setup file; public-template read access does not establish private write access.

For a new installation, paste this in ChatGPT:

```text
Read System/setup.md from my GitHub repository <OWNER>/<PRIVATE_REPO>
and guide me through Daily Companion setup, asking one question at a time.
Do not change files or create scheduled tasks before I approve the summary.
```

Follow the approved setup stages:

1. Answer the onboarding questions and choose optional data sources. ChatGPT verifies approved connector access before treating it as available.
2. Review the summary, including repository, paths, timezone and preferences; approve the concrete setup writes.
3. Verify the saved profile with setup_complete still false, then verify Ledger and Extra initialization through their separate commits. A new Extra stores one chosen next_due_date in the week after setup, not a seed or future-date list.
4. After package/state checks and any provisional-date alignment, verify the final profile commit with setup_complete true and the installation version/baseline markers when known. This verifies installation, not task activation.
5. Separately confirm activation. Morning/Evening keep their read-only scheduled boundary. Extra requires explicit consent to update only its own scheduling state; connector availability alone is not consent. Reuse matching existing tasks and preserve paused choices.

Extra compares the saved date daily: earlier means silence; on/after it, an eligible run reserves an attempt, verifies the next week's date save, then sends the final surprise. No Python/hash test or weekly approve is required. Task enabled status is separate from actual scheduled persistence and notification settings; check the first due run before claiming the entire path works. A pending claim stops automatic repeats and needs the engine's interactive recovery. Do not manually clear claims or redraw dates to make setup pass.

If you already completed setup, preserve it and use the upgrade flow when old instructions need updating. Obsidian installation never requires resetting the profile, Ledger or Surprise state.

## 3. Desktop Obsidian (Windows / macOS)

1. Install Obsidian and GitHub Desktop or use your existing Git client.
2. Clone **your private repository**, using the branch used by ChatGPT. Choose an ordinary local folder outside other live cloud-sync folders, so two systems do not synchronize the same working copy.
3. In Obsidian, open that cloned folder as a vault; respect any configured vault subfolder. Do not create a second blank vault and copy template files over an initialized one.
4. Install Kanban if you want a visual Action Ledger, and Slurp if you want its clipping workflow. Both are optional community plugins; plain Markdown remains usable.
5. Fetch/pull before editing. Save locally, inspect changes, commit and push when finished, then confirm GitHub shows your changes. Desktop GitHub Desktop/manual Git does not automatically sync merely because Obsidian was opened.

If this device already has the correct checkout/vault, verify its private remote and branch, then reuse it and pull changes. Do not clone over an existing vault or copy a new template into it.

If you later add desktop Git automation, use one coordinator for that working copy. Keep overlapping manual/background sync operations from running together. Git is the selected sync route for this guide; avoid simultaneously syncing the same folder through Obsidian Sync, iCloud, OneDrive or another service. [Obsidian's sync guidance](https://help.obsidian.md/sync-notes) explains the local-vault model and conflicts from mixed services.

## 4. Android Obsidian + GitSync

Use [GitSync by ViscousPotential](https://gitsync.viscouspotenti.al/wiki/), not a similarly named plugin/service.

1. Install Obsidian and GitSync. Authenticate GitSync with the account allowed to access your private repository.
2. Clone that repository/branch into a local folder Obsidian can access. Open that **same** folder as the vault. GitSync may require Android's broader **All files access** permission; review it before granting access. See its [Android file-access guide](https://gitsync.viscouspotenti.al/wiki/all-files-access).
3. Run a manual sync and inspect the result before enabling automation. Confirm the expected profile and Ledger appear; do not edit them as a sync test.
4. For optional app-based sync, select Obsidian in GitSync and configure open/close triggers. This uses its Android Accessibility Service; manual sync remains available if you choose not to enable it. Follow the [author's App Sync instructions](https://gitsync.viscouspotenti.al/wiki/sync-options/background/app-based).

Wait for sync to finish before editing or switching devices. An app-open trigger is not proof that a pull has completed. Inspect failed/conflicted syncs rather than assuming the automation worked. Disable other mobile Git automation for this vault.

## 5. iPhone / iPad Obsidian + GitSync

The apps must operate on the **same Obsidian-accessible vault folder**, not two separate Files copies. Follow the [author's iOS clone instructions](https://viscouspotenti.al/posts/gitsync-all-devices-tutorial#setting-up-gitsync):

1. In Obsidian, create a **new empty local vault**, with iCloud storage off for this Git-only route. This is a local destination for the existing private repo, not a second GitHub repository.
2. In GitSync, authenticate and select your existing private repository/branch.
3. Use the direct-clone option into that new vault under the device's Obsidian folder. If asked to replace files, confirm only that new empty vault's default files; stop if the prompt refers to existing personal notes or another vault. Do not clone elsewhere and assume Obsidian can open every arbitrary Files folder.
4. Return to that vault in Obsidian and confirm the repository files are present. Run and verify one manual GitSync sync.
5. In Shortcuts, create a shortcut using GitSync's **Sync Now** action. Set GitSync's selected/default repository to this vault.
6. Add Obsidian-open and Obsidian-close automations that run that shortcut, using **Run Immediately** when available. Test both triggers; app-version UI labels may vary. See [GitSync's Shortcuts instructions](https://gitsync.viscouspotenti.al/wiki/sync-options/background/app-based).

If this device already has the correct GitSync-linked vault, reuse it after verifying remote/branch/folder; do not create another local vault. Keep other sync automation off for this vault. Check completion manually before switching devices; background triggers are not a guarantee of instantaneous synchronization.

## 6. Keep the template's ignore rules and sync current state

Keep the existing root [.gitignore](../.gitignore), rather than replacing it with a shorter device-only example. It excludes local Obsidian settings/cache, credentials, Python cache, upgrade scratch files and backups. Because .obsidian is excluded, install/configure optional plugins separately on each device.

Profile, Ledger, Extra state and approved Daily notes **must remain tracked in your private repo** so ChatGPT and your devices see the same state. Ignoring them would break that shared storage. [Git's ignore rules](https://git-scm.com/docs/gitignore) apply to untracked files; they do not remove already committed template files, prevent connector writes or turn public data private. Never store tokens or keys in the vault.

Use your preferred commit identity and consider the GitHub-provided noreply email in each Git client's author settings; commit metadata is separate from app sign-in. See [GitHub's commit-email guidance](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

For normal use:

- Before editing: pull/sync, wait for completion, and inspect any incoming changes. Fetch alone does not update the local vault.
- After editing: save, commit/push or run GitSync sync, then verify the remote result before continuing on another device.
- After a ChatGPT save: verify the private GitHub commit first, then pull it to Obsidian. A generated preview is not a saved note.
- Extra can change its own state even when no Daily note was saved. Pull/sync current state before any engine edit; use ChatGPT's interactive pause/resume/recovery controls instead of editing its dates or claims casually.
- With conflicts: stop automatic sync, preserve both versions, inspect differences and resolve deliberately. For an Extra claim/state conflict, use its recovery contract and task-run evidence; never blindly choose an old local copy, clear a claim, restore blank template state or force-push. [GitSync conflict instructions](https://gitsync.viscouspotenti.al/wiki/merge-conflict-resolution) cover its conflict UI.
- Keep independent backups. Git history and device sync are useful recovery aids, not a guarantee that every local edit was uploaded.

## 7. Upgrade the existing private copy

GitSync synchronizes your private repository with its devices. It does **not** synchronize that repo with newer public-template releases.

Use [System/upgrade.md](../System/upgrade.md) for a pinned version comparison and a concrete proposed upgrade. Preserve profile/setup, note folders, Ledger/history, custom rules, pause status and live Extra state. Review any migration and task-prompt change before applying it. Never replace your vault with another blank template copy or merge public template history into it.

Older installations can start from the canonical public entrypoint:

```text
Read the latest System/upgrade.md from the public repository
yilinqiao/daily-companion-with-chatgpt and help upgrade my private
Daily Companion repository <OWNER>/<PRIVATE_REPO>.
First show the pinned source version/commit, proposed file changes and migrations.
Preserve my completed setup, configuration, notes, Ledger/history and custom rules.
Preserve existing task timing and paused status; do not recreate working
Morning/Evening tasks. Apply the specific changes only after I approve them.
```

For a v5/older Extra, the current migration replaces the seed/calendar with one date, asks for its new narrow scheduled-write consent and removes the old never-write task clause. It does not automatically activate a paused or never-activated Extra. See the upgrade contract for coordinated task suspension and restoration.

Before an upgrade, finish pending local edits and verify their push; keep an independent backup. Avoid simultaneous device edits/sync while the coordinated upgrade runs. Afterwards, inspect the verified private commit and pull it to each device before resuming edits. Existing live dates/claims are preserved on a documentation-only update; installation markers must not be stamped by a device sync alone.

## 8. Check the path you actually use

Use a harmless temporary test note in the private vault to verify device sync. Test only the devices you use; a phone and desktop are not both prerequisites for ChatGPT setup.

| Check | Evidence to inspect |
| --- | --- |
| Obsidian local edit → GitHub | Successful commit/push or sync, matching content in your private repository |
| GitHub edit → Obsidian | Completed pull/sync, matching content in the same local vault |
| GitHub → ChatGPT | Read of the exact private owner/repo, branch and configured setup/runtime path |
| Approved ChatGPT save → GitHub → device | Verified private commit/read-back, followed by a verified device pull |
| Extra → its own state, when activated | Actual due-run claim/advance commits; task enabled status alone is insufficient |

When something fails, identify the layer: account/repository permission, ChatGPT write, device sync, merge conflict, task activation or notification. Keep verified Morning/Evening tasks and existing data intact while diagnosing another layer.
