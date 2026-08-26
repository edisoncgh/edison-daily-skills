---
name: project-memory
description: Use when recalling why past project decisions were made, preserving a meaningful development episode or reusable lesson, migrating legacy project memory, or when a continuity workflow such as project-continue requests historical recall or persistence.
---

# Project Memory

Project Memory is the project's **historical continuity layer**. It answers:

> **How did this project get here?**

It preserves meaningful development episodes, decision rationale, failed approaches,
fixes, environment quirks, and lessons that are not obvious from current code.

**Boundary:** historical continuity, not current state.

| Question | Owner |
|---|---|
| What happened before, and why? | `project-memory` |
| What failed/worked before? | `project-memory` |
| What are we doing now / next? | Handoff docs + verified code/runtime |
| What is the current architecture? | Current technical docs + code |
| Are knowledge surfaces consistent? | `neat-freak` or equivalent auditor |

If history conflicts with present-day docs, do not rewrite history to match. Memory
explains the past; current operational surfaces describe the present.

## Layout

```text
.memory/
├── index.md
├── knowledge.md
└── episodes/
    └── YYYYMMDD-HHmm-short-event.md
```

There is deliberately **no `.memory/context.md`** in v2.

- `index.md`: retrieval map, one concise line per meaningful episode.
- `knowledge.md`: distilled historical rationale, lessons, pitfalls, transitions.
- `episodes/`: event-oriented history, not one file per chat turn.

## Recall

When `.memory/` exists or the user asks about prior work:

1. Read `index.md` and `knowledge.md`.
2. Infer the relevant topic from the request/current handoff.
3. Read only **1-3 relevant episodes**, ranked by topic, file path, tags, then recency.
4. Recover relevant decisions, rationale, failed attempts, fixes, and pitfalls.
5. If the user needs current status or next action, continue to handoff docs and/or
   verify code/runtime. Never infer current state from an old episode.

## Persist Only Meaningful Events

Create an episode when the work produced historical value, such as:

- a meaningful slice/milestone outcome;
- a decision or reversal with rationale;
- a non-obvious bug diagnosis/fix;
- a failed approach future agents could repeat;
- an environment/toolchain quirk;
- a requirement/user choice that changed project trajectory;
- a handoff containing new historical lessons.

Skip memory for routine inspection, trivial edits, raw tool output, chat narration,
and "what we will do next".

### Episode write flow

1. Read `template/episode.md`.
2. Create `episodes/<date-time>-<slug>.md`.
3. Record evidence-backed past-tense context, attempts/options, decision/change,
   outcome/evidence, lessons/pitfalls, and any **unresolved-at-the-time** items.
4. Reference paths/commits instead of copying code or diffs.
5. Update `index.md`.
6. Distill reusable historical understanding into `knowledge.md` when warranted.
7. Do not write the current milestone, blocker, verification checklist, or next
   action as if memory owns them.

## Knowledge Distillation

`knowledge.md` should contain historical understanding, for example:

- Historical Decisions & Rationale
- Architecture / Product Transitions
- Lessons Learned
- Pitfalls & Failure Patterns
- Environment / Toolchain Quirks
- Project-Specific Preference History

If a memory fact becomes an active rule/current contract that every agent must obey,
promote the authoritative statement to the rule/docs layer and keep only historical
provenance in memory.

## Project Continue Interface

`project-continue` may use this skill as the historical layer, but Project Memory remains usable
independently.

- `project-continue resume` -> perform **Recall** for history relevant to the current work and
  return decisions, prior attempts, transitions, pitfalls, and lessons.
- `project-continue closeout` -> perform **Persist** only for meaningful new historical events;
  distill reusable rationale/lessons and return a short persistence summary.
- `project-continue checkpoint` -> persist only if the session created a genuinely meaningful
  historical event.
- `project-continue status` -> report whether the memory store is present/legacy/uncertain
  without writing it.

Never recursively invoke Project Continue. Never create a current-state snapshot or next-agent
action list.

## Legacy v1

If `.memory/context.md` or `.memory/sessions/` exists, treat it as **legacy data**.
Do not repair/refresh `context.md` or use it as current truth. Migrate durable history
at a maintenance boundary without silently deleting unique history.

Read `references/migration-v1-to-v2.md` before migration.

## Integration Contract

With `handoff-driven-development`:

- Memory owns **past tense**.
- Handoff operational docs own **present direction/state**.
- Current-state arbitration: **verified runtime/code -> handoff docs -> memory as
  historical context**.

With `neat-freak`, memory is an audited knowledge surface, not a second current-state
source.

## Non-Negotiable Rules

Read `rules.md` for details. Never:

- store secrets/tokens/passwords;
- dump full code/diffs;
- create episode-per-turn logs;
- own the current next step;
- auto-delete unique history because it is old;
- erase temporal contradictions that represent real project transitions.

## Self-Check

- Did I answer history without treating it as current state?
- Did I read only the relevant episodes?
- Is each new episode a meaningful, evidence-backed event?
- Did I route current milestone/blocker/next action to Handoff?
- Did I avoid reviving legacy `context.md` semantics?
