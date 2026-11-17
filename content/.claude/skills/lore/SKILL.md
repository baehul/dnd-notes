---
name: lore
description: Create or update campaign lore pages and keep related pages cross-linked. Use when I want to write a page for a new major NPC, location, organization, religion, or piece of history, or fold new lore into existing articles. Triggers on "make a page for," "write up this NPC/location," "add this lore," "update the pages about."
allowed-tools: Read, Glob, Grep, Agent, SendMessage
---
You build and maintain the campaign's lore wiki with me. Size the process to the job. Never
invent facts: for anything permanent, if it isn't established and I haven't told you, ask me.
`.claude/rules/vault-writing.md` governs every word that reaches the vault.

## First: how big is this?
- **Small** — a line or a paragraph on an existing page, a relationship, a correction. Do it
  yourself: read `Private Notes/Planning/Current State.md` and the pages involved, draft the
  edit, run the propagation steps from the conventions file to find every other page that
  states the same fact, and show me the diffs (3 to 5 at a time). Write on my approval.
- **Substantial** — a new page for a major NPC, location, faction, religion or piece of
  history, or lore that touches several threads. Use the team, below.

## Substantial: new page
1. Gather the essentials from me in one batch: who or what it is, what it wants, how it connects
   to existing factions, places and people, and whether the players already know it. Don't
   launch anything until I've answered.
2. **Loremaster**: a cited brief of the canon this connects to, which related pages exist (so
   we link only real ones), the current state of everyone involved, and the closest existing
   page for placement and format.
3. **Worldsmith**, with my essentials and the brief: the draft (DM layer and player-facing
   layer), the target path, and the list of existing pages that need a line pointing back.
   Relay it; send my revisions to the same Worldsmith.
4. **Continuity Auditor**, once, on the draft I've accepted: Significant findings come to me;
   Minor ones are fixed and listed in one line. If I resolve a Significant conflict in a way
   that reaches other pages, send the resolution back to the Auditor for its integration list.
5. On my approval, launch the **Steward** to write the page and every reciprocal edit, with
   `draft: false` if the players know it and `draft: true` if they don't. Report the paths.

## Substantial: weaving new lore into existing pages
1. **Loremaster**: every page the new lore touches, with each one's current relevant text.
2. Draft the per-page edits yourself from that brief (or hand it to the **Worldsmith** if it
   needs real authorship), in chronicle voice, with reciprocal wikilinks.
3. Auditor once if it touches several threads. Then my approval, then the **Steward** applies.

## Always
- Anything secret goes inside a `%%` block or on a `draft: true` page, never in visible text.
- Never link a name that isn't established; if a page should exist but doesn't, tell me.
- After a lore change, update the affected lines of `Current State.md` and `Threads.md`.
- `Private Notes/Session Prep/` is not a source.
