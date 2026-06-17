---
name: handoff-driven-development-v2
description: Use when coordinating multi-session coding work through concise project docs, task slices, verification records, and agent handoffs while keeping operational docs distinct from project-memory.
---

# Handoff-Driven Development v2

Use this skill to keep agent-led development disciplined across long sessions,
tool switches, and partial implementations without letting docs become a second
memory system.

**TL;DR:** Maintain a small operational doc set: `PROJECT_BRIEF`, `TASKS`,
`TECH_PLAN`, `AGENT_HANDOFF`, and optional `QUALITY`. Work one slice at a time.
Plan -> implement -> verify -> handoff. Docs are the current operating surface;
project-memory is continuity and history; git is the rollback boundary.

**Not in scope:**
- This skill does not manage git branching strategy or CI/CD pipelines.
- This skill does not replace `project-memory`; it depends on a clean boundary
  with it.
- This skill does not provide code generation, debugging, or test-framework
  rules.
- This skill does not preserve unlimited history in active docs.

## Core Contract

- `docs/` = operational truth: current product brief, task board, technical plan,
  verification ledger, and next-agent handoff.
- `.memory/` = continuity memory: current session snapshot, durable lessons,
  prior decisions, and cross-session context.
- `git` = actual changed files, review surface, and rollback boundary.

`PROJECT_BRIEF.md` replaces older `CONTEXT.md` usage in this workflow. If a
legacy `docs/CONTEXT.md` exists, migrate stable project identity into
`docs/PROJECT_BRIEF.md` at the next doc-maintenance boundary, then leave a short
pointer or remove the duplicate according to the repo's rules.

## Required Project Docs

Minimum docs:

```text
docs/
  PROJECT_BRIEF.md  # stable product identity, users, runtime, boundaries, terms
  TASKS.md          # active milestone/slice, acceptance criteria, current debt
  TECH_PLAN.md      # architecture, module boundaries, contracts, commands
  AGENT_HANDOFF.md  # latest baton for the next agent/session
```

Optional docs by need:
- `QUALITY.md` / `TEST_PLAN.md`: verification commands, acceptance notes,
  regression history.
- `DECISIONS.md` / `docs/adr/`: important decisions and rationale.
- `API.md`, `DATA_MODEL.md`, `DEPLOYMENT.md`, `DESIGN_SYSTEM.md`, or
  domain-specific docs.

If docs are missing and the user wants the workflow installed, run
`scripts/init_handoff_docs.py` or create equivalent files manually. See
`references/doc-templates.md` for templates.

## Document Budgets

Budgets are maintenance signals, not hard failures. When a doc exceeds its max,
trim, split, or archive before adding more detail.

| Doc | Target | Max | Job |
|---|---:|---:|---|
| `PROJECT_BRIEF.md` | 100-180 lines | 250 | Stable project identity: product, users, runtime, boundaries, core terms. |
| `TASKS.md` | <=180 lines | 220 | Active milestone and next slices only; archive completed history. |
| `TECH_PLAN.md` | <=600 lines | 700 | Current architecture and contracts; split large domain sections. |
| `AGENT_HANDOFF.md` | <=50 lines | 80 | 2-minute handoff: exact next action, evidence, blockers, files. |
| `QUALITY.md` | concise current milestone | archive at 1500 | Verification ledger; summarize old logs and move history out. |
| `DECISIONS.md` / ADRs | one decision per entry | split by ADR | Short rationale and consequences, not meeting notes. |

## Source-of-Truth Map

| Question | Read / update |
|---|---|
| What is this project and what are its stable boundaries? | `docs/PROJECT_BRIEF.md` |
| What are we doing now? | `docs/TASKS.md` |
| How is the system shaped? | `docs/TECH_PLAN.md` |
| What can the next agent do in two minutes? | `docs/AGENT_HANDOFF.md` |
| What has been verified? | `docs/QUALITY.md` or the verification section in `TASKS.md` |
| What should survive across sessions as memory? | `.memory/context.md` and `.memory/knowledge.md` through `project-memory` |

