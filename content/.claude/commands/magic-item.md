---
description: Generate a balanced, rules-accurate magic item recipe grounded in my crafting system
argument-hint: [an item name, OR a hard component like "Beholder Eye"]
allowed-tools: Read, Write, Agent, SendMessage
---
Request: $ARGUMENTS

You generate a Magic Item Recipe for me (the DM). The Worldsmith drafts it and reads the
mechanical tables itself; you relay, and bring the recipe to me for approval. Be precise; no
in-character dialogue.

1. **Pick the mode from my input.**
   - An ITEM NAME → Item-to-Recipe: the full recipe gets generated.
   - A HARD COMPONENT (a monster part, e.g. "Beholder Eye") → Component-to-Recipe: the
     Worldsmith first suggests 3 suitable items, one line of rationale each, and STOPS; I choose
     one before the full recipe is generated.
   - Ambiguous → ask me which I meant before launching anything.
2. **Launch the Worldsmith** with my request and the recipe brief below. It reads these itself,
   as exact lookups, never approximated:
   - `C:\Users\mehul\DND\DesignLibrary\Export\Magic Item Crafting System.md` — the "DM Guide:
     Balancing the System" table (Costs, Time, DC, Magic Levels).
   - `C:\Users\mehul\DND\DesignLibrary\Export\Magic Item Categories.md` — the "Quick Decision
     Flowchart" for Category (A–I) and rarity if I didn't give one.
   - `C:\Users\mehul\DND\DesignLibrary\Export\Narrative Magic Items.md` — narrative grounding.
   - This campaign's tables in `Private Notes/Meta Notes/` (rarity tracking and our distribution
     table). Where a campaign table and the library disagree, the campaign table wins and the
     Worldsmith says so.
   - Two or three existing `Magic Items/Recipes/` files for format, and the vault pages for any
     campaign-specific source, crafter or material the item touches.
   Relay the draft to me; send my revisions to the same Worldsmith with SendMessage.
3. **Launch the Continuity Auditor** once, on the draft I've accepted: House Rules compliance
   (`Administrative/House Rules.md`; homebrew items are allowed), the numbers against the
   tables, naming, and player/DM leaks. Significant findings come to me; Minor ones go back to
   the Worldsmith and are listed in one line.
4. Ask me once whether the players have discovered this recipe: `draft: false` if so,
   `draft: true` if not. A recipe is a single new page, so on my approval write it yourself to
   `Magic Items/Recipes/<Item Name>.md`, following `.claude/rules/vault-writing.md`, and run the
   lint script. Report the path. No commit or push.

---

Recipe brief to hand the Worldsmith (it holds this only for the duration of this task):

**Grounding rules**
- All costs, times, DCs, magic levels, and category bands come from the tables named above.
  NEVER invent or approximate a number that contradicts them.
- Standard D&D 5e monster abilities and CR may come from general 5e knowledge. Anything
  campaign-specific — in-world sources, crafters, materials, factions, locations — must come
  from the vault; if it isn't there, say so and ask. Prefer a vault homebrew statblock over the
  standard one.
- Choose a Hard Component whose CR fits the item's Category (Minor Common → ~CR 1/4–2; Major
  Legendary → CR 17+) and whose ability/lore is thematic (e.g. a Displacer Beast for a Cloak of
  Displacement). Keep the Harvest DC (15 + CR/2) neither trivial nor impossible for the party's
  level — unless the vault specifies otherwise.

**Output template** (match the formatting of existing recipe files)
```
[Item Name] ([Category] – [Rarity])
Type: [Single / Limited / Charged / Permanent]
Hard Component: [Specific Part] (Monster Name, CR [X])
Soft Components:
- [X] Levels of [School] Magic.
- [X] gp of reagents ([flavor description of the reagents]).
The Ritual: [Time], [Tool Proficiency] (DC [X]).
Steps: 3–6 numbered, imperative steps. No flowery prose.
```
Any step that takes time carries a DURATION in real units — (2 Hours), (1 Day), (3 Days), never
an abstract index like (Day 1). Durations must sum to the total ritual Time from the balance
table, counting a crafting day as 8 hours (descriptive time inside prose, "over several hours,"
is fine). Each step connects the hard component and reagents through the physical logic of the
craft — Distill, Etch, Embed, Braid, Channel, Seal. Style reference (Rope of Climbing): "Soak
the giant spider silk in dissolved lodestone and quicksilver; braid it while channeling 2
Levels of Transmutation to retain flexibility; knot at 1-foot intervals with Weaver's Tools to
anchor the animation; dust the final knot with reagent residue to seal it."
