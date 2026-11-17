---
name: proto-map
description: Build a plain, draggable battlemap layout prototype for working out what a fight's map mechanically needs, before I draw it in a map editor. Triggers on "proto-map," "prototype map," "mock up the battlemap," "work through the map for this fight."
---

Make a working layout tool for one or more fights. It answers what has to be on the map and where: footprints, distances, cover, exits, reach, and areas of effect. It is not art. Keep every graphic a flat, labeled shape on a 5-ft grid, and never add texture, drawn terrain, or decorative styling. That part happens in my map editor.

## Steps
1. Work from what we've agreed for the fight: the prep doc or this conversation. Don't invent terrain the fight doesn't use. If a fight's mechanics don't depend on a feature, mark it optional or leave it out, and say so.
2. If something the layout depends on is undecided (map size, entrances, starting positions), ask me one plain question and state the default you'll use.
3. Copy `template.html` from this skill's folder into the session scratchpad and edit only the block between `EDIT ONLY THIS CONFIG` and `END CONFIG`, plus the `<title>`. Include:
   - One map per fight, with every combatant at its correct footprint (Medium/Small 5, Large 10, Huge 15, Gargantuan 20).
   - The terrain that matters mechanically, labeled by what it does.
   - An overlay for each reach or area of effect that affects positioning (`radius` or `cone`, at the real distance).
   - A `state` checkbox for each alternate starting setup.
   - Short "Must have" notes listing what the final map needs.
   - Map sizes to compare, in `sizes`.
4. Set the `<title>` to a two-to-four-word name for the fights. Publish with the Artifact tool, using a new file name per set of fights so earlier maps keep their links. Use `icon: "map"` on first publish.
5. Give me the link and name anything you couldn't check. Tell me it's private, and warn me not to share it with players if it shows spoilers.

## Rules
- These maps are DM-only prep. Never save them under `Images/`, which publishes regardless of draft state, and don't write them into `Session Notes/`.
- A layout is not canon. If it needs a new permanent place, flag it to me for the `lore` skill.
- If we settle a map size or layout that differs from the prep doc, update the prep file (it is DM-only, so write it directly) and tell me what changed.
