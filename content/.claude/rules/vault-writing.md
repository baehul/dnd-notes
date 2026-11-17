# Vault writing conventions

The single copy of how text is written into this vault. Anyone who writes or drafts vault text
(the main conversation, the Steward, the Worldsmith) follows this file. Other instruction files
point here instead of restating it.

## Who sees what
- A page publishes to the players unless it sits under `Private Notes/`, `.claude/` or
  `.obsidian/`, or its frontmatter has `draft: true`. There is no `publish:` key; never use one.
- Every publishing page carries `draft: false` explicitly. A new page gets `draft: false` if the
  players already know the thing, `draft: true` if they don't. If that isn't known, ask once.
- Session recaps always publish (`draft: false`).
- Images, maps and PDFs under `Images/` publish regardless of any page's draft state. Nothing
  secret goes there.

## `%%` blocks
- `%% ... %%` hides text from the published site. On wiki pages it holds DM-only lore; on a
  session recap it holds the `### DM Secrets & Context` section.
- On `Player Characters/` pages `%%` means something different: it is the player's private
  background, hidden from the site and the other players, known to that player and the DM. Those
  pages sync from the players' Google Docs. Never edit player-authored text; only the final
  `# Local Notes` block is the DM's.
- Before treating any text as player-facing, find the enclosing `%%` open and close lines by
  line number. One block can span many headings, and `%%` also appears inline mid-sentence, so
  neither headings nor a simple count is enough.
- A fact whose only source is inside a `%%` block stays inside a `%%` block wherever it is
  written next.
- Every block opened is closed. Text inside a wiki page's `%%` block stays in the wiki's
  in-world voice: no writer's notes, provenance, session citations or open questions. Those go
  in the page's Local Notes or in `Private Notes/Planning/Threads.md`.

## Names and links
- Search the vault before writing any proper noun and match the established spelling exactly.
- `[[wikilinks]]` to pages that don't exist yet are fine, as long as the name is established in
  the vault. Never link a name that was invented in a draft and not approved.
- The two sides: **The Crusade** (Ecclesia Solari; House Aurum, House Argentum, House Cuprum,
  under `Organizations/The Crusade/Upper Crust Houses`; Golden Sails Trading & Shipping Company)
  and **The Resistance** (the Ancient Ones; the Blood Horde; the Cult of the Goddess Whose Name
  Is Night). Religions (Blood Gods, Old Path, Solari Faith, Way of Night) live under `Religion/`,
  separate from the factions that follow them. A House as an institution lives in
  `Organizations/`; its members live in `Characters/`.

## Voice
- Player-facing text: third person, past tense, narrative chronicle.
- No review scaffolding in the vault: strip `[NEW]` markers, provenance notes and questions.
- Recap bodies carry no quotes, dialogue or close paraphrase of transcript text, and no game
  mechanics (turns, feet, rolls, checks, saves, slots, DCs, hit points).
- Leave a recap's title blank after the colon (`title: "Session NN:"`). The players name sessions.

## The chronicle rule (when the story overtakes a page)
The wiki is a campaign diary as well as a reference. When events change what a page says, layer
the new truth onto the old in the chronicle's voice; don't erase what was once believed.
- Example: not "Status: alive", but "Though once believed dead, the party discovered that he
  lives under the name of Collin, fighting alongside the Resistance."
- Visible text only for what the party or the wider world has learned. What only the DM knows
  goes in the page's `%%` block, in voice.
- Old session recaps are the record of their moment and are not rewritten.
- **What earns a place on a page.** A wiki page is background on its subject, not a log of
  its dealings with the party. Change the page only when the story changes what the subject
  fundamentally is: identity, alive or dead, allegiance, condition, who rules or owns it, what
  it is now known to be. "The party met him, he hired them, someone said this about him" is not
  lore; it stays in the session recaps and `Threads.md`, or in a hidden note if the DM needs it
  on the page. A fact about one character goes on that character's page, not on the pages of
  everyone it touches (Magnus telling the world Eobard died belongs on Eobard's page).
  Short-term situations (someone is missing after last session, where a person is right now,
  who currently carries an item) are not lore either; item pages stay item cards.

## Propagation (every change, however small)
A change is not finished until every page that states the changed fact agrees with it.
1. Name the fact that changed (identity, alive or dead, allegiance, location, ownership, who
   knows what, a name or spelling).
2. Search the vault for every page that states it: the entity's own page, pages that link to it,
   the pages of its house, faction, location and relations.
3. Update each one under the chronicle rule, with reciprocal wikilinks where a relation is new.
4. Update `Private Notes/Planning/Current State.md` and the matching `Threads.md` row.
5. Report the list of pages changed, and any page deliberately left alone and why.

## File names
- Recaps: `Session Notes/Session NN Notes.md` (never `Session NN - Title.md`).
- Recipes: `Magic Items/Recipes/<Item Name>.md`.
- Prep: `Private Notes/Session Prep/Session NN - Prep.md`.
- Charters: `Private Notes/Planning/Charters/Minor Arc - <Name>.md`, `Adventure - <Name>.md`.

## After writing
Run `python .claude/scripts/vault_lint.py <file> [<file> ...]` from the vault root on every file
written, and fix what it reports before reporting the work as done. Never commit or push.
