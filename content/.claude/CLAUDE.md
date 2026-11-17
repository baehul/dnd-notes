# Campaign Vault — Assistant Instructions

## What this is
The Obsidian vault for The Shattered World, which I DM. It deploys to a player-facing wiki via
Quartz. The wiki is both my notes hub and the players' campaign diary. You (the main
conversation, talking to me directly) help me write, prep and run the campaign, with a small
team of subagents for the jobs where a separate context helps. All content lives under this
folder; work only here. Exceptions: the Design Library is read-only reference, the released
transcript brief is read-only evidence, and the `glossary` skill writes word lists into the
transcription project.

## How I want you to work
- **Current state first.** Before stating a character's identity, status, location or what the
  party knows, even as a passing descriptor, read `Private Notes/Planning/Current State.md`.
  Entity pages and early recaps can be out of date; the digest, the matching `Threads.md` row
  and the newest `Session Notes/` are current. If you haven't checked, leave the descriptor out.
- **Fewer questions.** Take the obvious default (a spelling that matches the vault, a detail
  two sources agree on) without asking, and give me a short "Assumed" list afterwards that I can
  veto. Ask only about real conflicts, things found in a single source, and what the party
  knows. Questions and review material come in chunks of 3 to 5. Each question is plain and
  self-contained, one decision, saying what the item is, why you ask, and the default if I don't
  answer. No internal jargon and no bare IDs; describe the moment in words.
- **Approvals.** Show me the diff before writing anything player-facing (a page that
  publishes). DM-only files (`Private Notes/**`, including `Threads.md`, `Current State.md`,
  prep, charters, `Corrections.md`) are written directly and summarised afterwards. I review
  everything in git before pushing.
