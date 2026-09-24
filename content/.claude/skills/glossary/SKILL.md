---
name: glossary
description: Generate the proper-noun word lists the dnd-audio-transcription pipeline needs for Whisper hotword biasing and correction. Two modes -- refreshing the thin master glossary (PCs + campaign-central factions/NPCs, rarely) and building a per-session cast list (session-local names, every session). Triggers on "update the glossary," "build the session terms list," "what names does the transcription need for session NN," "refresh the master glossary."
allowed-tools: Read, Glob, Grep, Agent, Write, Edit, Bash
---
You generate the two word lists the **dnd-audio-transcription** pipeline (sibling project,
`C:\Users\mehul\DND\dnd-audio-transcription`) needs for Whisper hotword biasing and
name-correction. You ground every spelling through the **Loremaster** (never invent or guess a
name) and always show me the list before writing it -- these files feed a pipeline outside the
vault, but the same "ask, don't invent" discipline applies.

## Why two lists, and why the master one stays thin
Confirmed directly with the transcription pipeline (its `scripts/vocab.py`): Whisper hotwords are
re-fed to the decoder every 30s window and share a hard ~448-token budget with the prompt/output,
so `vocab.py` enforces a strict cap (`DEFAULT_BUDGET=200`, ~33 names) and tiers what it spends that
budget on, most important first: manual > core PCs > **this session's cast** (protected, up to 60%
of budget) > repeat-offenders > recency > generic glossary importance ranking (last resort).
A big rich `canon_terms.tsv` can't crash or overrun anything -- correction (Layers 2-4) scans the
full glossary with no token limit at all, so richness never hurts there. But on the *hotword* side,
an oversized master list dilutes the last-resort "importance" tier: it ranks globally, with zero
awareness of what's actually in a given session, so budget can go to a major NPC who isn't even in
play this week over a minor one who is. The fix already built for this (vocab.py's session-cast
tier) is exactly the per-session list this skill produces -- so:
- **Master list** (`glossary/canon_terms.tsv`) stays to things true across MOST sessions: the
  five PCs, plus only factions/NPCs/locations genuinely campaign-central (currently the
  importance=high factions). Refresh rarely, only when the stable cast changes.
- **Session list** (`state/session_terms/session-NN.terms`) carries everything session-local --
  one-offs, this-arc NPCs, this-session locations/items. Build it every session from prep notes.
  These names do **not** need to exist in the glossary at all -- plain canon-spelled strings are
  fine (confirmed: `vocab.py`'s `read_terms_file` takes raw lines, no cross-reference).

## Always
- Ground every spelling via the **Loremaster** (read-only spawn) -- never guess a proper noun or
  its exact casing/punctuation.
- Cross-check against `glossary/excluded_terms.txt` in the transcription repo before proposing any
  term: it records names Mehul already ruled out as ordinary-word risk (e.g. "The Crusade," "The
  Resistance" -- generic phrases indistinguishable from normal speech). Never re-propose an
  excluded term or alias.
- Show me the exact diff or list before writing anything. Nothing here auto-writes.
- Write straight into `C:\Users\mehul\DND\dnd-audio-transcription\...` (confirmed acceptable --
  this is a technical export, not vault canon, and that project's own `CLAUDE.md` already
  documents `glossary/canon_terms.tsv` as "produced by the vault's lore agent"). Never `git
  commit`/`push` there -- that project's own rule is commits/pushes are Mehul's explicit,
  separate step.
- Never touch anything inside the vault beyond reading it for grounding.

## Mode A -- Refresh the master glossary (rare; only on explicit request)
1. Read the current `glossary/canon_terms.tsv` and `glossary/excluded_terms.txt` in the
   transcription repo to see what's there and what's already excluded. Note each existing term's
   `known_mishearings` value (7th column, pipeline-curated, not lore-sourced) -- these must be
   preserved on refresh, the same as exclusions.
2. Spawn the **Loremaster**: ask for (a) the full party roster with exact canonical spellings and
   common nicknames/aliases (cross-check `speakers.yml` in the transcription repo for the
   player->character mapping first so you ask about the right five names), and (b) every faction/
   NPC/location genuinely central to the WHOLE campaign (not one arc) -- canonical spelling +
   common aliases for each.
3. Draft rows in the existing rich format (`term  category  pronunciation  aliases
   common_word_risk  importance  known_mishearings`), keeping the header comment block intact.
   Default categories: PCs -> `character`, importance `high`; central factions -> `faction`,
   importance `high`. Only include a non-PC, non-faction row (an NPC/location/item) if it's
   unmistakably campaign-central -- when in doubt, leave it for the session list instead and say
   so. Leave `known_mishearings` untouched from step 1 for any surviving term -- never draft or
   infer a value for it yourself, it's Mehul/pipeline-curated only.
4. Before showing me anything, re-apply `glossary/excluded_terms.txt` as a final filter pass over
   the full drafted set (both `[rows]` terms and `[aliases]`) -- confirmed with the transcription
   session that on a full refresh, exclusions must be re-applied after drafting or they silently
   come back (step 2's pre-check alone isn't enough if a term resurfaces via the Loremaster brief
   under different framing). Drop any match.
5. Show me the full proposed file content as a diff against the current one. Call out anything
   you're dropping from the current file and why (moving to session-scope, excluded, or genuinely
   no longer relevant) -- including whether any row carrying a non-empty `known_mishearings` value
   is being dropped, since that discards curated data, not just a name.
6. On my approval: write the file, then run `python scripts/glossary.py build --tsv
   glossary/canon_terms.tsv --out glossary/canon_terms.txt` in the transcription repo to
   regenerate the derived term list. Report what changed; do not commit.

## Mode B -- Build a session's cast list (routine; every session)
1. Confirm the session number (infer from the latest `Private Notes/Session Prep/Session NN -
   *.md` file if I don't say one; ask if ambiguous).
2. Spawn the **Loremaster** with that session's prep note(s) (and, if the session already
   happened, note that prep is *not* canon and may not reflect what actually occurred -- this list
   is about what's *likely to be said*, not a canon claim): ask for every proper noun (NPC,
   location, item, faction, event -- **excluding the five PCs**, already covered by the pipeline's
   own "core" tier) likely to come up, ranked most-important/likely first, spelled exactly as
   canon.
3. Trim to at most ~25 names. Cross-check against `glossary/excluded_terms.txt` and drop any
   ordinary-word-risk term it flags.
4. Show me the ordered list before writing.
5. On my approval: write one name per line, most important first, to
   `C:\Users\mehul\DND\dnd-audio-transcription\state\session_terms\session-NN.terms`. These are
   plain strings -- no need to force them into `canon_terms.tsv` format or add them to the master
   glossary.
