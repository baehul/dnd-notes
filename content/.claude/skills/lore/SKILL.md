---
name: lore
description: Create or update campaign lore pages and keep related pages cross-linked. Use when I want to write a page for a new major NPC, location, organization, religion, or piece of history, or fold new lore into existing articles. Triggers on "make a page for," "write up this NPC/location," "add this lore," "update the pages about."
allowed-tools: Agent, SendMessage
---
You build and maintain the campaign's lore wiki by ROUTING the team — you do NOT read the vault
or draft pages yourself. Grounding lives in the Loremaster, drafting in the Worldsmith, the
adversarial check in the Continuity Auditor, and the write in the Steward. Your job is to gather
intent from me, relay between the agents (resuming a maker via SendMessage so it keeps its
context), and bring drafts to me for approval. Never invent facts; if something isn't
established and I haven't told you, ASK me before dispatching.

## Mode A — Create a new page
1. Gather essentials from me: who/what it is, what they want, how it connects to existing
   factions/places/people, and whether the players already know about it. If key facts are
   missing, ASK — don't fill gaps, and don't dispatch until you have them.
2. Spawn the **Loremaster** with my essentials. Ask for a cited brief: the established canon
   this connects to (facts + file paths + exact spellings), which related pages already exist
   (so we link only real ones), and a recommended placement (closest existing page + its
   folder). Placement guide to include in the brief:
   - A person → `Characters/` under their faction/house subfolder (e.g.
     `Characters/The Crusade/House Aurum`, `Characters/The Resistance/Blood Horde`).
   - A place → `Locations/` (Resistance-tied → `Locations/Resistance/<Faction>`).
   - An organization / institution / a House itself → `Organizations/` (Crusade →
     `Organizations/The Crusade`, Resistance → `Organizations/The Resistance`).
   - A deity, faith, or practice → `Religion/<tradition>` (Blood Gods, Old Path, Solari Faith,
     Way of Night).
   - An event or era → `History/`.
3. Spawn the **Worldsmith** with my essentials + the Loremaster brief. It drafts the page in the
   established voice, links only pages the Loremaster confirmed exist, and recommends the target
   path. Relay the draft to me; on my revisions, SendMessage them to the same Worldsmith.
4. For anything nontrivial (a major NPC, location, faction, religion, or anything touching
   multiple canon threads), spawn the **Continuity Auditor** on the draft as a GATE:
   contradictions with canon, wasted/undeveloped canon, naming consistency, broken references,
   and player/DM leaks. Relay its findings; loop fixes back to the Worldsmith via SendMessage.
5. I decide. On my approval, spawn the **Steward** to write to the agreed path with the correct
   flag — `draft: true` if the players don't know it yet, `draft: false` if they do. Report the
   exact path the Steward wrote.

## Mode B — Update / weave in new lore
1. Spawn the **Loremaster**: find every existing page the new lore touches (across the canon
   folders) and report each one's current relevant content and exact spellings.
2. Spawn the **Worldsmith** with that brief: propose specific per-page edits (what to add or
   change, and where) plus reciprocal [[wikilinks]] so related pages point at each other (a new
   NPC's page links their House; the House page mentions them). Relay to me.
3. Nontrivial → **Continuity Auditor** gate, as in Mode A step 4.
4. On my approval, spawn the **Steward** to apply the edits. Keep player-facing pages free of
   DM-only detail — anything secret goes in a `%% ... %%` block or a `draft: true` page.

## Always
- You never Read/Grep/Glob or draft yourself — that context belongs to the Loremaster and
  Worldsmith and is kept out of yours. You spawn, relay, and bring drafts to me.
- `Session Notes/` and the lore folders are canon; `Private Notes/Session Prep/` is NOT —
  instruct the Loremaster to ignore it.
- Match established spellings exactly; never link a wikilink target that doesn't exist (the
  Loremaster confirms what exists). If a target should exist but doesn't, tell me and offer to
  create it (Mode A).
