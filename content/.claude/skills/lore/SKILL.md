---
name: lore
description: Create or update campaign lore pages and keep related pages cross-linked. Use when I want to write a page for a new major NPC, location, organization, religion, or piece of history, or fold new lore into existing articles. Triggers on "make a page for," "write up this NPC/location," "add this lore," "update the pages about."
allowed-tools: Read, Glob, Grep, Agent
---
You help me build and maintain the campaign's lore wiki by orchestrating the team: pull a
**Loremaster** brief before drafting, draft as the **Worldsmith**, run anything nontrivial past
the **Continuity Auditor** as a gate, and hand the approved result to the **Steward** to write.
Ground everything in canon and in what I tell you; never invent facts about the world. If
something isn't established and I haven't told you, ASK.

## Mode A — Create a new page
1. Gather the essentials from me. If key facts are missing (who they are, what they want, how
   they connect to existing factions/places/people), ask — don't fill gaps yourself.
2. Decide where it goes by finding the closest existing page and mirroring its location and
   format (frontmatter, headings, section order). Placement guide when there's no precedent:
   - A person → Characters/ under their faction/house subfolder (e.g.
     Characters/The Crusade/House Aurum, Characters/The Resistance/Blood Horde).
   - A place → Locations/ (Resistance-tied → Locations/Resistance/<Faction>).
   - An organization or institution (a House itself) → Organizations/ (Crusade →
     Organizations/The Crusade, Resistance → Organizations/The Resistance).
   - A deity, faith, or practice → Religion/<tradition> (Blood Gods, Old Path, Solari Faith,
     Way of Night).
   - An event or era → History/.
   If you're unsure where it belongs, ask before writing.
3. Draft the page in the established voice. Use [[wikilinks]] to connect it to related pages —
   but only to pages that actually exist (check first).
4. Ask whether the players know about this yet. Set `draft: true` if not, `draft: false` if so.
5. Show me the draft. Only after I approve, hand it to the **Steward** subagent to write, and
   tell me the path the Steward reports back.

## Mode B — Update / weave in new lore
1. Find every existing page the new lore touches (Grep/Glob across the canon folders).
2. Show me the specific edits you propose for each page — what you'd add or change, and where —
   before touching anything.
3. On my approval, hand the approved edits to the **Steward** subagent to apply, adding
   reciprocal [[wikilinks]] so related pages point at each other (e.g. a new NPC's page links
   their House, and the House page mentions them).
4. Keep player-facing pages free of DM-only detail; anything secret goes in a `%% ... %%`
   comment block or a `draft: true` page (see CLAUDE.md).

## Always
- Match established spellings and titles exactly — search the vault before writing any name.
- Do not use Private Notes/Session Prep/ as canon; use Session Notes/ and the lore folders.
- Never create a wikilink to a page that doesn't exist. If a link target should exist but
  doesn't, tell me and offer to create it (Mode A).
