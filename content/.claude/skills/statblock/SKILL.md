---
name: statblock
description: Enter an approved stat block into D&D Beyond as a homebrew monster (name ending " - HB") through Chrome, so it can be used in the encounter builder. Use after I approve a stat block, or when I say "put this on D&D Beyond," "make the HB version," "update the homebrew monster."
---
Create or update a homebrew monster on D&D Beyond from a stat block I have approved. Only enter
what was approved; don't adjust numbers on the way in. The name always ends with ` - HB`.
Stat blocks follow `Administrative/House Rules.md` (2024 rules; no banned spells).

Load the Chrome tools first (the `claude-in-chrome` skill), open a new tab, and work mostly
through page scripts and page text. **Avoid screenshots**: they time out on these pages.

## Rules that prevent the known failures
- After every `navigate`, wait about 3 seconds before reading or scripting the page.
- Never click something that navigates and keep running script in the same call. Click, end the
  call, wait, then continue; or navigate straight to the target URL.
- Find fields by id (`document.getElementById('field-<name>')`) and guard for null. Wrap values
  in `String(...)` when dumping them.
- To set a field: assign `.value`, dispatch `input` and `change` events, and also
  `jQuery(el).trigger('change')`.
- Tool output that includes cookie or query-string data is blocked. Verify with yes/no checks
  (`field.value.includes('…')`) or with page text, not by dumping the form.
- Do not trigger confirm dialogs (for example Delete buttons).

## Create
1. Go to `https://www.dndbeyond.com/homebrew/creations/create-monster`, choose **Create from
   Scratch** (lands on `…/create-monster/create`).
2. Main fields, by id `field-<name>`: `stat-block-type` (choose the 2024 / 5.5e option),
   `Name`, `monster-type`, `size`, `alignment`, `challenge-rating`, `armor-class`,
   `passive-perception`, `average-hit-points`, `hit-points-die-count`, `hit-points-die-value`,
   `hit-points-modifier`. Dropdowns take numeric option values: list each select's options and
   match by label; never assume an id from a previous monster.
3. Ability scores: seven inputs with hashed names, in order Initiative Bonus, STR, DEX, CON,
   INT, WIS, CHA. Identify each by the label text of its parent element before filling.
4. Multi-selects (`monster-saving-throw`, `damage-adjustment`, `condition-immunity`): set
   `option.selected` on the matching options, then fire `change`. `languages-note` is plain text.
5. Long text fields are TinyMCE editors (`special-traits-description`, `actions-description`,
   `bonus-actions-description`, `reactions-description` where present,
   `monster-characteristics-description`). For each:
   `tinymce.get(id).setContent(html)`, fire the editor's `change`, set the hidden textarea's
   `.value` to the same html, then `tinymce.triggerSave()`.
   Entry format: `<p><em><strong>Name.</strong></em> text</p>`, with `<em>Hit:</em>` style labels.
6. Clear the placeholder text D&D Beyond puts in the long fields you are not using.
7. Click **Create Monster**. The page redirects to
   `/homebrew/creations/monsters/<id>-<slug>/edit`. Note the id.
8. Speed, skills, senses and languages are separate pages, added after creation:
   `/monster/movement/create/<id>`, `/monster/skills/create/<id>`,
   `/monster/senses/create/<id>`, and the "Add a language" link on the edit page. Fill each
   form's fields, read the option labels to pick values, and click Save. One page per entry.
9. Back on the edit page, click **Save Changes**.

## D&D Beyond tags (use them; I want tooltips and rollers)
- Conditions, spells, skills: `[condition]Poisoned[/condition]`, `[spell]…[/spell]`,
  `[skill]…[/skill]`.
- Rollers: `[rollable]+5;{"diceNotation":"1d20+5","rollType":"to hit","rollAction":"Dart"}[/rollable]`
  (same pattern for damage, with `"rollType":"damage"` and the damage type). This renders
  correctly. `[roll]…[/roll]` and `data-dicenotation` spans do not.

## Update an existing monster
Open `/homebrew/creations/monsters/<id>-<slug>/edit` (the Edit link on its public page), change
the fields the same way, **Save Changes**. Renaming changes the slug but not the id.

## Verify and report
Reload the public page (`/monsters/<id>-<slug>`) and read its text: name ends ` - HB`, AC, HP,
speed, abilities, each trait and action present, tags rendered and not shown raw. Report the
public URL, anything that didn't render as intended, and that I should test the rollers in the
encounter builder (they can't be confirmed from here). Add the creature's name and URL to the
Encounters section of the session's prep file.

## If it fails
If the same step fails twice, stop automating. Give me the stat block as a paste-ready sheet in
the form's field order (main fields, abilities, saves and immunities, then each long field as
ready-to-paste text with the tags above, then the speed, skill, sense and language entries),
and say which step failed and what the page did.
