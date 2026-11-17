#!/usr/bin/env python
"""Convention checks for the campaign vault.

Usage (from anywhere):
    python .claude/scripts/vault_lint.py <file.md> [<file.md> ...]
    python .claude/scripts/vault_lint.py --all        # every markdown page in the vault
    python .claude/scripts/vault_lint.py --hook       # PostToolUse hook: reads the tool call on stdin

Checks: unbalanced %% markers, missing or wrong publish flags, leftover review markers,
wikilinks that are near-misses of an existing page name, and (session recaps only) quotation
marks and game-mechanics words in the visible body.

Exit code: 0 when clean, 1 when anything was reported. In --hook mode it always exits 0 and
passes findings back to the assistant as context.
"""
import difflib
import json
import re
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
PRIVATE_DIRS = ("Private Notes", ".claude", ".obsidian")
SKIP_DIRS = (".claude", ".obsidian", ".git", "node_modules")

WIKILINK = re.compile(r"\[\[([^\]\|#]+)(?:#[^\]\|]*)?(?:\|[^\]]*)?\]\]")
FENCE = re.compile(r"```.*?```", re.S)
INLINE_CODE = re.compile(r"`[^`\n]*`")
MECHANICS = re.compile(
    r"\b(DC ?\d+|\d+ ?(?:feet|ft\.?)|hit points?|saving throws?|spell slots?|"
    r"initiative|rolled|nat(?:ural)? ?(?:1|20)|advantage|disadvantage)\b",
    re.I,
)


def rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(VAULT).as_posix()
    except ValueError:
        return path.as_posix()


def is_private(relpath: str) -> bool:
    return relpath.split("/")[0] in PRIVATE_DIRS


def page_names() -> dict:
    """Lower-cased page name -> actual page name, for every markdown page in the vault."""
    names = {}
    for p in VAULT.rglob("*.md"):
        if any(part in SKIP_DIRS for part in p.relative_to(VAULT).parts):
            continue
        names.setdefault(p.stem.lower(), p.stem)
    return names


def split_frontmatter(text: str):
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[3:end], text[end + 4:]
    return "", text


def visible_body(body: str) -> str:
    """Body with code fences and %% blocks removed."""
    body = FENCE.sub("", body)
    parts = body.split("%%")
    return "".join(parts[0::2])


def lint_file(path: Path, names: dict) -> list:
    relpath = rel(path)
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        return [f"could not read file: {exc}"]

    issues = []
    front, body = split_frontmatter(text)
    private = is_private(relpath)

    # 1. %% markers must pair up.
    marker_lines = [
        i for i, line in enumerate(
            INLINE_CODE.sub("", FENCE.sub(lambda m: "\n" * m.group().count("\n"), text)).splitlines(), 1
        )
        for _ in range(line.count("%%"))
    ]
    if len(marker_lines) % 2:
        issues.append(
            f"unbalanced %% markers ({len(marker_lines)} found, on lines "
            f"{', '.join(map(str, marker_lines))}): a hidden block is not closed, "
            "so DM-only text may publish or visible text may vanish"
        )

    # 2. Publish flags.
    if re.search(r"^publish\s*:", front, re.M):
        issues.append("frontmatter uses `publish:`; this vault only uses `draft: true|false`")
    if not private and not re.search(r"^draft\s*:\s*(true|false)\s*$", front, re.M):
        issues.append("publishing page has no explicit `draft: true|false` in its frontmatter")

    # 3. Review scaffolding.
    for i, line in enumerate(text.splitlines(), 1):
        if "[NEW]" in line:
            issues.append(f"line {i}: leftover [NEW] review marker")

    # 4. Wikilinks that nearly match an existing page.
    seen = set()
    for match in WIKILINK.finditer(INLINE_CODE.sub("", FENCE.sub("", text))):
        target = match.group(1).strip().split("/")[-1]
        key = target.lower()
        if not target or key in seen:
            continue
        seen.add(key)
        if key in names:
            if names[key] != target:
                issues.append(f"wikilink [[{target}]] differs in capitalisation from the page '{names[key]}'")
            continue
        close = difflib.get_close_matches(key, names.keys(), n=1, cutoff=0.88)
        if close:
            issues.append(
                f"wikilink [[{target}]] has no page; did you mean '{names[close[0]]}'? "
                "(fine to keep if it is a different, established name)"
            )

    # 5. Session recaps: no quotes or mechanics in the visible body.
    if relpath.startswith("Session Notes/"):
        for i, line in enumerate(visible_body(body).splitlines(), 1):
            if re.search(r"[\"“”]", line):
                issues.append(f"recap body has a quotation mark: {line.strip()[:80]}")
            mech = MECHANICS.search(line)
            if mech:
                issues.append(f"recap body has game mechanics ('{mech.group()}'): {line.strip()[:80]}")

    return issues


def run(paths, names) -> dict:
    report = {}
    for p in paths:
        if p.suffix.lower() != ".md" or not p.exists():
            continue
        found = lint_file(p, names)
        if found:
            report[rel(p)] = found
    return report


def main(argv) -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass

    if "--hook" in argv:
        try:
            payload = json.load(sys.stdin)
            raw = payload.get("tool_input", {}).get("file_path", "")
        except (json.JSONDecodeError, AttributeError):
            return 0
        if not raw:
            return 0
        path = Path(raw.replace("\\", "/"))
        relpath = rel(path)
        if path.suffix.lower() != ".md" or relpath.split("/")[0] in SKIP_DIRS or relpath.startswith(("/", "..")) or ":" in relpath:
            return 0
        report = run([path], page_names())
        if report:
            lines = [f"vault_lint found issues in {name}:" for name in report]
            for found in report.values():
                lines += [f"- {item}" for item in found]
            print(json.dumps({
                "hookSpecificOutput": {
                    "hookEventName": "PostToolUse",
                    "additionalContext": "\n".join(lines),
                }
            }))
        return 0

    if "--all" in argv:
        paths = [
            p for p in VAULT.rglob("*.md")
            if not any(part in SKIP_DIRS for part in p.relative_to(VAULT).parts)
        ]
    else:
        paths = []
        for arg in argv:
            p = Path(arg)
            paths.append(p if p.is_absolute() else (Path.cwd() / p))
        if not paths:
            print(__doc__)
            return 0

    report = run(paths, page_names())
    if not report:
        print(f"vault_lint: {len(paths)} file(s) checked, no issues.")
        return 0
    for name, found in sorted(report.items()):
        print(name)
        for item in found:
            print(f"  - {item}")
    total = sum(len(v) for v in report.values())
    print(f"\nvault_lint: {total} issue(s) in {len(report)} of {len(paths)} file(s).")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
