---
description: Turn a played session into the player-facing Session Notes recap and bring the trackers and wiki pages up to date
argument-hint: NN [notes path] (or paste your raw notes in the next message)
allowed-tools: Agent, SendMessage
---
Usage: `/session-summary NN <notes path>`, or paste your raw session notes in the next message.

The brief folder is derived from NN:
`C:\Users\mehul\DND\dnd-audio-transcription\state\briefs\session-NN-v2\for-notes\`. It exists
only after the DM releases it. If the folder is missing, or `MANIFEST.json` shows no release,
say so and stop; do not read any other folder.

This flow belongs to the **Steward** subagent: grounding, timeline, drafting and writing all
happen in its context, so the raw session files never load into the main conversation. The main
conversation relays between the DM and the Steward and adds no review round of its own.

Run it with a SINGLE Steward: spawn it once, then continue it with SendMessage so it keeps what
it has read. Never spawn a fresh Steward mid-flow.

1. **Spawn the Steward** with the raw notes, the SOURCES rule and Stage 1. Relay what it returns.
2. **Corrections.** Send the DM's answers to the same Steward with Stage 2. Relay the draft.
3. **Write.** On the DM's approval of the recap, send Stage 3, quoting the DM's approving words.
4. **Stale pages.** Relay the Steward's proposed page edits; send back the DM's decisions.
5. Report every path written. No commit or push.

**How to relay.** Never pass a whole stage on at once. Relay 3 to 5 items at a time (timeline
bullets, questions or draft scenes) and wait for the DM before the next chunk. Order: the
"Assumed" list first as one short block the DM can skim and veto, then the questions, then the
timeline. Collect all answers and send them to the Steward in one message. If the DM says the
defaults are fine, stop asking and proceed.

Everything below the line is the Steward's brief; hand it the relevant stage.

---

**SOURCES**, in order of authority: the DM's answers and rulings > the transcript brief
(evidence of what was said and done) > the DM's pasted raw notes (player-written, paraphrased)
> `Session Notes/` > the canon folders. On what was said, pasted notes never override the brief;
where they disagree, use the brief's version and list both for the DM. Never consult
`Private Notes/Session Prep/`: prep is only what was planned. If a prep detail contradicts the
notes, discard it silently. A brief never overrides a recap or canon page automatically: list
both versions with the cited lines as a CONFLICT and wait for the DM. Read the brief folder
named above and `C:\Users\mehul\DND\dnd-audio-transcription\transcripts\corrected\session-NN.json`
only; nothing else in that repo.

**Stage 1 — grounding and timeline.** Read, in this order:
- `Private Notes/Planning/Current State.md` (who everyone is and what the party knows going in).
- The 2 most recent `Session Notes/` files (voice, continuity).
- From the brief folder: `MANIFEST.json`, `table_names.tsv`, `brief.md`, `brief.json`, and
  `lines.json` only for cited lines. The opening recap is `opening_recap.json` if the folder has
  it; otherwise use the opening-recap section inside `brief.json` / `brief.md`; if there is
  neither, say that the opening recap was not detected for this session and carry on.

Cross-check every proper noun against the vault for its exact established spelling. Build a
bulleted timeline of what happened, in order. Write nothing and draft no prose yet.

Sort every item and decide what needs the DM:
- **Take the default, no question:** anything in both the DM's notes and the brief; anything
  only in the DM's notes; a spelling that matches the vault; a name settled in `table_names.tsv`
  (use its `resolves_to`); an identity or relationship stated in `Current State.md`.
- **Ask:** items only in the brief that would change the story as recorded (a new fact, name,
  amount, promise or reveal); CONFLICTS between sources; names neither the vault nor the name
  table can identify; whether the party learned something, when that is unclear.
- Items only in the brief that are incidental colour (a gesture, a remark, scene dressing)
  are taken by default and listed under Assumed.

Handling rules: (1) An `improvised` flag is provenance only: keep the item, attributed ("the
ghost said …"), never as unattributed world fact unless the DM settles it, and never name
anyone the DM has marked unnamed. (2) Anything the brief marks open or awaiting audio stays out
of the visible recap until the DM rules. A character's guess stays attributed as a guess.
(3) Gaps are filled from the DM's notes, not from the brief. (4) Table talk, rules chatter,
table-address names and `present` lists stay out. (5) Nothing said or done in the session,
including in the opening recap, is left out for secrecy. (6) Table shorthand for a relationship
goes in as shorthand unless `Current State.md` confirms the relationship as fact.

Opening recap: every session opens with a player's recap of the previous one. Compare it with
the previous session's `Session Notes/` page. List what the recap says that the page lacks, and
anything it contradicts as a question, not an error. Do not edit that page.

Return Stage 1 as one message in four parts:
1. **Assumed** — one line each: the defaults you took that the DM might want to veto. Leave out
   the unremarkable ones.
2. **Questions** — numbered, each plain and self-contained, one decision, saying what the item
   is, why you ask, and the default. Describe the moment in words; no line ids or internal labels.
3. **Timeline** — the bullets, in order.
4. **Opening recap** — additions and contradictions for the previous session's page, if any.

Working notes: `brief.md` is long; read it in pages (offset and limit). `lines.json` is large;
read only cited lines with a short python script. Exclude `Private Notes/Session Prep` from
vault searches.

**Stage 2 — draft.** After the DM's answers, draft the recap in EXACTLY this structure. Voice:
third person, past tense, narrative chronicle. Keep story beats; leave out turns, distances,
check types, spell names and inventory counts. Who did what may stay ("Cletus made himself and
the bag invisible"). Ground every detail in the notes, the brief or canon; invent nothing. No
quotes, dialogue or close paraphrase of transcript text. Return the draft; do not write it yet.

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
* [Lore only the DM tracks, sourced from the DM: who an unnamed figure really is, what an NPC
  secretly did. Never resource tracking. Quartz strips this block from the published site.]
%%
```

Omit any Additions line with nothing to list, and the whole heading if all three are empty.
The visible sections hold what was said and done at the table. A private aside between the DM
and one player goes in the `%%` block and in `Threads.md` with who knows. Leave the title blank
after the colon; never write or suggest one.

Before returning the draft, check it yourself: search for quotation marks (only the frontmatter
title may have them); search for numbers and mechanics words and remove them or put them in
plain language; verify 3 to 5 claims that have no support in the DM's notes against their cited
lines. Say what you changed.

**Stage 3 — write and write-back.** On the DM's approval of the recap:
1. Write `Session Notes/Session NN Notes.md`.
2. Update `Private Notes/Planning/Threads.md` and `Private Notes/Planning/Current State.md`, and
   append the scorecard line to the active adventure charter's log, as your own instructions
   describe. These are DM-only: write them directly.
3. Run the lint script on the files written.
4. Return: the paths written; a short summary of what changed in the trackers (rows moved,
   added, resolved; who-knows changes); and the **stale pages** list: every canon page the
   session overtook, each with a proposed chronicle-voice edit as a diff. Do not write those
   yet; they publish, so the DM approves them, in chunks of 3 to 5.

**Stage 4 — stale pages.** Write the page edits the DM approved, exactly as approved. For each
one declined, note "page stale: <what>" on the matching Threads row. Run the lint script and
report the paths. No XP, loot or level logging. Do not commit or push.
