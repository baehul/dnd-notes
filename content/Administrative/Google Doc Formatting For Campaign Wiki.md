I am writing a tool to automatically sync Google Docs to our Campaign Wiki. You can structure your document however you like (backstories, session notes, etc), but you **must** follow these formatting rules so the tool can read your Google Doc.

# Google Doc Sharing

The Google Doc needs to be shared with my gmail or it needs to be publicly accessible via url with the ability to view.

As an example, the source google doc for this can be found here: [https://docs.google.com/document/d/1FKxwh-4thyKI8Ek-kT4yV9JLh-UJnyPmvwZy9B2SOi4/edit?usp=sharing](https://www.google.com/url?q=https://docs.google.com/document/d/1FKxwh-4thyKI8Ek-kT4yV9JLh-UJnyPmvwZy9B2SOi4/edit?usp%3Dsharing&sa=D&source=editors&ust=1767254357702608&usg=AOvVaw3wvLZ9J3RaCSyfSFxDss1M)

# Use "Styles"

**Do not** manually change font sizes to make headers (e.g., don't just set text to Size 24 and Bold). It looks fine here, but the tool will ignore it.

Instead, use the **Styles Dropdown** in the toolbar:

* Use **Heading 1** for major sections
* Use **Heading 2** for sub-sections
* etc.

# What NOT to do

These things will disappear:

* **NO Images:** Do not paste character art or maps into this doc. Send those files directly to the DM or upload them to the Discord.
* **NO Page Breaks:** The Wiki is one continuous scroll; page breaks are ignored.

# Links

You can do [[Links]] to link to reference pages such as existing notes within the campaign wiki,  characters you would like to be able to reference, or things you would like to give dedicated pages someday

**Example:**

> I talked to an NPC [[Lancaster Slickwhistle]] who has a page of background info. I also found out some new lore this session about the [[Crest Of Cinders]], a magic item that seems important but there’s no page for yet.

## Secrets & DM Notes (Hidden Text)

If you want to write something that is **hidden** from the public page (like a secret backstory element or a note for the DM), enclose the text in double percentage signs: \%\%. Everything inside the double percentage signs will be invisible on the final Wiki page. You can also comment out blocks of text.

**Example in Google Doc:**

> Everyone thinks I am a Bard. \%\% But actually, I am a Warlock in disguise.\%\% This part is visible again.

> \%\%

> This block of text will be hidden.

> I love writing secret lore.

> I am plotting to TPK the party and steal all their gold.

> \%\%

> This block of text is visible.

> I hate secrets.

> I love sharing loot with my party.

**Example Displayed on Wiki:**

> Everyone thinks I am a Bard. %% But actually, I am a Warlock in disguise. %% This part is visible again.

> %%

> This block of text will be hidden.

> I love writing secret lore.

> I am plotting to TPK the party and steal all their gold.

> %%

> This block of text is visible.

> I hate secrets.

> I love sharing loot with my party.

## Lists

Always use the standard **Bullet List** or **Numbered List** buttons.

* **Nested Lists:** You can press "Tab" to nest items.
  + Like this.

## Tables

Simple tables work well. **Do not merge cells**, as this breaks the format. Keep it a simple grid. Markdown requires tables to have a Header Row (titles at the top) so always use the first row of your table for labels (e.g., "Item Name", "Notes").

| Item Name | Weight | Notes |
| --- | --- | --- |
| Longsword | 3 lbs | Silvered |
| Potion | 0.5 lbs | Red liquid, smells like cinnamon |