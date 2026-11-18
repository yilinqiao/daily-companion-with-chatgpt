# GitHub onboarding only

Create a private template copy via Use this template (never fork); Obsidian optional. Confirm ownership/private visibility, scoped read/write access, canonical repository paths and approval. No Notion connection required.

After approval, verify the actual template copy's VERSION and source-owned files match the pinned upstream before initialization; on retry, allow only already verified approved initialization differences. Stop on mismatch and resolve the concrete diff, not just the label. Initialize and verify one file at a time with fresh content SHA; stop on conflict, access or read-back failure. Reuse already-correct files on retry; preserve existing cards/notes/settings. Existing installs use upgrade.md, not onboarding; missing files need scoped repair.

1. Populate private profile with approved settings/sources and capture mapping, storage_backend: github, valid planning window, Notion IDs null and consent false; setup_complete:false. Verify all applicable approved values and no unresolved required placeholders on read-back.
2. Initialize empty Ledger with the four lists and adapter's Kanban contract unless user explicitly approves seeding. Verify. Initialize Extra anchor_monday and weekday_pattern according to engine; keep enabled preference and existing valid state. Verify.
3. Verify all indexed/required runtime files: instructions, profile, workflows/morning, workflows/evening, policies/rules, policies/artifacts, storage/github, action_ledger, daily_companion_extra, setup, setup/github, upgrade, maintenance, plus private paths, writable Daily destination, approved connector checks and verified upstream VERSION/commit. No activation before readiness.
4. For a fresh never-activated installation, align the Extra anchor with first complete local week after finalization (if crossed week boundary, change only provisional anchor; never redraw live state). Separately set setup_complete:true and installed markers, verify. If finalization crosses week boundary, restore incomplete flag/new markers, align provisional anchor and verify finalization again before activation. Report configured, initialized, verified, and activation pending separately.

Source checks and activation follow shared setup.md. Never overwrite nonempty private data, rerun completed setup or bypass blocks. A legacy installation needs a specific approved upgrade.
