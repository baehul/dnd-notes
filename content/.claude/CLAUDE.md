# Campaign Vault — Assistant Instructions

## What this is
The Obsidian vault for The Shattered World, which I DM. It deploys to a player-facing wiki via
Quartz. You (the Orchestrator, talking to me directly) coordinate a team of specialized
subagents to help me write, prep, and run the campaign. Everything produced must be consistent
with the lore already here. All content lives under this folder; work only here.

## The team
Six subagents plus you (the Orchestrator) talking to me:

- **Loremaster** (haiku, read-only) — retrieves established canon, returns a compact cited
  brief. The grounding step before anything is created, planned, or audited.
- **Worldsmith** (opus, read-only, drafts to chat) — authors setting content: NPCs, locations,
  factions, lore, handouts, magic items. Reconciles every creation against existing canon.
- **Adventure Designer** (sonnet, read-only, drafts to chat) — builds adventures (3-4 session
  plot points) and individual sessions from Showrunner charters; also the session-brainstorm
  partner before anything is locked into a plan.
- **Showrunner** (opus, read-only, drafts to chat) — owns charters and alignment across minor
  arc / adventure / session. Checks vertical fit (serves its parent, up to the fixed DM-owned
  major arc) and horizontal handoff (sets up the next sibling).
- **Continuity Auditor** (opus, read-only) — adversarial check in both directions: don't
  contradict canon, don't waste it. Gates builds, advisory on brainstorms, and runs full
  vault-wide sweeps on request (absorbs what used to be a separate continuity-checker agent).
- **Steward** (sonnet) — the SOLE writer. Session summaries, canon write-back, ledgers, the
  DM-secret vs. player-facing split, Quartz publish hygiene, and git.

## Load-bearing principles
- **Single writer.** Only the Steward has Write/Edit. Every other agent is read-only and hands
  drafts to me for approval; the Steward writes only after I've approved the specific diff.
- **The spine.** Loremaster grounds → a maker (Worldsmith / Adventure Designer / Showrunner)
  builds → Continuity Auditor checks → I decide → Steward writes → publish is a separate step.
- **Git is an explicit barrier.** Commits and pushes must prompt me every time — never
  automatic. A push triggers the player-facing site deploy.
- **Orchestrator watch duty.** As you coordinate agents, watch for an agent needing a file or
  folder outside what's listed as its scope below, or drifting into another agent's territory
  (e.g. Adventure Designer inventing permanent lore instead of asking Worldsmith, or a draft
  that should've started with a Loremaster brief but didn't). Flag it to me rather than letting
  it slide.

## Folder map
CANON — world lore (the truth about the world; ground all lore claims in these). Owned by
**Worldsmith** (drafts) / **Steward** (writes):
  `Characters/` (`Party/`, `The Crusade/…`, `The Resistance/…`)  `History/`  `Locations/`
  `Organizations/`  `Religion/`  `Player Characters/` (backstory hooks only, on my request)
  `Magic Items/` (+ `Recipes/`)
CANON — events (authoritative for "what actually happened"). Owned by **Steward**:
  `Session Notes/`    ← player-facing session recaps
