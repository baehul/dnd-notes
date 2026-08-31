# Campaign Vault — Assistant Instructions

## What this is
The Obsidian vault for The Shattered World, which I DM. It deploys to a player-facing wiki
via Quartz (using the `draft` filter). You are my writing/prep/brainstorming assistant.
Everything you produce must be consistent with the lore already here. All content lives
under this folder; work only here.

## Folder map
CANON — world lore (the truth about the world; ground all lore claims in these):
  Characters/ (Party/, The Crusade/…, The Resistance/…)  History/  Locations/
  Organizations/  Religion/  Player Characters/  Magic Items/ (+ Recipes/)
CANON — events (authoritative for "what actually happened"):
  Session Notes/    ← player-facing session recaps
DM REFERENCE — real & authoritative, but DM-only; never show players. Use for prep and
mechanics; do NOT cite as in-world fact:
  Private Notes/Meta Notes/  (Magic Item Crafting System, Rarity, Income & Gold, dungeon
  tools, etc.)
NOT CANON — speculative; do not treat as things that happened:
  Private Notes/Session Prep/ (+ Old Sessions/)  and  Private Notes/Old Stuff/
ASSETS (reference only, not lore text): Images/
IGNORE ALWAYS: .obsidian/  .claude/

## Canon vs. prep — READ FIRST
- The ONLY sources of truth are the CANON folders above.
- `Private Notes/Session Prep/` is NOT canon — it records what I planned, which often
  changes or never happens. Never treat prep as evidence an event occurred, and never use
  it to write player-facing pages. Ignore `Old Sessions/` and `Old Stuff/` entirely unless
  I explicitly point you at a file.
- To answer "what happened," use `Session Notes/`, never prep. Canon always beats prep.
- Order of authority: what I tell you > `Session Notes/` > canon pages. Prep is not a source
  at all -- do not surface prep details as questions or ask me to reconcile them with canon.

## Player knowledge vs. DM knowledge
- Player-facing = a page Quartz publishes: NOT under an ignored folder (e.g. `Private
  Notes/`, `.claude/`) AND without `draft: true` in its frontmatter.
- DM-only = anything under `Private Notes/` (incl. Meta Notes) OR any page with `draft: true`.
- Session recaps in `Session Notes/` DO publish, so their VISIBLE body is player-facing.
  DM-only tracking for a session goes ONLY inside the `%% ... %%` comment block, which
  Quartz strips from the published site. Never put DM-only info in the visible sections.
- For any other player-facing page, never include DM-only info: secrets, unrevealed plot,
  NPC motives the party hasn't learned, monster tactics, or anything the characters didn't
  witness. If unsure whether the party learned something, ask me before including it.
- `Administrative/`, `Lair/`, and `Misc/` currently publish (they aren't ignored). If any
  hold DM-only info, those pages need `draft: true` — tell me if so.

## Grounding — errors can derail the campaign
- Ground every world claim in a specific vault page; be ready to name the file.
- Do NOT invent names, places, history, factions, or lore. If it isn't in the vault, say
  "I don't find this in the vault" and ask.
- Match established spellings exactly — search the vault before writing any proper noun.
  (Watch faction names: The Crusade vs. The Resistance, Ecclesia Solari, House Aurum /
  Argentum / Cuprum, Blood Horde, Cult of the Goddess Whose Name Is Night, etc.)
- When uncertain, ask. A question always beats a plausible fabrication.

## Where things go
- Player-facing session recaps: `Session Notes/Session NN Notes.md` -- never `Session NN - Title.md`.
  Leave the frontmatter title blank after the colon (`title: "Session NN:"`); my players name the
  sessions themselves.
- Magic item recipes: `Magic Items/Recipes/<Item Name>.md`
- Session prep (DM-only): `Private Notes/Session Prep/Session NN - Prep.md`

## Style
- Player-facing voice: third person, past tense, narrative chronicle.
- `[[wikilinks]]`: hanging links to pages that do not exist yet are fine and useful -- they let me
  create the note later. What matters is the NAME: search the vault first and match the established
  spelling exactly, and never link a proper noun you invented.