Use `project-memory` for volatile/current session snapshots and long-term
lessons. Do not copy `.memory/context.md` into `PROJECT_BRIEF.md`. Do not turn
`AGENT_HANDOFF.md` into a session transcript.

## Boundary Conditions

| Scenario | Trigger | Action |
|---|---|---|
| Legacy `docs/CONTEXT.md` exists | Project predates v2 | Migrate stable identity to `PROJECT_BRIEF.md`; avoid duplicate truth. |
| Docs conflict with code | Code behavior contradicts docs | Stop coding, verify reality, update docs, then resume. |
| Docs conflict with memory | `.memory/` says one thing and docs say another | Treat docs as current operating truth; update stale memory or doc intentionally. |
| `TASKS.md` becomes a changelog | Completed milestone history dominates current work | Archive history and keep only active milestone/slice. |
| `AGENT_HANDOFF.md` exceeds 80 lines | Handoff cannot be read in two minutes | Trim to latest state and move detail to `TASKS`, `QUALITY`, or archives. |
| Existing project has docs | README/CONTRIBUTING/domain docs already exist | Read them and seed docs without overwriting useful content. |
| TASKS.md stale | Checkboxes don't match code or git log | Refresh state with tests/logs/git before proceeding. |
| No test infrastructure | No test runner exists | Record in `QUALITY.md`; use manual acceptance and do not fake TDD. |
| Slice too large | Work cannot complete in one session | Split into sub-slices, mark partial progress, and update handoff. |
| User skips verification | User wants unchecked behavior marked done | Leave verification unchecked; record external/user verification separately. |

## Rules

1. Read docs before code when continuing work.
2. Keep one active slice. Do not begin a second slice until the current one is
   verified or explicitly paused.
3. State non-goals before implementation.
4. Implementation done is not verification done.
5. Update docs at slice boundaries: planned, implemented, verified, handed off.
6. Active docs answer only: what to do, what is done, how to verify, what is
   next.
7. Archive old detail instead of letting active docs grow without limit.

## Workflow Decision Tree

- **New project / workflow setup** -> Initialize docs.
- **New session / agent switch** -> Resume workflow.
- **Before coding a feature** -> Plan slice.
- **During implementation** -> Implement slice.
- **Bug, mismatch, or failed acceptance** -> Stabilize/diagnose.
- **Feature appears done** -> Verify and close slice.
- **Pause or handoff** -> Handoff workflow.
- **Docs over budget** -> Trim/split/archive before adding new material.

## Initialize Docs

1. Inspect existing project docs and manifests.
2. Create missing minimum docs only; do not overwrite useful existing docs.
3. Seed `PROJECT_BRIEF.md` with stable project identity, users, runtime,
   constraints, domain terms, and update rules.
4. Seed `TASKS.md` with current milestone, next slice, non-goals, acceptance
   criteria, and current debt/backlog.
5. Seed `TECH_PLAN.md` with architecture, file map, contracts, and verification
   commands.
6. Seed `AGENT_HANDOFF.md` with current state, next action, blockers,
   verification steps, and files of interest.
7. If `project-memory` exists, record only that the docs workflow was
   initialized; do not duplicate all doc content into memory.

## Resume Workflow

At session start or when switching agents:

1. Use `project-memory` if available: read `.memory/context.md`,
   `.memory/knowledge.md`, and relevant recent memory entries.
2. Read `docs/AGENT_HANDOFF.md`, `docs/TASKS.md`, `docs/TECH_PLAN.md`, and
   `docs/PROJECT_BRIEF.md`.
3. Read optional/domain docs only if the current slice needs them.
4. Check document budgets quickly; trim only if the active work would worsen an
   already oversized doc.
5. Summarize current state, active slice, blockers, and next recommended action.
6. **CHECKPOINT:** Confirm current slice and acceptance criteria before coding
   unless the user has explicitly authorized execution.

