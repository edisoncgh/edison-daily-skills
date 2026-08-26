---
name: handoff-driven-development
description: Use when current project direction, milestone, active slice, blocker, verification state, or next action must be planned, aligned, synchronized, or handed off across coding sessions or agents; also use when a continuity orchestrator such as project-continue requests current-state alignment or synchronization.
---

# Handoff-Driven Development

Handoff-Driven Development is the project's **operational control plane**.

It answers:

> **Where are we now, where are we going, and what should happen next?**

It owns **current direction and current operational state**. It does not own project
history and it does not orchestrate other continuity skills.

## Source-of-Truth Contract

| Question | Source of Truth |
|---|---|
| What actually exists/works now? | verified code/runtime |
| Durable product north star and boundaries? | `docs/PROJECT_BRIEF.md` |
| Active milestone/slice/blocker/next work? | `docs/TASKS.md` |
| Current architecture/contracts/runtime strategy? | `docs/TECH_PLAN.md` + code |
| What has actually been verified? | `docs/QUALITY.md` or explicit evidence in `TASKS.md` |
| What must the next agent know **now**? | `docs/AGENT_HANDOFF.md` |
| Why did we get here / what failed before? | historical memory, outside this skill |
| Are knowledge surfaces mutually clean? | an auditor/reconciler such as `neat-freak` |

For **current-state** conflicts:

**verified code/runtime -> current operational docs -> historical material as context**.

Never preserve a stale operational claim merely because an older document or memory
entry says it was once true.

## Operational Docs

```text
docs/
├── PROJECT_BRIEF.md   # durable north star, users, boundaries, constraints
├── TASKS.md           # active milestone/slice, blocker, acceptance, near backlog
├── TECH_PLAN.md       # current architecture/contracts/runtime strategy
├── QUALITY.md         # optional verification evidence / quality gates
└── AGENT_HANDOFF.md   # concise current baton and exact next slice
```

Read `references/doc-templates.md` for templates and budgets.

## Ownership Boundaries

### This skill owns

- current project direction and boundaries;
- current milestone and active slice;
- current blocker/uncertainty;
- implementation versus verification state;
- current architecture/contracts when documented;
- exactly what the next agent should do next.

### This skill does not own

- historical narrative, old attempts, or why a superseded design once existed;
- per-session transcripts or changelogs;
- cleanup policy across unrelated docs/workspace artifacts;
- the user-facing orchestration of `project-memory`, this skill, and `neat-freak`.

A higher-level workflow such as `project-continue` may coordinate those components. When that
happens, perform only the current-state operation requested here and return control
to the orchestrator.

## Core Rules

1. Read operational docs before broad code exploration when aligning existing work.
2. Verify material current claims against code/runtime when stale state is plausible.
3. Keep one active slice unless parallel lanes are explicit.
4. State non-goals before implementation when scope could drift.
5. **Implemented** and **verified** are different states.
6. Update docs at meaningful planned/implemented/verified/handoff boundaries, not on
   every chat turn.
7. `TASKS.md` + `AGENT_HANDOFF.md` are the only owners of current next action.
8. `AGENT_HANDOFF.md` is a short baton, not a session transcript.
9. `PROJECT_BRIEF.md` changes only when durable product direction/boundaries change.
10. `TECH_PLAN.md` describes the current technical contract, not architecture history.
11. CLAUDE.md, AGENTS.md, rules, and similar instruction files contain durable
    constraints, commands, entry points, and pointers — not duplicate current status.

## Operation: Align / Resume Current State

Use when entering an existing project or when another workflow requests present-state
alignment.

1. Read current operational surfaces in this order:
   `AGENT_HANDOFF -> TASKS -> TECH_PLAN -> PROJECT_BRIEF -> QUALITY (if needed)`.
2. Inspect only enough code/git/runtime evidence to validate material or doubtful
   current claims.
3. Resolve contradictions explicitly using the Source-of-Truth Contract.
4. Report:
   - current direction;
   - current milestone and active slice;
   - recently verified result;
   - blocker, uncertainty, or unverified item;
   - exactly one recommended next action.
