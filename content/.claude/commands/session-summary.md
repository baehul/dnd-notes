---
description: Turn raw session notes into a player-facing Session Notes recap, interactively
argument-hint: (paste your raw notes in the next message)
allowed-tools: Read, Glob, Grep, Write, Edit
---
I'll turn my raw session notes into a player-facing recap for `Session Notes/`. I'll paste
the notes in my next message.

Follow this process and DO NOT skip steps:

SOURCES: my notes and my answers are authoritative, then `Session Notes/`, then the canon
folders. NEVER consult `Private Notes/Session Prep/` for a recap -- prep is only what I
planned, it is frequently wrong, and it is not canon. If a prep detail contradicts my notes,
discard the prep version silently: do not raise it, and do not ask me to reconcile it.

1. Read my notes. Then read the 2–3 most recent files in `Session Notes/` to match voice
   and continuity, and to see what the players already know.
2. Produce a BULLETED TIMELINE of what you think happened, in order. Cross-check every
   proper noun against the vault (`Characters/`, `Locations/`, `Organizations/`,
   `Religion/`, `Player Characters/`), use the exact established spellings, and mark
   anything you can't find or that's ambiguous with (?).
3. STOP. Write no file yet. Wait for my corrections and additions.
4. After I confirm, draft the recap using EXACTLY this structure. Voice: third person,
   past tense, narrative chronicle. Ground every detail in my notes or canon — invent
   nothing.

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
* [DM-only tracking: things that happened that the players do NOT know — hidden factions,
  secret plot developments, etc. Quartz strips this block from the published site.]
%%

   The visible sections (Summary, Additions) must contain ONLY what the party witnessed or
   would know. Anything secret goes in the `%% DM Secrets & Context %%` block, never in the
   visible body.
5. Show me the draft. Only after I approve, write it to `Session Notes/Session NN Notes.md`
   -- the vault convention, NOT `Session NN - Title.md`. Use exactly this frontmatter,
   leaving the title after the colon BLANK; my players invent the session titles, so never
   write one yourself and never offer me options for one:

```
---
title: "Session NN:"
tags:
  - session-notes
---
```

   Then tell me the exact path you wrote.
