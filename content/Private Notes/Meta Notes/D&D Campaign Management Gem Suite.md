## 1. The Lore Architect
* **Task:** Create New Lore (Characters, Locations, Factions).
* **Prompt Summary:** Acts as a neutral interviewer. It takes bulleted ideas, performs an iterative Q&A to flesh out details/secrets, and outputs a formatted Markdown file with public text and hidden (\%\%) DM notes.
* **Knowledge Files:** Full Campaign Wiki / Lore Export.
* **Example Interaction:** "I want to create a new location called 'The Sunken Grotto'. It's a cave near the cliffs with glowing moss and a hermit inside. Please flesh this out."

## 2. The Lore Maintainer
* **Task:** Update Existing Lore.
* **Prompt Summary:** Acts as a "Patch Manager." It identifies files needing changes, checks for lore conflicts (warning you if a retcon breaks history), and outputs "Patch Notes" containing full text blocks to copy/paste into Obsidian.
* **Knowledge Files:** Full Campaign Wiki / Lore Export.
* **Example Interaction:** "Update the 'Sunspire' file. We established last session that the Ecclessia Solari have taken it over. Please generate the updates."

## 3. The Campaign Scribe
* **Task:** Session Summaries.
* **Prompt Summary:** Acts as an Archivist. It ingests raw player notes, pauses to interview the DM about "Behind the Scenes" secrets, and generates a Wikipedia-style session log with separate sections for Loot, New NPCs, and hidden (\%\%) DM context.
* **Knowledge Files:** Full Campaign Wiki / Lore Export.
* **Example Interaction:** "Here are the player notes from last night: *Paste Notes* Help me summarize this."

## 4. The Session Strategist
* **Task:** Synthesize Session Prep.
* **Prompt Summary:** Acts as a Co-Pilot. It conducts a "Discovery Interview" (asking about strong starts, secrets, and monsters) and synthesizes the answers into an interactive Obsidian checklist with links to stat blocks and locations.
* **Knowledge Files:** Full Campaign Wiki / Lore Export.
* **Example Interaction:** "I need to prep for the next session. The party is currently resting in the vestibule of the Sunspire and I want them to find the Altar of Light."

## 5. The Narrative Artifact Consultant
* **Task:** Create Narrative Magic Items (Base Enhancements).
* **Prompt Summary:** Acts as a Homebrew Consultant. It prioritizes flavor over stats. It uses a 3-step loop: Generates 1 Prototype -> Asks Calibration Questions -> Generates 3 Variations. It categorizes items by "Scale" and "Variety" (Mood Setter, Personality Pump, etc.).
* **Knowledge Files:** [[Narrative Artifacts]], Full Campaign Wiki / Lore Export
* **Example Interaction:** "I want a 'Large Scale' item for the garden sector of the island. It should be a 'Mood Setter' that makes the area feel ancient and sleepy."

## 6. The Arcane Smith
* **Task:** Create Magic Item Recipes.
* **Prompt Summary:** Acts as a Game Balance calculator. It takes a "Hard Component" (monster part) provided by you and calculates the "Soft Costs" (Magic Levels, Gold, Ritual Steps) based on the item's power. It outputs step-by-step ritual instructions.
* **Knowledge Files:** [[Magic Item Crafting System]]
* **Example Interaction:** "I want a recipe for 'Gloves of Climbing'. The Key Component they found is a Mimic's Adhesive Gland. Please balance the recipe."