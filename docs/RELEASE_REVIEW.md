# Public release checklist

- [ ] Verify the repository is a new, separate public source, never a personal vault or imported private Git history.
- [ ] Verify README links, System/setup.md and paths all resolve and agree.
- [ ] Confirm profile is unconfigured, Ledger has no cards, Extra contains no delivery history and user note folders are empty.
- [ ] Inspect all file contents, comments, examples and linked resources for names, emails, addresses, keys, tokens, private paths, personal amounts and identifiers.
- [ ] Run python3 scripts/check_public_release.py and inspect any warnings.
- [ ] Verify the Actions privacy-check workflow completes successfully.
- [ ] Check GitHub public owner, commit author name/email, issue metadata and prior commits.
- [ ] In Settings → General, enable **Template repository**.
- [ ] Use **Use this template** to create a test **Private** repository.
- [ ] Test GitHub read and approved write into that private repository.
- [ ] Test one-question onboarding, source permissions, Calendar/Gmail reduced-source mode, Morning, Evening, Ledger and persistence.
- [ ] Test schedules and time zones only if supported by the test ChatGPT account.
- [ ] Test Obsidian sync separately on the devices actually supported.
- [ ] Record remaining limitations rather than declaring an untested production launch.

Static checks cannot guarantee that all personal information has been removed.
