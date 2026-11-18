# GitHub storage (alternative)

Use only the verified private repository and configured System/Daily paths; never public source. Installation is in `System/setup/github.md`, not a runtime dependency. Obsidian is optional.

Scheduled runs are read/output only. Daily unique identity is configured filename/date/type; save exact approved Markdown interactively with YAML and H1 from artifacts.md. Inject only hidden Calendar identity comments per common identity recovery contract, immediately after corresponding event line:
```markdown
<!-- dc-calendar: {"calendar_id":"<calendar id>","event_id":"<event id>"} -->
```
Keep comments hidden in previews; preserve existing historical linkage on edits. Before each write read current file and fresh SHA; stop on conflict, don't overwrite or duplicate Daily history, verify committed content/link. Capture pages use original slurped timestamp or reliably attributable repository commit timestamp; preserve links. Skip if no approved capture source.

Include optional `account_id` in the same comment when the stable approved source account is known; never store session credentials. Retain older two-ID comments unchanged.

## Kanban representation

Use the four fixed lists Action, Waiting, Upcoming, Closed. Current list position is authoritative; CLOSE changes [ ] to [x] and moves same card to top of Closed; REOPEN reverses checkbox and preserves ID/opened. Preserve order of unrelated cards and plugin settings.

### File frontmatter

`action_ledger.md` carries a small file-level contract in addition to card metadata:

- `type: companion-action-ledger` and `schema_version` identify the file model and its version;
- `kanban-plugin: board` is the Obsidian Kanban file marker;
- `updated_at` records the local ISO-8601 time of the most recent **authorized interactive write**, stamped automatically by the assistant when that write occurs. It is never maintained manually and never updated by scheduled read-only runs. Manual user moves inside the Kanban board are not individually timestamped (the plugin emits no per-card modified date); the current Kanban list position is authoritative and is reflected at the next authorized interactive write.

### Card format and metadata

Each card has:
1. a short human-readable title;
2. a concise visible description of the current next step/wait/outcome;
3. one hidden HTML comment `<!-- dc: {...} -->`.

Core metadata:
- `id`: unique stable kebab-case ID; immutable and never reused;
- `opened`: date first admitted/recorded; immutable;
- `closed`: `null` while open; closure date when reliably known;
- `source`: optional when a clear source exists.

Optional metadata (owner is legacy GitHub-only, not required; record responsibility in Details for Notion): `owner`, `due`, `revisit`, `resolution`, `scope`, `standing_until`.

Preferred `resolution`: `completed`, `no_action`, `cancelled`, `declined`, `superseded`.

Do not add empty optional fields. Do not expose machine fields in the visible title/description.

If a manually moved Closed card has no reliable historical closure date, do not invent one merely to complete metadata; its column remains authoritative and `closed` may stay `null` until reliable evidence exists.



Apply only authorized changes against fresh file SHA; verify exact card ID, status/list, metadata, and content; never invent absent dates. Stamp updated_at only on authorized interactive writes. Extra uses the common read-only cadence; interactive edits preserve state/body and use fresh SHA/read-back.
