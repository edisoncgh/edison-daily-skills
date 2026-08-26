# Migrating Project Memory v1 -> v2

v1 mixed historical memory with current-state coordination through
`.memory/context.md` and per-conversation `sessions/`. v2 deliberately removes that
responsibility overlap.

## Target Layout

```text
.memory/
├── index.md
├── knowledge.md
└── episodes/
```

## Migration Procedure

1. Read current handoff/task/technical docs and verified code/runtime first. These
   establish current truth.
2. Treat old `.memory/context.md` as a legacy snapshot only.
3. Review legacy `sessions/` in thematic groups. Convert only meaningful events into
   focused episodes: decisions, reversals, failures, fixes, transitions, and lessons.
4. Distill recurring rationale/pitfalls into the new `knowledge.md`.
5. Rebuild `index.md` from the new episodes.
6. Keep legacy files in place or move them under `.memory/legacy/` according to user
   and repo policy. Do not silently delete unique history.
7. Remove all active references that instruct agents to refresh/read
   `.memory/context.md` for current state.

## What Not to Migrate

Do not preserve as v2 memory:

- current next-action lists;
- current blockers or verification checklists;
- chat-turn-by-turn narration;
- raw tool output;
- current architecture inventories already owned by technical docs.

## Sanity Check

A new agent should be able to answer "why did we choose this?" from memory, but
should have to read handoff/current docs to answer "what should I do next?".
