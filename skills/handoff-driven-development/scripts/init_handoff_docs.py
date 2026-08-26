#!/usr/bin/env python3
"""Initialize the minimum Handoff-Driven Development operational docs.

Creates PROJECT_BRIEF.md, TASKS.md, TECH_PLAN.md, and AGENT_HANDOFF.md without
overwriting existing files unless --force is supplied.
"""
from __future__ import annotations

import argparse
from pathlib import Path

TEMPLATES = {
    "PROJECT_BRIEF.md": """# Project Brief\n\n## North Star\nTODO: Describe the durable project outcome.\n\n## Product / Users\n- Product: TODO\n- Primary users / environment: TODO\n\n## Durable Boundaries\n- In scope: TODO\n- Out of scope: TODO\n\n## Runtime / Platform Constraints\n- Language/runtime: TODO\n- Frameworks/tools: TODO\n- Target platform: TODO\n\n## Core Capabilities\n- TODO\n\n## Domain Terms\n- `TODO`: TODO\n\n## Source of Truth\n- Current tasks: docs/TASKS.md\n- Current architecture/contracts: docs/TECH_PLAN.md\n- Current baton: docs/AGENT_HANDOFF.md\n- Verification: docs/QUALITY.md if present\n- Historical rationale/lessons: .memory/ if project-memory is installed\n\n## Update Rule\n- Update only when stable direction, users, durable boundaries, runtime constraints, or domain language change.\n- Do not record current blocker or next action here.\n""",
    "TASKS.md": """# Tasks\n\n## Current Milestone: TODO\n\n### Goal\nTODO\n\n### Scope\n- TODO\n\n### Explicitly NOT in Scope\n- TODO\n\n### Acceptance Criteria\n- [ ] TODO\n\n## Current Slice: TODO\n- [ ] Implement: TODO\n- [ ] Verify: TODO\n\n## Blockers / Unverified\n- [ ] TODO\n\n## Near Backlog\n- [ ] TODO\n\n## Debt / Later\n- [ ] TODO\n\n## Archive Pointer\n- TODO\n""",
    "TECH_PLAN.md": """# Technical Plan\n\n## Current Architecture Summary\nTODO\n\n## File / Module Map\n- TODO\n\n## Data / Control Flow\nTODO\n\n## Interfaces / Contracts\nTODO\n\n## Runtime / Verification Strategy\n- Start/run: TODO\n- Tests: TODO\n- Integration/runtime checks: TODO\n- Manual acceptance: TODO\n\n## Current Risks / Constraints\n- TODO\n""",
    "AGENT_HANDOFF.md": """# Agent Handoff\n\n## Current Direction\nTODO\n\n## Current State\nTODO\n\n## Last Completed & Verified\n- Work: TODO\n- Commit (if any): TODO\n- Evidence: TODO\n\n## Current Blockers / Unverified\n- TODO\n\n## Next Recommended Step\nTODO\n\n## Explicit Non-Goals\n- TODO\n\n## Files of Interest\n- TODO\n\n## Run / Verify\n1. TODO\n""",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--docs-dir", default="docs")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    docs = Path(args.docs_dir)
    docs.mkdir(parents=True, exist_ok=True)
    created: list[str] = []
    skipped: list[str] = []

    for filename, content in TEMPLATES.items():
        path = docs / filename
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
