#!/usr/bin/env python3
"""Initialize Project Memory v2 without creating a current-state snapshot."""
from __future__ import annotations

import argparse
from pathlib import Path

INDEX = """# Memory Index\n\n> Historical retrieval index maintained by project-memory v2. One line per meaningful development episode.\n\n## Episodes\n\n## Retrieval Notes\n- Prefer topic/file/tag relevance over pure recency.\n- Read only 1-3 episodes for normal recall.\n- This index does not describe current project status.\n"""

KNOWLEDGE = """# Project Historical Knowledge\n\n> Distilled historical understanding. This is not the current architecture, task board, or handoff.\n\n## Historical Decisions & Rationale\n\n## Architecture / Product Transitions\n\n## Lessons Learned\n\n## Pitfalls & Failure Patterns\n\n## Environment / Toolchain Quirks\n\n## Project-Specific Preference History\n"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="Project root")
    args = parser.parse_args()

    memory = Path(args.root) / ".memory"
    episodes = memory / "episodes"
    episodes.mkdir(parents=True, exist_ok=True)

    created: list[str] = []
    for path, content in [(memory / "index.md", INDEX), (memory / "knowledge.md", KNOWLEDGE)]:
        if not path.exists():
            path.write_text(content, encoding="utf-8")
            created.append(str(path))

    print("Project Memory v2 initialized.")
    for item in created:
        print(f"Created: {item}")
    legacy = [memory / "context.md", memory / "sessions"]
    if any(p.exists() for p in legacy):
        print("Legacy v1 memory detected; read references/migration-v1-to-v2.md before migrating.")


if __name__ == "__main__":
    main()
