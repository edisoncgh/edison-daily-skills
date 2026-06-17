#!/usr/bin/env python3
"""Initialize minimum docs for handoff-driven development v2.

Creates docs/PROJECT_BRIEF.md, TASKS.md, TECH_PLAN.md, and AGENT_HANDOFF.md
without overwriting existing files unless --force is supplied.
"""
from __future__ import annotations

import argparse
from pathlib import Path

TEMPLATES = {
    "PROJECT_BRIEF.md": """# Project Brief

## Product
TODO: Describe what the product is and why it exists.

## Users
- TODO: Primary users and usage environment.

## Runtime / Stack
- Language/runtime: TODO
- Frameworks/tools: TODO
- Target platform: TODO

## Product Boundaries
- In scope: TODO
- Out of scope: TODO

## Core Capabilities
- TODO

## Domain Terms
- `TODO`: TODO

## Source Of Truth
- Tasks: docs/TASKS.md
- Technical plan: docs/TECH_PLAN.md
- Handoff: docs/AGENT_HANDOFF.md
- Memory: .memory/context.md and .memory/knowledge.md if present

## Update Rules
- Update only when stable project identity, runtime, domain language, or long-lived boundaries change.
- Do not record current slice status or temporary blockers here.
""",
    "TASKS.md": """# Tasks

## Current Milestone: TODO

### Goal
TODO

### Scope
- TODO

### Explicitly NOT in Scope
- TODO

### Acceptance Criteria
- [ ] TODO

## Current Slice: TODO
- [ ] Implement: TODO
- [ ] Verify: TODO

## Bugs / Stabilization
- [ ] TODO

## Technical Debt / Polish Debt
- [ ] TODO

## Later / Backlog
- [ ] TODO

## Archives
- TODO
""",
    "TECH_PLAN.md": """# Technical Plan

## Architecture Summary
TODO

## File / Module Map
- TODO

## Data / Control Flow
TODO

## Interfaces / Contracts
TODO

## Testing and Verification Strategy
- Pure logic: TODO
- Integration/runtime: TODO
- Manual acceptance: TODO

## Known Risks
- TODO
""",
    "AGENT_HANDOFF.md": """# Agent Handoff

## Current State
TODO

## Last Completed Work
- Commit: TODO
- Files changed: TODO
- Verified behavior: TODO

## Current Blockers / Known Issues
- TODO

## Next Recommended Step
TODO

## Explicit Non-Goals for Next Agent
- TODO

## Files of Interest
- TODO

## Run / Verify Steps
1. TODO
""",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--docs-dir", default="docs", help="Docs directory to initialize")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    args = parser.parse_args()

    docs_dir = Path(args.docs_dir)
    docs_dir.mkdir(parents=True, exist_ok=True)

    created: list[str] = []
    skipped: list[str] = []
    for filename, content in TEMPLATES.items():
        path = docs_dir / filename
        if path.exists() and not args.force:
            skipped.append(str(path))
            continue
        path.write_text(content, encoding="utf-8")
        created.append(str(path))

    print("Created:")
    for item in created:
        print(f"  {item}")
    print("Skipped existing:")
    for item in skipped:
        print(f"  {item}")


if __name__ == "__main__":
    main()
