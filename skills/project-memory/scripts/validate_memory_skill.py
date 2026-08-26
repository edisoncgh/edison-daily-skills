#!/usr/bin/env python3
"""Static portability/regression checks for Project Memory."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
errors: list[str] = []

required = [
    "SKILL.md",
    "rules.md",
    "template/index.md",
    "template/knowledge.md",
    "template/episode.md",
    "references/migration-v1-to-v2.md",
    "test-prompts.json",
]
for rel in required:
    if not (root / rel).is_file():
        errors.append(f"missing required file: {rel}")

for rel in ["template/context.md", "template/session.md", "examples/context-example.md", "examples/session-example.md"]:
    if (root / rel).exists():
        errors.append(f"legacy live artifact must be removed: {rel}")

episode = root / "template/episode.md"
if episode.is_file():
    text = episode.read_text(encoding="utf-8")
    for phrase in ["Unresolved at the Time", "Outcome & Evidence", "Lessons / Pitfalls"]:
        if phrase not in text:
            errors.append(f"episode template missing: {phrase}")

skill = root / "SKILL.md"
if skill.is_file():
    text = skill.read_text(encoding="utf-8")
    for phrase in ["historical continuity", "no `.memory/context.md`", "current state", "Project Continue Interface", "handoff-driven-development"]:
        if phrase.lower() not in text.lower():
            errors.append(f"SKILL.md missing boundary phrase: {phrase}")
    for forbidden in [r"handoff-driven-development-v3", r"\$ARGUMENTS", r"\$0\b", r"disable-model-invocation"]:
        if re.search(forbidden, text):
            errors.append(f"vendor/legacy core dependency found: {forbidden}")
    if text.startswith("---\n"):
        fm = text.split("---\n", 2)[1]
        keys = [line.split(":", 1)[0].strip() for line in fm.splitlines()
                if line and not line.startswith((" ", "\t")) and ":" in line]
        if set(keys) != {"name", "description"}:
            errors.append(f"frontmatter must use only name+description, found: {keys}")
    else:
        errors.append("missing YAML frontmatter")

prompts = root / "test-prompts.json"
if prompts.is_file():
    try:
        data = json.loads(prompts.read_text(encoding="utf-8"))
        if len(data) < 6:
            errors.append("need at least 6 regression scenarios")
    except json.JSONDecodeError as exc:
        errors.append(f"invalid test-prompts.json: {exc}")

if errors:
    print("FAIL")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)
print("PASS: project-memory portability/static checks")
