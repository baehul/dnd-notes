---
description: Turn raw session notes into a player-facing Session Notes recap, interactively
argument-hint: NN [notes path] (or paste your raw notes in the next message)
allowed-tools: Agent, SendMessage
---
Usage: `/session-summary NN <notes path>`, or paste your raw session notes in the next message.
The brief path is derived from NN:
`C:\Users\mehul\DND\dnd-audio-transcription\state\briefs\session-NN-v2\for-notes\` (judge-blind;
it only exists after the DM says "release"). If that folder is missing, or `MANIFEST.json` shows
no release, say so and stop; do not read any other folder. In Stage 1 the Steward reads
`brief.md`, `brief.json`, `opening_recap.json`, `table_names.tsv` and `MANIFEST.json` from that
folder, and `lines.json` only for cited lines.

This flow is owned end-to-end by the **Steward** subagent — grounding, timeline, drafting, and
writing all happen inside the Steward's context, so the raw session files and canon pages never
load into mine. My only job is to relay between you and the Steward. I do NOT read, grep, or
glob the vault for this flow, and I do NOT draft the recap myself. The Orchestrator adds no
separate review round between the Steward's draft and the DM unless the DM asks for one.

Run it as a resumable loop with a SINGLE Steward instance — spawn it once, then continue it via
SendMessage so it keeps everything it has read. Never re-spawn a fresh Steward mid-flow; that
throws away its context and re-reads every file.

1. **Spawn the Steward** with your raw notes plus the SOURCES rule and Stage 1 instructions
   below. Relay its timeline back to you.
2. **Corrections.** You give corrections/additions. I SendMessage them to the same Steward
   along with the Stage 2 instructions (structure + frontmatter below). Relay the draft to you.
3. **Write.** Only on your explicit approval, I SendMessage the Stage 3 instruction. I never
   approve on your behalf.
4. Report back the exact path the Steward wrote. I do NOT commit or push — git is a separate
   step you trigger.

Everything below this line is the Steward's brief — I hand it the relevant stage's text; the
Steward holds the recap format only for the duration of this flow, never permanently.

---

**SOURCES**, in order of authority: your answers and rulings > a transcript brief, if the DM has
granted one (EVIDENCE of what was said and done) > the DM's pasted raw notes (player-written
and paraphrased) > `Session Notes/` (what happened at the table, improvised details included)
> the canon folders. On what was said, pasted notes never override the brief; if they
disagree, use the brief's version and list both for the DM. NEVER consult
`Private Notes/Session Prep/` — prep is only what was planned, is frequently wrong, and is
not canon. If a prep detail contradicts the notes, discard it silently: don't raise it,
don't ask to reconcile it. A brief never overrides anything automatically: where it
disagrees with `Session Notes/` or a canon page, list both versions with the cited lines in
Stage 1 and wait for the DM's confirmed resolution; a session event outranks an older canon
page only once the DM has confirmed the resolution. Brief-only items are confirmed with the
DM before they enter a draft. Read a brief or transcript only at the exact paths the DM
granted in this session.

**Stage 1 — grounding + timeline.** Read the 2–3 most recent `Session Notes/` files (to match
voice, continuity, and current player knowledge) and cross-check every proper noun against
`Characters/`, `Locations/`, `Organizations/`, `Religion/`, `Player Characters/` for exact
established spelling. Return a BULLETED TIMELINE of what happened, in order, with `(?)` on
anything you can't find or that's ambiguous. STOP — write nothing, draft no prose yet.

If the DM has granted a transcript brief, mark each timeline bullet BOTH (in the DM's notes and
the brief), NOTES-ONLY (keep; mark it), or BRIEF-ONLY. List BRIEF-ONLY bullets separately and
hold them for the DM's confirmation; they do not enter a draft unconfirmed. List each
disagreement between the brief and `Session Notes/` or canon as a CONFLICT with both versions and
the cited lines; resolve nothing yourself. Handle brief items this way: (1) an `improvised` flag
is provenance only: keep the item, attributed ("the ghost said …"), never as unattributed world
fact unless the DM settles it, and never name anyone the DM has marked unnamed. (2) Anything the
brief marks open or awaiting audio, or that depends on an open queue entry, stays out of the
visible recap until the DM rules. A character's guess at a duration stays attributed as a guess.
(3) Gaps come from the DM's notes, not the brief; do not fill a gap from the brief without
confirmation. (4) Table talk, rules chatter, table-address names (nicknames, DM-name mishearings, the
recording bot) and `present` lists stay out of the visible recap. Anything said or done in the
session, including in the opening recap, is never left out for secrecy. The table's shorthand
"Collin's sister" for Alexandra goes in attributed as shorthand, never as a claim that they
are siblings.
(5) No quotes, dialogue or close paraphrase of transcript text: facts in your own words. Ask
the DM only plain, self-contained questions, one decision each: say what the item is, why you
are asking, and what happens by default. No internal jargon and no bare line ids; describe the
moment in words.

Return Stage 1 as ONE grouped message. First list what is included automatically: every BOTH
item, and every NOTES-ONLY item (marked). Then ask only about BRIEF-ONLY items, CONFLICTS, and
names the vault and the known-names list cannot identify. Each is its own plain question with a
default, following the rule on questions above. Do not ask about anything already decided.

Known names: read `table_names.tsv` from the brief folder (columns: heard, kind, resolves_to, note). A name listed there is settled: use its `resolves_to` and never ask about it. Only names not listed get a vault check and, if still unidentified, a question.

Opening recap: every session opens with a player's recap, from when the DM asks who wants to
give the session summary until he thanks them for the wonderful session summary and grants
Inspiration. Compare it against the previous session's Session Notes page and list anything
said in the recap that the page lacks, described in plain words. List anything the recap
contradicts as a question for the DM, not as an error. Do not edit the page; any edit needs
the DM's direct approval.

Working notes: `brief.md` is long and Read truncates at about 25,000 tokens, so read it in
pages (offset and limit). `lines.json` is large: read only the cited lines with a short python
script, never the whole file. When searching the vault, exclude `Private Notes/Session Prep`.
When editing wrapped text, match by content across line breaks.

**Stage 2 — draft.** After the DM's corrections, draft the recap in EXACTLY the structure
below. Voice: third person, past tense, narrative chronicle. Keep story beats; leave out turns,
distances, check types, spell names and inventory counts. Who did what may stay (for example,
"Cletus made himself and the bag invisible"). Ground every detail in the notes
or canon — invent nothing. Return the draft; do not write it yet.

Before returning the draft, spot-check it: (1) search for quotation marks (only the
frontmatter title may have them; quote nothing from the transcript); (2) search for numbers and
mechanics words (turns, feet, rolls, checks, saves, slots, DC, hit points) and remove them or
put them in plain language; (3) verify 3 to 5 claims that have no support in the DM's notes
against the cited lines. Note anything you changed.

```
---
draft: false
title: "Session NN:"
tags:
  - session-notes
