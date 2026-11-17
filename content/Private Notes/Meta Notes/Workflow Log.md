---
tags:
  - workflow
draft: true
---
# Workflow Log

DM-only. Friction notes on how the assistant setup is working, used as the input to the next audit of `.claude/`. One dated line per event: a fact the DM had to correct, a question that had an obvious default, an agent launch (which, why, whether its result was used), a step that had to be redone, or a remark from the DM about how the process felt. Appended automatically during `/cycle`, `/session-summary` and `prep`; nobody needs to ask.

## Round 1 changes (2026-11-16)
Setup redesigned after the first audit: `Current State.md` digest added and read first by everything; `Threads.md` slimmed to current state; defaults taken with an "Assumed" list instead of questions; diffs shown only for player-facing pages; pushback scaled to impact; creativity by layer; Adventure Designer agent retired into the `prep` skill; charters reduced to minor-arc and adventure files with a session log; `/cycle` and `statblock` added; conventions gathered in `.claude/rules/vault-writing.md`; lint script and hook added.

## Things to watch in Session 33's cycle
- Does anything state an out-of-date fact despite the digest?
- How many questions get asked, and how many of them had an obvious default?
- Does the prep "Decided so far" list actually stop drift?
- Is the Showrunner report useful at one screen, or noise?
- Which agent launches paid for themselves?
- Does the D&D Beyond procedure work first time?

## Log
- 2026-11-16 (setup) — Lint found an unclosed `%%` block on `Broomhilda Bonebelly.md` (3 markers, last one opens at line 32 and never closes). Raised with the DM.
- 2026-11-16 (catch-up) — DM narrowed the page catch-up: pages are background, so only fundamental changes go on them; event-style additions (Varius, Magnus) rejected. Sweep prompts over-collected because "missing a development the party witnessed" counted as stale. Rule added to vault-writing.md. Lesson: ask what belongs on a page before sweeping.
- 2026-11-16 (catch-up) — Agents launched: 2 Sonnet sweeps (61 pages, ~326k tokens). Used: Eobard, Sylas, Alexandra, item-holder and status findings. Not used: roughly half the proposals (event additions).
- 2026-11-16 (catch-up) — Earlier "leave untouched" ruling on Eobard and Alexandra pages lifted by the DM today; Session 19 recap still untouched.

- 2026-11-16 (catch-up) — Finished. Written with approval: Eobard (+ House Aurum entry), Sylas (published), Alexandra (published, vanishing line cut by the DM as short-term), Bloos (published as is), Jitterhop (Project Genesis made visible). Declined under the page rule: item bearers, captives on pages. 14 questions asked across the catch-up; the DM narrowed my proposal on 3 of them, each time toward "less on the page".
- 2026-11-16 (catch-up) — Still owed, not done: tell Collin's player his synced page still describes black hair and brown eyes (gold since S29).
- 2026-11-16 (verification) — Loremaster test on Collin passed: read Current State first, grepped Threads, no "cover" wording, 32k tokens, 13 seconds. Wobble: called Collin's player-private background "stale"; player-authored `%%` text is not ours to call stale.
- 2026-11-16 (cycle step 4) — Showrunner launched once (Opus, 67k tokens) for the S33 report plus charter currency. Report used whole as the prep file's Arc fit section; adventure charter draft written. It flagged Twilight as unserviced for 4 sessions, which nothing else had surfaced.
- 2026-11-16 (charters) — DM corrected the adventure model twice: adventures are islands; voyages are never adventures but self-contained downtime inside or between them. The Showrunner's old definition (3 to 4 sessions around a plot point) produced a wrong charter, and my first restatement of the DM's answer was only partly right. Rule now in the Showrunner file and the charter template. Lesson: restate a new rule back in the DM's terms before building on it.
- 2026-11-16 (charters) — I created the Session 33 prep working file before the DM had agreed setup was finished. The DM asked to confirm setup is complete first.
- 2026-11-16 (setup close-out) — Minor-arc charter fully reconciled through S32; Planning Backlog retired after its live content (the Restitution coffer, the Ettercap leave, design rules, open items) was folded into the charter. The backlog was not empty: my earlier summary of Luwei's terms to the DM had left out the Restitution and the Ettercap leave because I had only read the charter.
- 2026-11-16 (setup close-out) — October magic-item rulings and D&D Beyond reference moved from the unused memory folder into Magic Item Rarity.md. Most rulings were already in that table.
- 2026-11-16 (cycle step 5) — Resumed /cycle 32 at prep. Showrunner not relaunched (its report is already the working file's Arc fit). Loremaster launched once for the Jade Fragment brief (places, cast, Luwei's terms, Twilight hooks, Design Library fits).
- 2026-11-16 (cycle step 5) — DM reversed the Restitution: Otis plants Whisper Reeds in Luwei's garden instead of carrying a coffer to the aboleth. The S32 prep and the reconciled charter disagreed on it; asking was right. Defaults on the old S32 prep's open items accepted as given.
- 2026-11-16 (cycle step 5) — DM corrected my reading of 'his garden': the party's Lair, not the Jade Fragment. I had assumed instead of asking, although it was ambiguous and the stakes were high; the Assumed list caught it.
- 2026-11-16 (cycle step 5) — DM took both defaults (no fire quote; Luwei curious and noncommittal toward the Cult).
- 2026-11-16 (cycle step 5) — Compiled S33 prep. Continuity Auditor and Showrunner launched together, once, on the locked document.
- 2026-11-16 (cycle step 5) — Auditor result used: 6 significant, 8 minor; one minor was wrong (Cletus's fence is in S31:11). Showrunner fit check used: two significant (Vaxen thin; reeds and the mole). Two of the auditor's significant findings overturn defaults I gave the DM earlier (Collin's watch on Mithbarakaz; Luwei not knowing Vase's uncle); the S32 prep was the source, so I carried its errors forward.
- 2026-11-16 (cycle step 5) — DM ruled on all five review points, turning three of my defaults into richer beats (Luwei testing Collin's honesty, feigning about Vase, a Cult of Night study as the Dawn hint). Prep final; cycle for S32 complete.
