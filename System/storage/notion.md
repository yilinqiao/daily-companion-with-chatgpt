# Notion storage (recommended)

Use only the configured private suite, System index and source IDs. Never switch stores on failure. For installation see `System/setup/notion.md` (not a runtime dependency).

## Read and identity

- Prefer verified saved views and paginate every page using has_more / next_cursor or the equivalent connector mechanism. Read recent Daily records via Last 7 days when available; ensure all seven previous local dates are covered. For exact identity use the unfiltered Daily Briefing & Memory view sorted newest first, query the specific dates/category or scan until past the target; never infer absence from a truncated or filtered view. Use targeted SQL only if necessary and supported.
- Daily unique key = local date + Category (exactly one category, not title); read all matches, stop on ambiguity or incomplete coverage. Treat Auto-Saved as provisional, Edited as user-approved; Imported only as confirmed if provenance establishes approval.
- Ledger: query all rows of unfiltered Ledger Audit (All), including Closed and standing precedents; paginate. Use fresh schema and existing property options on every authorized write. Fill applicable reliably known properties, ask if uncertain, leave nonapplicable blank, never invent options, dates or IDs. Match immutable Task ID and exact row identity. Verify changed properties/values and preserve unrelated data.
- Approved capture sources only: use original reliable capture metadata or genuine native Created time; imported/archive creation timestamps are not evidence of capture today. Keep source links. If no configured capture source, skip.

## Daily persistence

With persisted notion_daily_autosave_authorized:true, create only the run's initial Daily page (Status Auto-Saved, date, category, title and body). No overwrite on replay, including existing Auto-Saved, Edited or Imported pages. Verify exact row identity, date, category, status and body before claiming saved. If missing consent, use approved interactive save only. Never scheduled Ledger mutations. Report actual partial failure and offer interactive recovery; never cross-store backup.

Notion uses native title/date/category/status properties; omit GitHub YAML and duplicate H1 from its body. Preview the exact visible body for interactive approval.

Morning: append a final Notion-only `Calendar ID` section with original title/start/end, exact calendar_id + event_id and provider link when available, one per confidently mapped event. Use the common narrow identity-recovery contract in artifacts.md. If no identity, distinguish no events from incomplete retrieval/identity. Never expose this section or its IDs in chat. Preserve it unchanged on every revision; Evening reads it for exact event lookup first. If missing on an old page, report incomplete linkage; repair only with explicit approval and uniquely recoverable original identity.

Evening: initial Auto-Saved Diary-first Memory before ordinary check-in; no initial full Markdown preview. Interactive revision after answers follows artifacts.md: fresh-read correct page, reconcile intervening edits with fresh approval, update same page and verify exact normalized visible content and protected metadata before setting Status Edited; read back status and identity. Do not claim Edited on partial failure. Same revision procedure for Morning. Keep provisional evidence distinct from confirmation.

If initial auto-save was unauthorized, failed or absent, offer an interactive full preview and approved exact-date creation only after a fresh complete lookup can prove no existing row; if a row exists, reconcile and revise that row instead. Preserve any original Calendar identity. Verify body and metadata before marking Edited. Never duplicate on uncertain save results.

## Private System revisions

Before changing any System page interactively (including Extra controls), fresh-read its body and numeric version; save and verify a complete prior-body snapshot under Versions (excluding the history container itself). Apply only approved changes, increment version, and read back body/version. The numeric page revision is independent of template semver. Stop/report any failure; no scheduled System writes.
