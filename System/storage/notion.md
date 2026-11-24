# Notion storage (recommended)

Use only the configured private suite, System index and source IDs. Never switch stores on failure. For installation see `System/setup/notion.md` (not a runtime dependency).

## Runtime field mapping

- Daily: ONE shared `Daily Companion` source contains both Morning Briefing and Evening Memory; never split them into separate databases or data sources. `File name` = title, `As of` = local artifact date, `Category` = single-select exactly one of `Morning briefing` / `Evening memory`, `Status` = Auto-Saved / Edited / Imported. Native `Created time` and `Last edited time` are storage timestamps; `Day` / `Month` / `Year` are formulas. No legacy Google Drive URL property is required or created by the current template; preserve pre-existing custom and historical properties. Do not substitute timestamps for an original generation date/time.
- Ledger: `Name` = title, `Task ID` = immutable id, `Details` = next step/context, `Status` = lifecycle list, `Opened` = opened, `Closed On` = closed, `Due` = due, `Revisit` = revisit, `Resolution` = resolution, `Scope` = text scope, `Source` = source text, `Category` / `Tag` = user-defined multi-select classifications; `Standing Until` is optional only if present in the real private schema. Responsibility belongs in Details where useful.
- System: `System file name` = logical path, `version` = numeric page revision. Use verified private mappings for customized properties; never guess missing mappings or change schema during runtime.

## Read and identity

- Prefer verified saved views and paginate every page using has_more / next_cursor or the equivalent connector mechanism. Read recent Daily records via Last 7 days when available; ensure all seven previous local dates are covered. For exact identity use the unfiltered Daily Briefing & Memory view sorted newest first, query the specific dates/category or scan until past the target; never infer absence from a truncated or filtered view. Use targeted SQL only if necessary and supported.
- Daily unique key = local date + Category (exactly one category, not title); read all matches, stop on ambiguity or incomplete coverage. Treat Auto-Saved as provisional, Edited as user-approved; Imported only as confirmed if provenance establishes approval.
- Ledger: query all rows of unfiltered Ledger Audit (All), including Closed and standing precedents; paginate. Use fresh schema and existing property options on every authorized write. Fill applicable reliably known properties, ask if uncertain, leave nonapplicable blank, never invent options, dates or IDs. Match immutable Task ID and exact row identity. Verify changed properties/values and preserve unrelated data.
- Approved capture sources only: use original reliable capture metadata or genuine native Created time; imported/archive creation timestamps are not evidence of capture today. Keep source links. If no configured capture source, skip.

## Daily persistence

With persisted notion_daily_autosave_authorized:true, create only the run's initial Daily page (Status Auto-Saved, date, category, title and body). No overwrite on replay, including existing Auto-Saved, Edited or Imported pages. Verify exact row identity, date, category, status and body before claiming saved. If missing consent, use approved interactive save only. Never scheduled Ledger mutations. Report actual partial failure and offer interactive recovery; never cross-store backup.

Notion uses native title/date/category/status properties; omit GitHub YAML and duplicate H1 from its body. For new Morning Briefings retain the configured-timezone generation timestamp as a short visible line in the body; preserve original timestamps on revisions, never invent missing historical values. Preview the exact visible body for interactive approval.

Morning: append a final Notion-only `Calendar ID` section with original title/start/end, exact calendar_id + event_id, stable approved account_id and provider link when available, one per confidently mapped event. Use the common narrow identity-recovery contract in artifacts.md. If no identity, distinguish no events from incomplete retrieval/identity. Never expose this section or its IDs in chat. Preserve it unchanged on every revision; Evening reads it for exact event lookup first. If missing on an old page, report incomplete linkage; repair only with explicit approval and uniquely recoverable original identity.

Evening: auto-save one provisional Diary-first Memory; display the same complete user-visible body in ordinary chat after verified readback, without summary or omission. Keep link/status and questions outside the body; no editable approval preview before answers. Interactive revision after answers follows artifacts.md: fresh-read correct page, reconcile intervening edits with fresh approval, update same page and verify exact normalized visible content and protected metadata before setting Status Edited; read back status and identity. Do not claim Edited on partial failure. Same revision procedure for Morning. Keep provisional evidence distinct from confirmation.

If initial auto-save was unauthorized, failed or absent, offer an interactive full preview and approved exact-date creation only after a fresh complete lookup can prove no existing row; if a row exists, reconcile and revise that row instead. Preserve any original Calendar identity. Verify body and metadata before marking Edited. Never duplicate on uncertain save results.

## Bounded retry and safe Daily recovery

During Morning/Evening, retry a transient Notion fetch, view query, pagination request or readback at most twice after the first attempt (three attempts total per failed request). Retry only that request with the same target/cursor; retain successful reads and the original local occurrence date. Respect rate-limit retry-after guidance when supported. Do not retry explicit permission denial, invalid schema/request or a confirmed missing canonical target as if transient. No permission bypass or indefinite waiting. Required instructions and full exact-date/category identity coverage must be verified before any write.

Freeze the exact intended Daily body, date/category, status and protected Morning Calendar ID suffix before writing. On a timeout, ambiguous response or transient write error, never blindly repeat the operation: fresh-query the complete unfiltered Daily identity view and fetch any exact match. If its identity, status and normalized full intended body are verified, reuse that page without another write. Never overwrite an existing Auto-Saved page on replay, Edited/Imported records, conflicting content or duplicates. A failed readback is not proof that creation failed.

Only if non-commit is conclusively established, no request remains pending, and a fresh identity check proves the original operation is safe, retry that same frozen operation at most once. Creation requires verified absence; interactive update requires the same page ID and unchanged authorized baseline. If commit status, absence, approval or identity is uncertain, stop. Verify every successful or ambiguous write. These rules do not expand standing consent or interactive approval scope.

If recovery fails, report the failed stage (System dependency, identity query/pagination, write or readback), affected logical file/view or operation, available error code/message, attempt count and whether persistence is verified, failed or unverified. Do not invent a diagnosis or expose credentials/internal identifiers. Keep the full safe draft and, for Evening, all three capture questions; status/link/failure details precede them. Preserve Morning's approved-save fallback. No new schedules, background retries, automatic backfill, cross-store fallback or scheduled Ledger changes. Extra and Update Watch remain unchanged.

## Private System revisions

Before changing any System page interactively (including Extra controls), fresh-read its body and numeric version; save and verify a complete prior-body snapshot under Versions (excluding the history container itself). Apply only approved changes, increment version, and read back body/version. The numeric page revision is independent of template semver. Stop/report any failure; no scheduled System writes.
