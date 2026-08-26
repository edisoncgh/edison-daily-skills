#!/usr/bin/env python3
"""Static portability/regression checks for Handoff-Driven Development."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
errors: list[str] = []

required = [
    "SKILL.md",
    "references/doc-templates.md",
    "references/neat-freak-interop.md",
    "references/migration-v2-to-v3.md",
    "scripts/init_handoff_docs.py",
    "test-prompts.json",
]
for rel in required:
    if not (root / rel).is_file():
        errors.append(f"missing required file: {rel}")

for obsolete in ["references/relay-closeout.md", "references/workflow-prompts.md"]:
    if (root / obsolete).exists():
        errors.append(f"obsolete orchestration file must be removed: {obsolete}")

skill = root / "SKILL.md"
if skill.is_file():
    text = skill.read_text(encoding="utf-8")
    for phrase in [
        "operational control plane",
        "handoff-driven-development",
        "Synchronize for Handoff",
        "Project Continue Interface",
        "does **not** invoke `project-memory` or `neat-freak`",
        "AGENT_HANDOFF.md` **last**",
    ]:
        if phrase.lower() not in text.lower():
            errors.append(f"SKILL.md missing boundary phrase: {phrase}")
    for forbidden in [r"name:\s*handoff-driven-development-v3", r"\$ARGUMENTS", r"\$0\b"]:
        if re.search(forbidden, text):
            errors.append(f"vendor/legacy core dependency found: {forbidden}")
    # Minimal common Agent Skills frontmatter only.
    if text.startswith("---\n"):
        fm = text.split("---\n", 2)[1]
        keys = [line.split(":", 1)[0].strip() for line in fm.splitlines()
                if line and not line.startswith((" ", "\t")) and ":" in line]
        if set(keys) != {"name", "description"}:
            errors.append(f"frontmatter must use only name+description, found: {keys}")
    else:
        errors.append("missing YAML frontmatter")

# Legacy current-memory semantics are allowed only in the migration reference.
for path in root.rglob("*.md"):
    rel = path.relative_to(root).as_posix()
    if rel == "references/migration-v2-to-v3.md":
        continue
    text = path.read_text(encoding="utf-8")
    if ".memory/context.md" in text:
        errors.append(f"unexpected legacy current-memory reference: {rel}")

prompts = root / "test-prompts.json"
if prompts.is_file():
    try:
        data = json.loads(prompts.read_text(encoding="utf-8"))
        if len(data) < 8:
            errors.append("need at least 8 regression scenarios")
    except json.JSONDecodeError as exc:
        errors.append(f"invalid test-prompts.json: {exc}")

if errors:
    print("FAIL")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)
print("PASS: handoff-driven-development portability/static checks")
