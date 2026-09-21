---
description: Turn raw session notes into a player-facing Session Notes recap, interactively
argument-hint: (paste your raw notes in the next message)
allowed-tools: Agent, SendMessage
---
Paste your raw session notes in the next message.

This flow is owned end-to-end by the **Steward** subagent — grounding, timeline, drafting, and
writing all happen inside the Steward's context, so the raw session files and canon pages never
load into mine. My only job is to relay between you and the Steward. I do NOT read, grep, or
glob the vault for this flow, and I do NOT draft the recap myself.

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

**SOURCES**, in order of authority: your notes and answers > `Session Notes/` > the canon
folders. NEVER consult `Private Notes/Session Prep/` — prep is only what was planned, is
frequently wrong, and is not canon. If a prep detail contradicts the notes, discard it
silently: don't raise it, don't ask to reconcile it.

**Stage 1 — grounding + timeline.** Read the 2–3 most recent `Session Notes/` files (to match
voice, continuity, and current player knowledge) and cross-check every proper noun against
`Characters/`, `Locations/`, `Organizations/`, `Religion/`, `Player Characters/` for exact
established spelling. Return a BULLETED TIMELINE of what happened, in order, with `(?)` on
anything you can't find or that's ambiguous. STOP — write nothing, draft no prose yet.

**Stage 2 — draft.** After the DM's corrections, draft the recap in EXACTLY the structure
below. Voice: third person, past tense, narrative chronicle. Ground every detail in the notes
or canon — invent nothing. Return the draft; do not write it yet.

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
* **New NPCs:** [names met, or "None"]
* **New Locations:** [places visited, or "None"]
* **Loot & Acquisitions:** [items gained, or "None"]

%%
### DM Secrets & Context
* [DM-only tracking: things the players do NOT know — hidden factions, secret plot
  developments, offscreen events, unfelt consequences. Quartz strips this block from the
  published site.]
%%
```

The visible sections (Summary, Additions) must contain ONLY what the party witnessed or would
know; everything secret goes in the `%%` block, never the visible body. Leave the title blank
after the colon (`title: "Session NN:"`) — players name their own sessions; never write or
suggest one.

**Stage 3 — write.** Only after the DM approves: write to `Session Notes/Session NN Notes.md`
(the vault convention — NOT `Session NN - Title.md`) and apply the state updates the recap
implies (advance/resolve threads, bump NPC last-seen, log XP/loot/level) inside the `%%` block.
Report the exact path written. Do not commit or push unless separately asked.