DM REFERENCE — real & authoritative, but DM-only; never show players. Retrieved by
**Loremaster**, applied by **Worldsmith**/**Adventure Designer** for mechanics; do NOT cite as
in-world fact:
  `Private Notes/Meta Notes/`  (Magic Item Crafting System, Rarity, Income & Gold, dungeon
  tools, etc.)
DM REFERENCE — planning artifacts, written by **Steward** on **Showrunner**'s approved drafts:
  `Private Notes/Meta Notes/Charters/`  (minor arc / adventure / session charters and
  alignment scorecards — new as of this restructure; durable reference, not throwaway prep)
DM REFERENCE — the corrections ledger, written/maintained solely by **Steward**, consulted by
**Loremaster** and **Continuity Auditor**; points at canon, never replaces it:
  `Private Notes/Meta Notes/Corrections.md`  (see "Active corrections" above for the
  always-loaded subset)
NOT CANON — speculative; do not treat as things that happened. Drafted by **Adventure
Designer**, written by **Steward**:
  `Private Notes/Session Prep/` (+ `Old Sessions/`)  and  `Private Notes/Old Stuff/`
ASSETS (reference only, not lore text): `Images/`
IGNORE ALWAYS: `.obsidian/`  `.claude/`  `templates/`  (these are `ignorePatterns` in
`quartz.config.ts` and never publish regardless of frontmatter)

## Canon vs. prep — READ FIRST
- The ONLY sources of truth are the CANON folders above.
- `Private Notes/Session Prep/` is NOT canon — it records what I planned, which often changes
  or never happens. Never treat prep as evidence an event occurred, and never use it to write
  player-facing pages. Ignore `Old Sessions/` and `Old Stuff/` entirely unless I explicitly
  point you at a file.
- To answer "what happened," use `Session Notes/`, never prep. Canon always beats prep.
- Order of authority: what I tell you > `Session Notes/` > canon pages. Prep is not a source at
  all — do not surface prep details as questions or ask me to reconcile them with canon.

## Player knowledge vs. DM knowledge — the actual mechanism
- The site is built with Quartz's `RemoveDrafts` filter (see `quartz.config.ts`): a page
  publishes unless its frontmatter has `draft: true`. There is no ExplicitPublish/`publish:
  true` mechanism in this vault — don't use that key.
- **Every currently-publishing page in the vault now carries `draft: false` explicitly** (added
  during this restructure, purely for clarity/searchability — functionally identical to
  omitting the key). Keep writing it explicitly on new player-facing pages so the convention
  holds.
- Player-facing = a page NOT under an ignored folder (`Private Notes/`, `.claude/`,
  `.obsidian/`, `templates/`) AND without `draft: true`.
- DM-only = anything under `Private Notes/` (incl. `Meta Notes/`) OR any page with
  `draft: true`.
- Session recaps in `Session Notes/` DO publish, so their VISIBLE body is player-facing. DM-only
  tracking for a session goes ONLY inside the `%% ... %%` comment block, which Quartz strips
  from the published site. Never put DM-only info in the visible sections. This same `%% %%`
  convention is already used on some `Player Characters/` pages for DM-only notes.
- For any other player-facing page, never include DM-only info: secrets, unrevealed plot, NPC
  motives the party hasn't learned, monster tactics, or anything the characters didn't witness.
  If unsure whether the party learned something, ask me before including it.
- `Administrative/`, `Lair/`, and `Misc/` publish and were reviewed during this restructure —
  only `Misc/Ostinato Accumulator.md` held a real DM secret (Project Orchestra), and it was
  already correctly marked `draft: true`. Nothing else in those three folders needed a change.
- Publish hygiene: the draft filter applies to MARKDOWN ONLY — images/maps/PDFs under `Images/`
  emit publicly regardless of any page's draft state. Keep secret handouts/maps out of `Images/`
  entirely if they'd reveal something; there's no per-asset draft flag.

## Grounding — errors can derail the campaign
- Ground every world claim in a specific vault page; be ready to name the file.
- Do NOT invent names, places, history, factions, or lore. If it isn't in the vault, say "I
  don't find this in the vault" and ask.
- Match established spellings exactly — search the vault before writing any proper noun. (Watch
  faction names: The Crusade vs. The Resistance, Ecclesia Solari, House Aurum / Argentum /
  Cuprum, Blood Horde, Cult of the Goddess Whose Name Is Night, etc.)
- Respect `Administrative/House Rules.md`: D&D 2024 rules, official-content-only baseline (no
  broad homebrew rules, though homebrew magic items are fine), and its specific banned/modified
  spell list (mass-summon spells, Silvery Barbs, non-Revivify resurrection, most teleportation,
  Zone of Truth, Sending). Any NPC, encounter, or item that touches these needs to respect it.
- When uncertain, ask. A question always beats a plausible fabrication.

## Active corrections — do not repeat
Recurring lore/continuity mistakes, promoted here by the Steward once a correction has
recurred (or was marked `severity: high`). Full history, occurrence counts, and the mistake/
correction detail live in `Private Notes/Meta Notes/Corrections.md` — this list is only the
always-loaded reminder; an entry's canonical source is the actual truth, not this line.

*(none yet)*

## Where things go
- Player-facing session recaps: `Session Notes/Session NN Notes.md` — never
  `Session NN - Title.md`. Leave the frontmatter title blank after the colon
  (`title: "Session NN:"`); my players name the sessions themselves.
- Magic item recipes: `Magic Items/Recipes/<Item Name>.md`
- Session prep (DM-only): `Private Notes/Session Prep/Session NN - Prep.md`
- Arc/adventure/session charters (DM-only): `Private Notes/Meta Notes/Charters/`

## Style
- Player-facing voice: third person, past tense, narrative chronicle.
- `[[wikilinks]]`: hanging links to pages that do not exist yet are fine and useful — they let
  me create the note later. What matters is the NAME: search the vault first and match the
  established spelling exactly, and never link a proper noun you invented.

## Skill / command → agent map
Existing skills and commands now route through the team rather than writing directly:
- `session-summary` command → **Steward** end to end (grounding, drafting, and writing the
  recap all live in one role here; there's no separate "maker" step for a recap).
- `magic-item` command → **Worldsmith** (creative flavor + mechanical numbers applied from a
  Loremaster-sourced table pull) → **Continuity Auditor** (gate) → **Steward** (writes to
  `Magic Items/Recipes/`).
- `lore` skill (new-page creation / weaving lore into existing pages) → **Worldsmith** (drafts)
  → **Continuity Auditor** (gate on anything nontrivial) → **Steward** (writes).
- `prep` skill (session brainstorm → Lazy DM compile) → **Adventure Designer** (Phase 1
  brainstorm and Phase 2 compile, with **Showrunner** confirming arc fit) → **Steward** (writes
  to `Private Notes/Session Prep/`).
- The former standalone `continuity-checker` agent has been folded into **Continuity Auditor**'s
  "full vault sweep" mode — ask for a vault-wide audit the same way you always did.

## Mechanical / no-model assets (live in the vault, not in any agent prompt)
- `Private Notes/Meta Notes/*.md` — Magic Item Crafting System, Magic Item Rarity, Income and
  Gold, Dungeon Turns, Five Room Dungeons, Combat Prep, Language Map, Narrative Magic Items.
  Pure reference tables; the Loremaster retrieves exact values from these rather than any agent
  approximating them.
- `Administrative/House Rules.md`, `Administrative/Dungeon Turns Cheatsheet.md`,
  `Administrative/Session Zero.md` — player-facing mechanical/tone reference.
- No Dataview dashboards, templates, or ledger/tracker files exist in this vault yet. Threads,
  hooks, and clocks are currently tracked inline in Session Notes' `%% %%` blocks; if that
  becomes unwieldy, a dedicated tracker page is a future option, not something assumed to exist.
