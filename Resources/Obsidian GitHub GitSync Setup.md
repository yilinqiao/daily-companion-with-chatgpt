# Obsidian + GitHub + GitSync Setup

This guide sets up one Obsidian vault backed by a private GitHub repository. GitHub is the canonical remote copy and version history. Each device edits a local working copy.

## Architecture

```text
Desktop Obsidian                         Mobile Obsidian
      ↕                                       ↕
GitHub Desktop / Git                    GitSync
      ↘                                       ↙
          private GitHub repository
                    ↕
                 ChatGPT
```

ChatGPT reads the repository directly through the GitHub connection. After explicit interactive approval, it can commit approved Daily Companion file changes back to the configured repository. GitSync is only the device sync layer; ChatGPT does not need the phone to be online to read GitHub.

## 1. Create the GitHub repository

1. Create a **private** GitHub repository for the vault. A name such as `daily-companion-vault` is fine.
2. Copy the contents of `Daily Companion Starter` into the repository root, then commit and push.
3. Keep the repository root as the Obsidian vault root unless you have a reason to use a subfolder.

Recommended `.gitignore` for this starter:

```gitignore
.obsidian/
.trash/
.DS_Store
Thumbs.db
```

The starter intentionally does not depend on syncing `.obsidian/`. Install the required Obsidian plugins separately on each device. This avoids device-specific workspace/plugin state creating noisy Git conflicts.

## 2. Desktop setup (Windows / macOS)

1. Install **Obsidian**.
2. Clone the repository with **GitHub Desktop** or your normal Git client.
3. In Obsidian, choose **Open folder as vault** and select the cloned repository folder.
4. Install the **Kanban** and **Slurp** community plugins on that device.
5. Test the path both ways: edit a small note in Obsidian, commit/push it, then make a small repository edit elsewhere and pull it back.

You do not need a separate cloud-sync utility on desktop. Git is the sync/version-control layer.

## 3. Android setup with GitSync

1. Install **Obsidian** and **GitSync** by ViscousPotential.
2. Open GitSync and sign in to GitHub.
3. Clone the vault repository into a local folder that Obsidian can access.
4. Open that local folder in Obsidian as a vault.
5. In GitSync, enable app-based sync for Obsidian. GitSync can watch Obsidian opening and closing through its optional Android Accessibility Service. Configure sync on open and sync on close.
6. Run one manual **Sync Now** and confirm the repository is clean before normal use.

With app-based sync configured, you normally do **not** need to open GitSync manually before every Obsidian session. Opening Obsidian can pull/sync first, and closing it can commit/push the session's changes. Manual Sync Now remains useful before switching devices when you want to verify the latest state immediately.

## 4. iPhone / iPad setup with GitSync

1. Install **Obsidian** and **GitSync**.
2. In GitSync, sign in to GitHub and clone the vault repository to a Files location that Obsidian can open as a vault.
3. Open that folder in Obsidian.
4. In the iOS **Shortcuts** app, add GitSync's **Sync Now** action.
5. Create an Automation for **Obsidian → Is Opened** and run **Sync Now** immediately.
6. Create another Automation for **Obsidian → Is Closed** and run **Sync Now** immediately.

This is the recommended GitSync pattern for notes apps on iOS. It gives the same practical behavior as Android: sync when you enter and leave Obsidian without manually visiting GitSync each time.

## 5. Connect ChatGPT to GitHub

1. Connect the **GitHub** app/connector in ChatGPT.
2. Grant it access to the Daily Companion repository.
3. During setup, provide the repository in `owner/repository` form.
4. Test that ChatGPT can read `System/setup.md` from that repository.
5. After you approve the setup summary, the setup flow will perform its first intended repository writes and verify them.

Use a launch prompt like:

```text
Read System/setup.md from GitHub repository <owner>/<repo> and start Daily Companion setup.
```

## 6. Sync safety

- Treat the GitHub repository as the canonical shared remote.
- Pull/sync before editing on a device and push/sync after editing. App-open/app-close automation handles most of this on phones.
- Avoid editing the same note on two devices at exactly the same time.
- Do not run two separate sync systems against the same vault. GitSync/Git should be the only vault sync path.
- Git history is useful version control, but a separate backup is still sensible for irreplaceable material.

## 7. Quick end-to-end check

Before running Daily Companion setup, confirm all four directions:

```text
Phone Obsidian edit → GitSync → GitHub
GitHub change → GitSync → Phone Obsidian
Desktop Obsidian edit → Git push → GitHub
GitHub repository → ChatGPT can read System/setup.md
```

If those checks work, the vault, version history and ChatGPT access are all using the same repository instead of separate copies.
