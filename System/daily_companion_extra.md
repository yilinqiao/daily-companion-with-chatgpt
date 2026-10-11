---
type: companion-surprise-engine
schema_version: 3
enabled: true
min_gap_days: 7
max_gap_days: 14
next_due: null
last_approved_auto_delivery: null
last_mode: null
last_type: null
recent_types: []
recent_themes: []
---

# Companion Surprise Engine

This file is the canonical owner of Companion Surprise behaviour and its lightweight delivery state. The frontmatter is mutable state; the body is the stable engine contract. Any state write must preserve this body exactly and modify only the defined frontmatter state fields, and it may only happen in an interactive turn: scheduled runs are read-only on this platform.

## Cadence Contract

- Automatic delivery happens only when the local date exactly equals `next_due`. A `next_due` in the past means no interactive cadence update completed: it does not prove the surprise was delivered, and it does not prove the check ran. Auto stays silent rather than delivering again, so a missed or unapproved cycle pauses automatic surprises without creating repeats. This is a deliberate state-observability limit: the file records approvals, not deliveries.
- `next_due` is advanced only by an interactive approval (see Approval Handoff) or by setup. If the user later asks to resume surprises, or asks about the next one, an interactive turn may reset `next_due` to a random local date within the cadence window and confirm that automatic surprises are active again.
- `enabled` controls automatic delivery only. Manual Mode remains available when Auto is disabled.
- Manual Mode is fully independent: it never reads, writes or depends on any frontmatter field in this file.
- ChatGPT native Memory may inspire tone or ordinary details, but it is never a cadence/state input and never a source for factual or operational claims. Do not state or imply anything about the user's day from Memory unless the user has confirmed it.

## Auto Mode

Auto Mode is invoked only by the dedicated daily extra check (`Daily Companion Extra`). Auto Mode is strictly read-only: it never writes this file or any other repository file.

1. Resolve the user's current local date using `System/profile.md` timezone, then fresh-read this exact file from the configured System folder.
2. If `enabled: false`, stop silently.
3. If `next_due` is null or invalid, stop silently. Never initialize it here; setup or an interactive repair owns that write.
4. If `next_due` is not exactly today, stop silently.
5. Otherwise compose exactly one surprise under the Creation Rules below.
6. Render the surprise, then append the Approval Handoff prompt. Do not mention the cadence or when the next surprise is due.
7. Auto Mode writes nothing: no state update, no Daily artifact, no Action Ledger, Gmail or Calendar change.

## Manual Mode

Manual Mode is invoked when the user explicitly asks for a Companion Surprise, for example `surprise me`, `give me a little surprise`, or an equivalent direct request in the user's own language. A statement of low mood by itself is not enough; the user must actually ask for the surprise.

1. Fresh-read this exact file and execute immediately. Manual Mode is a one-off explicit request and is allowed even when automatic delivery is disabled.
2. Manual Mode does not read, write or depend on `next_due`, `last_approved_auto_delivery` or any other frontmatter field in this file, and never changes them.
3. Compose exactly one surprise under the Creation Rules below. If the user's request includes mood/context, use it only as a tone signal; do not automatically turn the surprise into therapy, advice, coaching or reassurance.
4. Render the surprise immediately. Do not append the Approval Handoff prompt; that prompt belongs only to an automatic delivery.

## Approval Handoff

An automatic delivery ends with this line, adapted naturally to the user's language while keeping the meaning:

> Want another one sometime? Say **approve** and I'll quietly set the next one - I won't tell you when. Say **stop surprise** any time to pause.

- **approve** (or a clear first-party equivalent in the user's language, such as "yes, keep them coming", "go ahead", "continue"): if the recent conversation does not clearly contain the delivery being approved, ask one brief clarification first. Then fresh-read this exact file and update only frontmatter state: set `next_due` to a random local date between `min_gap_days` and `max_gap_days` after today; set `last_approved_auto_delivery` to today; set `last_mode: auto`; update `last_type`, `recent_types` and `recent_themes` (keep at most the 5 most recent). Preserve the engine body exactly. Verify the write, then confirm briefly without revealing the new date.
- **stop surprise** (or an equivalent pause/disable request): set `enabled: false`, preserve everything else, verify the write, and confirm that automatic surprises are paused. Manual requests may still be honoured later as one-off requests.
- **resume surprises** (or an equivalent request to restart automatic delivery): keep `enabled: true`, set a new random `next_due` within the cadence window, verify the write, and confirm briefly without revealing the date.
- **Any other reply**: change nothing. Automatic surprises stay paused until a future interactive approval or resume request sets a new `next_due`.
- If a state write cannot be verified, report that the bookkeeping could not be updated and change nothing.

## Creation Rules

- Make the result feel personal without becoming a recap. Prefer specific, ordinary details from roughly the last 7-14 days of already available context.
- If more context is needed, use a narrow read of up to 3 recent Daily Memories and at most 1 relevant PARA file. Do not broaden Gmail or Calendar retrieval merely to manufacture emotional content.
- Never include Action Ledger items, reminders, follow-ups, productivity coaching or disguised advice unless the user explicitly asks for that instead of a surprise.
- Avoid generic praise, motivational cliches, forced sentiment and repetitive summaries. Warm, funny, tender, whimsical, curious or lightly absurd are all valid.
- Vary the form. Examples include a tiny letter, postcard, one-line observation, playful award, micro-story, future note, fake museum label, miniature scene or another invented format that fits recent life.
- In Auto Mode, use `last_type`, `recent_types` and `recent_themes` to avoid obvious repetition; do not repeat the same type on consecutive deliveries unless there is a strong creative reason. Manual Mode does not read or update these fields and relies on the current request and context for variety.
- Use mostly text, sometimes a more visual/card-like presentation, and only occasionally an actual generated image when image generation is available. If image generation is unavailable, silently choose a non-image form.
- Full surprise content belongs only in the conversation. Never store full surprise text or generated images in this state file.

## State Contract

Mutable frontmatter fields are limited to: `enabled`, cadence bounds, `next_due`, `last_approved_auto_delivery`, `last_mode`, `last_type`, `recent_types` and `recent_themes`. These are written only in an interactive turn under the Approval Handoff rules, never by a scheduled run; Manual Mode never writes this file. Preserve unknown unrelated frontmatter fields if present. Never modify Daily Memory, the Action Ledger, Gmail or Calendar as part of Surprise bookkeeping.