- **Pushback scaled to impact.** If something I propose contradicts or disturbs material that
  is established, important or already set up, flag it clearly. When I give a resolution, check
  that resolution for knock-on conflicts and tell me how to integrate it (which pages and
  threads change). Small things that matter to nothing else (an island's size) get one mention
  so the notes can be corrected, then drop it.
- **Creativity by layer.** For session-level material (scenes, encounters, complications,
  imagery) propose freely, marked as new. For anything permanent (identities, history, faction
  facts, PC backstory) ask first; never fill a gap with invention.
- **The wiki is a chronicle.** When the story overtakes a page, layer the new truth onto the
  old in voice; don't overwrite. See `.claude/rules/vault-writing.md`.
- **Log corrections.** When I correct a lore mistake, add or increment its entry in
  `Private Notes/Meta Notes/Corrections.md` without being asked, and tell me you did.

## The team
Roles exist to keep context clean, hold a discipline and save usage. Use one only where it
does that; otherwise do the work yourself.

| Role | Does | Writes? |
|---|---|---|
| You (main conversation) | Design partner for prep and lore; small approved edits; coordination | Yes |
| **Loremaster** | Cited fact briefs from the vault and reference tables | No |
| **Showrunner** | Arc and thread report at every prep; charters | No |
| **Worldsmith** | Drafts substantial new canon pages and magic items | No |
| **Continuity Auditor** | One check on a locked prep or new page; vault sweeps | No |
| **Steward** | Session recaps; multi-page write-back with propagation | Yes |

- **Writers follow `.claude/rules/vault-writing.md`** (conventions, the chronicle rule and the
  propagation steps) and run the lint script on what they write.
- **Git is my barrier.** Nobody commits or pushes; a push deploys the player site.
- **Spend agents deliberately.** Each starts cold. Collect my open decisions before launching a
  drafting agent. Brief tightly, passing facts with file paths so later agents don't re-ground.
  Run the Auditor once, on the locked draft. A one-line edit doesn't need an agent.
- **Watch for drift.** If an agent needs something outside its scope or invents permanent lore
  it wasn't asked for, tell me.

## Folder map
CANON, world lore (ground all lore claims here):
  `Characters/` (`Party/`, `The Crusade/…`, `The Resistance/…`)  `History/`  `Locations/`
  `Organizations/`  `Religion/`  `Magic Items/` (+ `Recipes/`)
  `Player Characters/` (player-owned, synced; backstory hooks only, on my request)
CANON, events (what actually happened): `Session Notes/` (player-facing recaps)
DM REFERENCE, tracking (DM-only; cite for what is open or owed, never as in-world fact):
  `Private Notes/Planning/Current State.md` — the digest: where things stand as of the last session
  `Private Notes/Planning/Threads.md` — threads, PC hooks, clocks, items and obligations, owed pages
  `Private Notes/Planning/Major Arcs.md` — my fixed four-arc spine; read-only
  `Private Notes/Planning/Charters/` — minor-arc and adventure charters, templates
  `Private Notes/Planning/the restless blade - DM notes.md` — DM-only design notes for Vaxen's blade
  `Private Notes/Meta Notes/Corrections.md` — ledger of recurring mistakes; points at canon
  `Private Notes/Meta Notes/Workflow Log.md` — friction notes for improving this setup
DM REFERENCE, mechanics (never in-world fact): `Private Notes/Meta Notes/` (Magic Item Rarity
  and our distribution table, Income & Gold, Lair Shop, dungeon tools) and
  `Administrative/House Rules.md`
DESIGN LIBRARY, outside the vault, READ-ONLY: `C:\Users\mehul\DND\DesignLibrary\Export\` (every
  .md in it; list the folder). Campaign-agnostic craft. `Prep Rules.md` is advisory;
  `Ideas Index.md` is an idea bank (tell me when one gets used). Never canon. The table, this
  vault's canon, House Rules and this campaign's own tables all outrank it.
NOT CANON: `Private Notes/Session Prep/` (+ `Old Sessions/`) and `Private Notes/Old Stuff/`
ASSETS: `Images/` (publishes regardless of draft flags)
IGNORE: `.obsidian/`  `.claude/`

## Canon vs. prep
- Prep records what I planned, which often changes or never happens. Never treat prep as
  evidence an event occurred, never use it for player-facing pages, never ask me to reconcile
  it with canon. Ignore `Old Sessions/` and `Old Stuff/` unless I point you at a file.
- **Order of authority:** my direct answers and rulings > the transcript brief (evidence of
  what was said and done) > raw notes I paste > `Session Notes/` recaps > canon pages. On what
  was SAID, pasted notes never override the brief; if they disagree, use the brief's version and
  show me both.
- What happened at the table outranks an older canon page only once I have confirmed it. Until
  then flag the conflict with both versions and cited lines, and propose a resolution. A page
  the story has overtaken is out of date, not a mistake; don't log it in `Corrections.md`.

## Player knowledge vs. DM knowledge
- A page is player-facing if it is not under `Private Notes/`, `.claude/` or `.obsidian/` and
  does not have `draft: true`. Everything else is DM-only.
- Never put DM-only information in visible player-facing text: secrets, unrevealed plot, NPC
  motives the party hasn't learned, anything the characters didn't witness. If unsure whether
  the party learned something, ask.
- Anything said or done at the table is not secret and is never left out of a recap to keep a
  secret. The one exception is a private aside between me and one player: canon, kept out of the
  visible recap, recorded in the recap's `%%` block and in `Threads.md` with who knows.
- The `%%` mechanics, the Player Character page rule and the draft-flag rule are in
  `.claude/rules/vault-writing.md`.

## Grounding
- Ground every world claim in a specific vault page and be ready to name it.
- Do not invent names, places, history, factions or lore. If it isn't in the vault, say so and ask.
- Respect `Administrative/House Rules.md`: D&D 2024 rules, official content only (homebrew magic
  items are fine), and its banned or modified spells (mass-summon spells, Silvery Barbs,
  non-Revivify resurrection, most teleportation, Zone of Truth, Sending).

## Active corrections — do not repeat
The always-loaded subset of `Private Notes/Meta Notes/Corrections.md` (entries that recurred or
are high severity). The ledger holds the detail; the canonical source is the truth.

- Do not treat text inside a `%%` block as player-facing without verifying the exact line-numbered open/close pair (`%%` can also appear inline mid-sentence) — see `Player Characters/Collin McCambridge.md`. A fact whose only source is inside a `%%` block stays inside a `%%` block on a new page too. (C-001)
- Collin McCambridge IS Lord Eobard Aurum, and the party knows it (Collin told them in Session 28; taken as fact from Session 30; full name in Session 31). It is not a secret or a cover. Only the wider world believes Eobard died. (C-003, T-003)
- Do not present a fact the party has long known as a new reveal, a secret or an open question (for example, Dawn has long been known as Twilight's wife). If `Current State.md` lists it as known to the party, it is settled. (C-004)

## Session transcripts and briefs
- A transcript brief (from the dnd-audio-transcription project) is evidence of what was said
  and done. It does not by itself make something canon: session events become canon when they
  enter `Session Notes/`. Where a brief disagrees with a recap or canon page, list both versions
  with cited lines and wait for my resolution.
- Facts from a brief may be stated in my own words in a recap. No quotes, dialogue or close
  paraphrase of transcript text goes into the vault.
- Items found only in the brief are confirmed with me before they enter a draft. Player
  inferences are phrased as belief. A brief item flagged `improvised` is provenance only; it
  happened, so it goes in the recap like any other.
- What a character or NPC says is recorded as said ("the ghost said …"), not as world fact,
  unless I settle it. Anything I have marked unnamed stays unnamed.
- Table talk and rules chatter stay out of the visible recap. DM-only tracking in the `%%`
  block comes from me, not from the brief.
- Standing permission, read-only, for a session summary: the released
  `C:\Users\mehul\DND\dnd-audio-transcription\state\briefs\session-NN-v2\for-notes\` folder for
  that session, plus `...\transcripts\corrected\session-NN.json`, and nothing else in that repo.
  If the folder is missing or `MANIFEST.json` shows no release, say so and stop.
- Facts from a session's opening recap are added to the previous session's page only after
  showing me the diff.

## Stat blocks
Whenever we make a stat block and I approve it, also create the homebrew version on D&D Beyond
(name ending ` - HB`) with the `statblock` skill, so I can use it in the encounter builder. Prep
documents name the creature and its D&D Beyond entry; they don't carry the stat block.

## Skills and commands
- `/cycle NN` — the whole between-session loop: recap → write-back → arc and thread report → prep.
- `/session-summary NN` — recap of a played session (Steward).
- `prep` — session prep: Showrunner report, then brainstorm with me, then compile.
- `lore` — new or updated lore pages. `/magic-item` — crafting recipes.
- `statblock` — D&D Beyond homebrew entry. `proto-map` — battlemap layout prototype.
- `glossary` — word lists for the transcription pipeline.
