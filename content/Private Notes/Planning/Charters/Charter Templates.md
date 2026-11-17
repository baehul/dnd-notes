---
tags:
  - charter
  - template
---
# Charter Templates

DM-only. Templates for the planning hierarchy beneath the four major arcs in [[Major Arcs]]. The Showrunner drafts a charter into the conversation; it is written here once the DM agrees with the content. The major arcs are fixed and read-only: every charter below serves one.

## How the levels fit
- **Major arc** (fixed, DM-owned) → **minor arc** → **adventure** → **session**.
- **An adventure is an island** (or one place the party goes to do something): it starts on arrival and ends on departure, however many sessions that takes. **A voyage is never an adventure.** Voyages are self-contained downtime that fall inside an adventure or between two of them; what happens on one is logged, but it gets no charter and no milestones of its own.
- Each level owes something up (vertical) and sets something up for its next sibling (horizontal).
- Minor arcs and adventures each have one living charter file. Tick milestones as they land and keep the file current; don't write a new one per session.
- A **session** has no charter file. Its obligations are the `## Arc fit` section of its prep document (`Private Notes/Session Prep/Session NN - Prep.md`), taken from the Showrunner's report. Its outcome is one line in the adventure charter's Log, added after the recap.
- Threads, hooks and clocks are referred to by ID from [[Threads]], with a few words of description. Charters never restate a thread's state.

## File naming (flat, in `Charters/`)
- `Minor Arc - <Name>.md`
- `Adventure - <Name>.md`

## Charter template

```
---
tags:
  - charter
level: minor-arc | adventure
major-arc: 2
parent: "[[<parent charter or Major Arcs>]]"
status: draft | active | closed
---
# <Level>: <Name>

## Premise
The through-line in a few sentences.

## Milestones
- [ ] <beat that must land>
- [ ] T-000: advance | plant | resolve
- [ ] H-000: service

## Vertical obligation
What this level owes its parent, ending at the line of the major arc it serves.

## Horizontal obligation
What this level must set up for its next sibling.

## In play
Threads (T-), PC hooks (H-), clocks (K-) and items (I-) this level touches, by ID.

## Locked constraints
Things this level must not contradict or reveal early (for example, the Terramancer betrayal stays in Arc 4).

## Log
One dated entry per session played under this charter (adventure charters) or per adventure closed (minor-arc charters), newest last.
- Session NN (YYYY-MM-DD) — Satisfied: … · Drifted: … · Owed next: …
```

## Closing a charter
When an adventure or minor arc ends, add a closing entry to its Log (vertical fit: fits / drifts / breaks; horizontal handoff: set up / partly / missed; one or two sentences each), set `status: closed`, and carry anything still owed into the next sibling's charter.

## Rules
- Do not retro-charter work that is already deep in play.
- A charter is not canon. What happened is recorded in `Session Notes/`.
- Changing a major arc is the DM's call alone.
