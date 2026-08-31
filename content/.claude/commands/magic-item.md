---
description: Generate a balanced, rules-accurate magic item recipe grounded in my crafting system
argument-hint: [an item name, OR a hard component like "Beholder Eye"]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---
Request: $ARGUMENTS

You're generating a Magic Item Recipe for me (the DM). Be precise and mechanically
accurate. No in-character dialogue.

## 1. Load the rules first (before anything else)
Read these and treat them as the source of truth for all mechanics:
- `Private Notes/Meta Notes/Magic Item Crafting System.md` — especially the "DM Guide:
  Balancing the System" table (Costs, Time, DC, Magic Levels). Use these values EXACTLY.
- `Private Notes/Meta Notes/Magic Item Rarity.md` — use the "Quick Decision Flowchart" to
  assign the Category (A–I) and rarity if I didn't give one.
- `Private Notes/Meta Notes/Narrative Magic Items.md` — for narrative grounding.
Then skim a few existing recipes in `Magic Items/Recipes/` to match their exact format.
If the vault's tables or existing recipes differ from anything below, THE VAULT WINS.

## 2. Pick the mode from my input
- I gave an ITEM NAME  → Item-to-Recipe: determine appropriate components, generate the full recipe.
- I gave a HARD COMPONENT (a monster part, e.g. "Beholder Eye") → Component-to-Recipe:
  suggest 3 suitable items craftable from it, each with a one-line rationale, then STOP and
  let me choose one before generating the full recipe.
If it's ambiguous, ask which I meant.

## 3. Grounding rules for this task
- All costs, times, DCs, magic levels, and category bands come from the vault tables above.
  NEVER invent or approximate a number that contradicts them.
- Standard D&D 5e monster abilities and CR may come from your general 5e knowledge. Anything
  campaign-specific — in-world sources, crafters, materials, factions, locations — must come
  from the vault; if it isn't there, say so and ask. Prefer a vault homebrew statblock over
  the standard one.
- Choose a Hard Component whose CR fits the item's Category (Minor Common → ~CR 1/4–2;
  Major Legendary → CR 17+) and whose ability/lore is thematic to the item (e.g. a Displacer
  Beast for a Cloak of Displacement). Keep the Harvest DC (15 + CR/2) neither trivial nor
  impossible for the party's level — unless the vault specifies otherwise.

## 4. Output template (follow this structure; match the formatting of existing recipe files)
[Item Name] ([Category] – [Rarity])
Type: [Single / Limited / Charged / Permanent]
Hard Component: [Specific Part] (Monster Name, CR [X])
Soft Components:
- [X] Levels of [School] Magic.
- [X] gp of reagents ([flavor description of the reagents]).
The Ritual: [Time], [Tool Proficiency] (DC [X]).
Steps: 3–6 numbered, imperative steps. No flowery prose.
Any step that takes time carries a DURATION in real units — (2 Hours), (1 Day), (3 Days). Never an abstract index like (Day 1) or (Days 2–3). The durations must add up to the total
ritual Time from the balance table, counting a crafting day as 8 hours. The rule is about the
step's time label — descriptive time inside the step's prose ("over several hours") stays. Each step connects the hard
component and reagents through the physical logic of the craft — verbs like Distill, Etch,
Embed, Braid, Channel, Seal. Style reference (Rope of Climbing): "Soak the giant spider silk
in dissolved lodestone and quicksilver; braid it while channeling 2 Levels of Transmutation
to retain flexibility; knot at 1-foot intervals with Weaver's Tools to anchor the animation;
dust the final knot with reagent residue to seal it."

## 5. Finish
Show me the finished recipe. On my approval, save it to `Magic Items/Recipes/<Item Name>.md`.
Ask whether the players have discovered this recipe yet; if not, set `draft: true` in the
frontmatter so it stays DM-only until they find it.