---
## Summary
### [Event/Scene Name]
[1–2 paragraphs on the event, focusing on narrative story beats.]

### [Event/Scene Name]
[1–2 paragraphs.]

### Additions
* **New NPCs:** [only recurring or campaign-level NPCs]
* **New Locations:** [only real places the DM will revisit]
* **Loot & Acquisitions:** [only acquired magic or quest items]

%%
### DM Secrets & Context
* [Lore only the DM tracks, for example who an unnamed figure really is, or what an NPC
  secretly did. Never resource tracking (spell slots, expended or lost items, unstated
  durations): those appear as a story beat in the prose if they matter, or are dropped.
  Quartz strips this block from the published site.]
%%
```

Omit any Additions line with nothing to list, and omit the whole Additions heading if all
three are empty. Do not list single-scene NPCs, sub-areas, or "None".

The visible sections (Summary, Additions) hold what was said and done at the table, including
the opening recap; nothing said or done in a session is secret, so nothing from it is left out
to keep a secret. Lore only the DM tracks goes in the `%%` block, never the visible body. Leave the title blank
after the colon (`title: "Session NN:"`) — players name their own sessions; never write or
suggest one.

**Stage 3 — write.** Only after the DM approves: write to `Session Notes/Session NN Notes.md`
(the vault convention — NOT `Session NN - Title.md`) and update `Private Notes/Planning/Threads.md`
(State, Status, Knows and Touched for every row the session moved; new rows at the next free ID;
resolved rows to the archive) and bump NPC last-seen. The `%%` block holds only secrets and
offscreen lore the DM tracks; threads, hooks and clocks live in `Threads.md`. A private aside
between the DM and one player is recorded in both. No
resource tracking (spell slots, expended or lost items, unstated durations) and no XP, loot or
level logging goes in it. Report the exact path written. Do not commit or push unless
separately asked.
