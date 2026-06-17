# Workflow Prompt Patterns

Use these patterns to brief coding agents. Adapt to the project and keep scope narrow.

## Resume Prompt

```text
Please resume this project using handoff-driven development v2.

First restore context:
1. Use project-memory if available; read .memory/context.md and .memory/knowledge.md.
2. Read docs/AGENT_HANDOFF.md, docs/TASKS.md, docs/TECH_PLAN.md, docs/PROJECT_BRIEF.md.
3. Read only the code files needed for the current slice.

Then report:
- current milestone and slice
- verified state
- blockers
- next recommended action
- any active doc that is over budget
Do not write code yet.
```

## Plan Slice Prompt

```text
Please plan the next slice before coding.

Define:
1. Goal
2. Scope and likely files
3. Explicitly not in scope
4. Acceptance criteria
5. Verification mode: tests for pure logic, diagnose/manual acceptance for runtime/visual/integration
6. Commit boundary

Update docs/TASKS.md if the slice is not represented. If TASKS.md is over budget, archive completed history first. Do not implement yet.
```

## Implement Slice Prompt

```text
Please implement only the current slice.

Follow docs/TASKS.md and docs/TECH_PLAN.md.
Do not implement items listed as not in scope.
Use the project's existing test/diagnose workflow.
After implementation, output changed files, verification steps, warnings/errors, docs updates, memory updates, and commit status.
```

## Diagnose Prompt

```text
Please diagnose the current slice failure.

Observed behavior:
[Paste logs/screenshots/symptoms]

Allowed scope:
[Current slice files/systems]

Do not implement unrelated features.
Separate symptoms from root causes.
Add tests for pure logic failures where practical.
Add diagnostic logs/manual checks for runtime or visual failures.
After fixing, update AGENT_HANDOFF.md and concise verification evidence.
```

## Verification Close Prompt

```text
The slice has been manually verified.

Verified behavior:
[List observed checks]

Please only close the slice:
1. Update docs/TASKS.md verification items.
2. Update docs/QUALITY.md or concise verification notes.
3. Update docs/AGENT_HANDOFF.md, keeping it under 80 lines.
4. Update project-memory only with verified state and lasting decisions.
5. Do not implement new features.
```

## Handoff Prompt

```text
Please prepare a handoff.

Update docs/AGENT_HANDOFF.md with current state, last commit, verified behavior, blockers, next recommended slice, files of interest, run/verify steps, and explicit non-goals.
Apply the 2-minute handoff test and keep it under 80 lines.
Update project-memory context only for the volatile/current session snapshot. Do not implement new features.
```
