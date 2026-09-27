---
tags:
  - charter
  - template
---
# Charter Templates

DM-only. Templates for the planning hierarchy that sits beneath the four major arcs in [[Major Arcs]]. The Showrunner drafts a charter into the conversation; the Steward writes it here only after the DM approves it. The major arcs are fixed and read-only: every charter below serves one.

## How the levels fit
- **Major arc** (fixed, DM-owned) → **minor arc** → **adventure** (3 to 4 sessions around one plot point) → **session**.
- Each level owes something up (vertical) and sets something up for its next sibling (horizontal).
- Threads, hooks and clocks are referred to by ID from [[Threads]]. Charters never restate a thread's state.

## File naming (flat, in `Charters/`)
- `Minor Arc - <Name>.md`
- `Adventure - <Name>.md`
- `Session NN - Charter.md`
- `Scorecard - <Level> <Name>.md`

## Charter template

```
---
tags:
  - charter
level: minor-arc | adventure | session
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
```

## Scorecard template

```
---
tags:
  - charter
  - scorecard
level: minor-arc | adventure | session
charter: "[[<the charter being scored>]]"
---
# Scorecard: <Level> <Name>

## Pending milestones
## Satisfied
## Drifted
## Owed next

## Vertical fit
Verdict: fits | drifts | breaks. One or two sentences.

## Horizontal handoff
Verdict: set up | partly | missed. One or two sentences.
```

## Rules
- Do not retro-charter work that is already deep in play. The first real minor-arc charter is written for whatever follows Session 28.
- A charter is not canon. What happened is recorded in `Session Notes/`.
- Changing a major arc is the DM's call alone.
