---
title: Corrections
tags:
  - corrections
draft: true
---
DM-only ledger of recurring lore/continuity mistakes and their corrections. This ledger
records the failure mode and points at canon — it never replaces canon; the linked page is
always the source of truth.

Owned by the **Steward** (only writer): dedupes on a new correction (increments an existing
entry rather than duplicating), promotes an entry into `CLAUDE.md`'s "Active corrections" list
at 2 occurrences or immediately at `severity: high`, and retires an entry to `resolved` (and
removes it from the Active list) on the DM's say-so. Consulted by the **Loremaster** (surfaces
scope-matching entries in briefs) and the **Continuity Auditor** (flags repeats as
must-fix RECURRENCE).

Entry format:

```
## C-NNN: <short title>
- **Status:** watch | active | resolved
- **Severity:** high  (omit if not high)
- **Occurrences:** <count> (<dates>)
- **The mistake:** <the incorrect understanding that was produced>
- **The correction:** <the DM's clarification / the correct understanding>
- **Canonical source:** [[<vault page>]]
- **Scope:** <tags reused from the affected canon page(s)>
```

## C-001: %% DM-only block boundary discipline (read and write direction)
- **Status:** active
- **Severity:** high
- **Occurrences:** 2 (2026-09-20, 2026-09-20)
- **The mistake:** Two related failures of the same discipline. (1) READ DIRECTION: during a canon retrieval pass on Lady Alexandra Aurum, text inside a `%%` DM-only comment block in [[Collin McCambridge]] was classified as visible, player-facing text. Specifically, the "# Family" section and its description of Alexandra Aurum (powerful abjurer, lacking in combat capabilities, forced into becoming the family's scion of the church) were reported as player knowledge. Caught before any content was published — no leak occurred. (2) WRITE DIRECTION: while drafting [[Lady Alexandra Aurum]], DM-only details sourced from a `%%` block — specifically her birth order ("seventh child") and her mother's name (Baroness Adelaide Aurum) — were placed into the page's VISIBLE body instead of inside its `%%` block. Caught by the Continuity Auditor gate before the Steward wrote the page; no leak occurred.
- **The correction:** The `%%` markers in [[Collin McCambridge]] sit at lines 32 and 82 (line numbers may drift if the page is edited — the file itself is the source of truth). Everything between them — the entire Backstory section, the Family list, and Alexandra's description — is DM-only; the party does not know any of it. Verified by `grep -n '^%%'`. General rule (read direction): before classifying ANY vault text as player-facing, verify the enclosing `%%` open/close pairs by line number — never judge from section headings or surrounding context, since a single `%%` block can span many headings. Note also that `%%` appears inline mid-sentence in some files (e.g. lines 18 and 28 of [[Collin McCambridge]]), so a naive count of `%%` occurrences is not sufficient — check position and pairing. General rule (write direction): when drafting a new page, every fact must be traced to a player-facing source before it goes into visible text. A fact whose ONLY source is inside a `%%` block (in any file, including the page being drafted) stays inside a `%%` block on the new page too — it does not migrate to visible prose just because the new page's visible section discusses related, genuinely public material. Applies especially to the **Loremaster** and **Continuity Auditor**, who consult this ledger, and to the **Worldsmith** and **Steward** when drafting/writing new pages.
- **Canonical source:** [[Collin McCambridge]], [[Lady Alexandra Aurum]]
- **Scope:** player-character, collin-mccambridge, house-aurum
