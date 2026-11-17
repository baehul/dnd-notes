---
description: The whole between-session loop in order — recap, write-back, arc and thread report, prep — resumable at any step
argument-hint: NN (the session just played; prep is then for NN+1)
allowed-tools: Read, Glob, Grep, Write, Edit, Agent, SendMessage, Skill
---
`/cycle NN` walks me from "we just played Session NN" to "Session NN+1 is prepped". Each step
is an existing workflow; this command only sequences them, records progress, and lets me stop
for the day at any point.

## Where progress lives
The `## Cycle` block at the top of `Private Notes/Planning/Current State.md`:

```
## Cycle
- Played: Session NN
- [ ] 1 Recap written
- [ ] 2 Trackers updated (Threads, Current State, scorecard line)
- [ ] 3 Stale pages reviewed
- [ ] 4 Arc and thread report
- [ ] 5 Prep for Session NN+1 compiled
- Notes: <anything deferred, in a few words>
```

On start, read that block. If it is for this NN, resume at the first unticked step and tell me
which one in a sentence. If it is for an earlier session with steps unticked, tell me what was
left and ask whether to finish it or drop it. If NN is missing, use the newest played session.
Tick each step as it completes (the file is DM-only; write it directly).

## Steps
1. **Recap** — run the `session-summary` flow for NN (Stages 1 to 3). If
   `Session Notes/Session NN Notes.md` already exists, tick this and move on.
2. **Trackers** — done by the Steward in Stage 3 of the same flow. Give me its summary of what
   moved. If step 1 was already done but `Current State.md` still says an earlier session,
   launch the Steward for the write-back alone.
3. **Stale pages** — Stage 4 of the same flow: the proposed chronicle-voice page edits, 3 to 5
   at a time, written as I approve them. I can say "later"; then note the remainder under Notes.
4. **Arc and thread report** — launch the **Showrunner** for the report for Session NN+1. Show
   it to me in one screen. If it says the adventure or minor arc is ending or its charter is out
   of date, offer to have the Showrunner draft the next charter before prep starts.
5. **Prep** — run the `prep` skill for Session NN+1, passing it the report from step 4 so it
   doesn't launch the Showrunner again. Tick the box when the prep document is compiled.

## Between steps
After each step say what was done in a line or two and what comes next, then continue unless I
say to stop. A good place to pause is after step 3 (the record is current) and anywhere inside
step 5 (the prep working file holds everything decided so far). Never commit or push; remind me
once, after step 3, that the recap and page edits are ready for my git review.

## Workflow log
While running any step, append one line to `Private Notes/Meta Notes/Workflow Log.md` each
time: I correct a fact; I answer a question that had an obvious default; an agent is launched
(which, why, and whether its result was used); a step has to be redone; or I say something
about how the process felt. Date each line and name the step. Don't ask me about these entries.
