#!/usr/bin/env python3
"""Static portability/regression checks for the Project Continue skill."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
errors: list[str] = []

required = ["SKILL.md", "references/portability.md", "test-prompts.json"]
for rel in required:
    if not (root / rel).is_file():
        errors.append(f"missing required file: {rel}")

skill_path = root / "SKILL.md"
if skill_path.is_file():
    text = skill_path.read_text(encoding="utf-8")
    # Core must not depend on vendor argument/template machinery.
    forbidden = [r"\$ARGUMENTS", r"\$0\b", r"disable-model-invocation", r"disableModelInvocation", r"argument-hint:", r"arguments:"]
    for pattern in forbidden:
        if re.search(pattern, text):
            errors.append(f"vendor-specific core dependency found: {pattern}")
    for phrase in [
        "project-continue closeout",
        "project-continue resume",
        "project-memory",
        "handoff-driven-development",
        "neat-freak",
        "owns no project facts",
        "verified code/runtime",
        "Idempotency",
        "Degraded Mode",
    ]:
        if phrase.lower() not in text.lower():
            errors.append(f"missing core contract phrase: {phrase}")
    # Ensure frontmatter uses only the common required fields.
    if text.startswith("---\n"):
        fm = text.split("---\n", 2)[1]
        keys = []
        for line in fm.splitlines():
            if line and not line.startswith((" ", "\t")) and ":" in line:
                keys.append(line.split(":", 1)[0].strip())
        if set(keys) != {"name", "description"}:
            errors.append(f"frontmatter must use only name+description, found: {keys}")
    else:
        errors.append("missing YAML frontmatter")

prompts = root / "test-prompts.json"
if prompts.is_file():
    try:
        data = json.loads(prompts.read_text(encoding="utf-8"))
        if len(data) < 10:
            errors.append("need at least 10 project-continue regression scenarios")
    except json.JSONDecodeError as exc:
        errors.append(f"invalid test-prompts.json: {exc}")

if errors:
    print("FAIL")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)
print("PASS: project-continue portability/static checks")
