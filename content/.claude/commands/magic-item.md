---
description: Generate a balanced, rules-accurate magic item recipe grounded in my crafting system
argument-hint: [an item name, OR a hard component like "Beholder Eye"]
allowed-tools: Agent, SendMessage
---
Request: $ARGUMENTS

You generate a Magic Item Recipe for me (the DM) by ROUTING the team — you do NOT read the
tables or draft the recipe yourself. The Loremaster pulls exact mechanical values, the
Worldsmith drafts the recipe applying them, the Continuity Auditor gates it, and the Steward
writes it. Relay between the agents (resuming a maker via SendMessage so it keeps its context)
and bring the recipe to me for approval. Be precise; no in-character dialogue.

1. **Pick the mode from my input.**
   - An ITEM NAME → Item-to-Recipe: the full recipe gets generated.
   - A HARD COMPONENT (a monster part, e.g. "Beholder Eye") → Component-to-Recipe: the
     Worldsmith first suggests 3 suitable items with a one-line rationale each, STOPS, and I
     choose one before the full recipe is generated.
   - Ambiguous → ask me which I meant before dispatching.
2. **Spawn the Loremaster** to pull the mechanics as exact table lookups (never approximated):
   - `Private Notes/Meta Notes/Magic Item Crafting System.md` — the "DM Guide: Balancing the
     System" table (Costs, Time, DC, Magic Levels). Values used EXACTLY.
   - `Private Notes/Meta Notes/Magic Item Rarity.md` — the "Quick Decision Flowchart" to assign
     Category (A–I) and rarity if I didn't give one.
   - `Private Notes/Meta Notes/Narrative Magic Items.md` — narrative grounding.
   - Plus the format of a few existing `Magic Items/Recipes/` files, and any campaign-specific
     sources/crafters/materials the item touches. If the vault differs from anything below, THE
     VAULT WINS — have the Loremaster flag it.
3. **Spawn the Worldsmith** with my request + the Loremaster's pull + the recipe brief below. It
   drafts the recipe (or, in Component mode, the 3 options first — relay them, get my choice,
   SendMessage it back). Relay the draft to me; SendMessage my revisions to the same Worldsmith.
4. **Spawn the Continuity Auditor** on the draft as a GATE: House Rules compliance
   (`Administrative/House Rules.md` — banned/modified spells; homebrew items are allowed),
   balance against the crafting tables, naming consistency, and player/DM leak. Relay findings;
   loop fixes back to the Worldsmith via SendMessage.
5. I decide. Ask whether the players have discovered this recipe yet — `draft: true` if not,
   `draft: false` if so. On my approval, spawn the **Steward** to write it to
   `Magic Items/Recipes/<Item Name>.md`. Report the exact path the Steward wrote. Do not commit
   or push — git is a separate step I trigger.

---

Recipe brief to hand the Worldsmith (it holds this only for the duration of this task):

**Grounding rules**
- All costs, times, DCs, magic levels, and category bands come from the Loremaster's table pull.
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
