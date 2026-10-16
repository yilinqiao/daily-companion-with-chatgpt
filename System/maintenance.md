---
type: companion-template-maintenance
schema_version: 1
---

# Public Template Maintenance

This is the entrypoint for maintaining the canonical public template `yilinqiao/daily-companion-with-chatgpt`, whether through Codex or GPT web. It does not authorize modifying someone's private vault. Private installation upgrades use `upgrade.md`; normal personal settings and note changes keep their existing approval rules.

## Before editing

1. Verify the destination is the intended public source. Read root `AGENTS.md`, `VERSION`, `CHANGELOG.md`, `System/upgrade.md` and the existing files affected by the request. Resolve the current branch head and pin reads to that commit.
2. Understand the requested behaviour, compatibility and state ownership. Keep public examples generic and state fields null/empty. User customization and active data belong only in private copies.
3. Choose the next template version under the changelog's policy. Runtime file schema versions are independent. Older unversioned installations must remain supported through a conservative file comparison.

## Every public update

- Change the requested rules and their routing together. Keep setup, runtime entrypoints and user documentation consistent.
- Bump root `VERSION` and add a dated `CHANGELOG.md` entry containing actual user-visible changes, affected files, migrations, limitations and verification. Do not change previously released behaviour under the same version. Stage related files in a branch, then squash-merge a complete, tested release into `main`.
- Check whether `System/upgrade.md` needs a new migration: list old/new formats, preserve configuration/cards/history/customizations, describe authorized fields and handle partial failure. If no migration is needed, say so in the release entry. Maintain the upgrade entrypoint and its links even for a small rule edit.
- For new required files, update setup readiness and the public release checker. For new tool dependencies, update capability verification and honest activation reporting.
- Do not modify the public profile's installed markers; those are populated only when a private user's installation or approved upgrade is verified.

## Verify and publish

- Run `python -B scripts/check_public_release.py` and regression checks appropriate to the change. Inspect diffs for private data; automated heuristics do not prove complete PII removal.
- On a release PR, run `python -B scripts/check_release_version.py --base <target-main-commit>`. CI checks privacy/structure and regressions on PRs and `main` pushes, and checks the cumulative version/notes delta on PRs only. Work-in-progress feature-branch pushes do not trigger CI. The version unit test checks that the current `VERSION` has exactly one valid dated changelog entry on every run. Direct-to-main pushes do not enforce a version bump, so use PRs for releases; do not mistake source commits for a published version. A branch with history but no dependable baseline requires an explicit base, never a tip-only comparison.
- CI reports a failing check; repository protection settings determine whether that blocks merging. A workflow does not undo an already accepted direct push. Do not describe these checks as automatic branch protection.
- GitHub can package multiple changed files into one commit; GPT integrations that update files sequentially should stage those commits on a branch and squash-merge after successful PR CI. Use a normal commit/ref update with an expected current head; inspect concurrency conflicts rather than overwriting them. Stop and report any safety/access block.
- Verify remote files and CI. Report the version, changed behaviour, migration requirements and any unverified runtime capability. Source publication never means private copies were automatically updated.

## GPT web entry prompt

```text
Before modifying the public repository yilinqiao/daily-companion-with-chatgpt,
read AGENTS.md and System/maintenance.md from that repository.
Apply the requested instruction changes with a version bump and dated
CHANGELOG.md entry, and update System/upgrade.md if migration is needed.
Keep all public configuration/state uninitialized and verify the release.
```

Codex can load root `AGENTS.md` when working in the checkout. GPT web needs an explicit repository read; a new conversation cannot know unread repository rules. The CI gate is an additional publication check, not a substitute for that context.