## Plan Slice

Before coding, write or confirm:

- Goal: one sentence.
- Scope: files/modules likely touched.
- Explicitly not in scope.
- Acceptance criteria: observable checks, not vague outcomes.
- Verification mode:
  - Pure logic -> tests/verification functions.
  - Integration/visual/runtime behavior -> logs, screenshots, manual acceptance.
- Commit boundary: expected commit message.

Update `TASKS.md` if the slice is not already represented. If adding this slice
would push `TASKS.md` over budget, archive completed history first.

## Implement Slice

1. Change one concern at a time.
2. Do not refactor outside the current slice scope; note it for later.
3. Keep boundaries described in `TECH_PLAN.md`. If a boundary changes, update
   `TECH_PLAN.md` deliberately.
4. If requirements conflict with docs, stop and reconcile the docs first.
5. Add tests or verification hooks where practical.
6. For runtime/visual work, record exact manual verification steps and expected
   observations.

## Stabilize / Diagnose

Use when implementation claims do not match runtime behavior.

1. Treat reports as hypotheses; trust logs, screenshots, tests, and reproduction.
2. Reproduce the issue and separate symptoms from root causes.
3. Restrict fixes to the current slice unless the user approves scope expansion.
4. For logic bugs, add or adjust tests to capture the failure.
5. For visual/integration bugs, add diagnostics and manual acceptance criteria.
6. Record root cause and fix in `AGENT_HANDOFF.md`; use memory only for reusable
   lessons.

## Verify and Close Slice

1. Run the stated tests/commands.
2. Perform manual acceptance steps when required.
3. Present verification results to the user when human observation matters.
4. Update `TASKS.md`: implementation and verification items separately.
5. Update `QUALITY.md` or the task verification section with concise evidence.
6. Update `AGENT_HANDOFF.md`: current state, verified behavior, known issues,
   next step.
7. Update project memory only for durable decisions, pitfalls, and verified
   state.
8. Commit only when the user or repo workflow calls for it.

## Handoff Workflow

When pausing, switching agents, or ending a work session, update
`AGENT_HANDOFF.md` with:

- Current milestone and slice status.
- Last completed work and commit, if any.
- What was verified by user/runtime/tests.
- Current blockers and known issues.
- Next recommended action: one slice only.
- Files of interest.
- Run and verification commands.
- Explicit non-goals for the next agent.

Run the 2-minute handoff test: a new agent reading only `AGENT_HANDOFF.md`
should know what to do next within two minutes. If not, shorten the file and
move supporting detail elsewhere.

## Anti-Patterns

- `PROJECT_BRIEF.md` as a current-status diary.
- `TASKS.md` as a full changelog or release archive.
- `AGENT_HANDOFF.md` as a transcript of the whole session.
- `TECH_PLAN.md` as a line-by-line code diary.
- `QUALITY.md` as pasted raw logs with no conclusion.
- Duplicating `.memory/context.md` into docs or copying all docs into memory.
- Checking off verification that has not actually run.
- Keeping outdated TODOs because deleting them feels risky.

## Static Verification

Use these checks when editing the workflow itself or repairing project docs:

```bash
wc -l docs/PROJECT_BRIEF.md docs/TASKS.md docs/TECH_PLAN.md docs/AGENT_HANDOFF.md docs/QUALITY.md
rg -n "CONTEXT.md|current session|today|next step" docs/PROJECT_BRIEF.md
rg -n "CONTEXT.md|PROJECT_BRIEF|AGENT_HANDOFF|TASKS" .agents/skills/handoff-driven-development-v2
```

Intentional legacy-migration mentions of `CONTEXT.md` are allowed; active
templates and prompts should use `PROJECT_BRIEF.md`.

## Reference Files

- Read `references/doc-templates.md` when initializing or repairing docs.
- Read `references/workflow-prompts.md` when drafting prompts for agents.
- Use `scripts/init_handoff_docs.py` to scaffold the minimum docs without
  overwriting existing files.