5. Do **not** infer historical rationale. If history is needed, tell the caller that a
   historical-memory layer should provide it.
6. If a higher-level orchestrator requested alignment, return the aligned state to it
   rather than starting unrelated work.

## Operation: Plan Current Slice

Define one observable goal with:

- scope;
- non-goals;
- acceptance criteria;
- verification method;
- blockers/dependencies;
- commit/review boundary when applicable.

Record it in `TASKS.md`. Keep the active slice small enough for another agent to
understand and verify independently.

## Operation: Implement / Diagnose

Stay inside the active slice. Update `TECH_PLAN.md` only when the **current**
architecture or contract genuinely changes.

For diagnosis, separate:

1. symptom;
2. evidence/reproduction;
3. root cause or current best explanation;
4. fix;
5. verification.

Do not turn the operational docs into a detailed story of failed attempts. Historical
lessons belong to the historical-memory layer.

## Operation: Verify

Verification is evidence, not confidence.

- Run the checks promised by the slice when possible.
- Record commands/results concisely enough for the next agent to trust the state.
- Mark unrun, partial, flaky, environment-blocked, or inferred checks honestly.
- Never convert "implemented" into "verified" without evidence.

## Operation: Synchronize for Handoff

Use when pausing/switching sessions or when `project-continue closeout` requests current-state
synchronization.

1. Inspect the current repository/worktree and available verification evidence.
2. Refresh `PROJECT_BRIEF.md` only if durable direction changed.
3. Refresh `TECH_PLAN.md` only if current technical contracts changed.
4. Refresh `TASKS.md` with the current milestone/slice, status, blocker, acceptance,
   and next action.
5. Refresh `QUALITY.md` when the project uses it and evidence changed.
6. Write `AGENT_HANDOFF.md` **last**, so it reflects the other current-state docs.
7. Keep the baton concise enough to scan in roughly two minutes.
8. Return a synchronization summary to the caller.

This operation does **not** invoke `project-memory` or `neat-freak`. If the user wants
full multi-skill continuity closeout, the `project-continue` orchestrator owns that sequence.

## Project Continue Interface

`project-continue` is the suite's optional user-facing orchestrator. This skill remains usable
without it.

When called by Project Continue:

- `project-continue resume` -> perform **Align / Resume Current State** and return current facts;
- `project-continue closeout` -> perform **Synchronize for Handoff** after reality has been
  inspected; write `AGENT_HANDOFF.md` last;
- `project-continue checkpoint` -> refresh only operational state that materially changed;
- `project-continue status` -> inspect/report operational health without writing files.

Never recursively invoke Project Continue from this skill.

## Interoperability Boundary

When a cleanup/governance tool such as `neat-freak` is present, preserve these
ownership rules:

- `TASKS.md` / `AGENT_HANDOFF.md`: current coordination and next action;
- `TECH_PLAN.md`: current technical contract;
- rules files: durable instructions/commands/pointers only;
- historical memory: past rationale/episodes, not current status.

Read `references/neat-freak-interop.md` for the compact reconciliation contract.

## ADR Boundary

Use ADRs/`DECISIONS.md` for decisions that remain normatively useful **now**.
Historical provenance, superseded options, and the path by which a decision emerged
belong to historical memory.

## Anti-Patterns

- current status duplicated into `.memory/`, CLAUDE.md, or AGENTS.md;
- `AGENT_HANDOFF.md` as a session transcript;
- `TASKS.md` as a permanent changelog;
- `PROJECT_BRIEF.md` as daily status;
- `TECH_PLAN.md` as architecture archaeology;
- multiple competing "next action" fields across docs;
- unrun verification marked complete;
- this skill invoking Memory/Neat-freak itself when Project Continue is the orchestrator.

## References / Verification

- `references/doc-templates.md`
- `references/neat-freak-interop.md`
- `references/migration-v2-to-v3.md`
- `scripts/init_handoff_docs.py`
- `scripts/validate_handoff_skill.py`
- `test-prompts.json`

Run static checks with:

```bash
python scripts/validate_handoff_skill.py .
```
