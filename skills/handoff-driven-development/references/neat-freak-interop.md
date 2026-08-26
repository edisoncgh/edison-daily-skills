# Neat-Freak Interoperability

`neat-freak` is a reconciliation/governance skill. Handoff-Driven Development is the
current operational control plane. Neither should duplicate the other's ownership.

## Ownership Matrix

- verified code/runtime: implementation reality;
- `handoff-driven-development`: current direction, milestone/slice, verification,
  blocker, and next action;
- `project-memory`: historical rationale, episodes, attempts, and lessons;
- `neat-freak`: audit/reconcile surfaces; it owns no project state.

## Guard for Cleanup/Audit

When a higher-level workflow such as `project-continue` invokes neat-freak, preserve this
project-specific contract:

> `docs/TASKS.md` and `docs/AGENT_HANDOFF.md` own current coordination and next
> action. `docs/TECH_PLAN.md` owns the current technical contract with code.
> `.memory/` is historical continuity. CLAUDE.md, AGENTS.md, rules, and similar
> instruction files contain durable constraints, commands, workflow entry points,
> and short pointers — not a duplicate current-state snapshot.

If a generic cleanup recommendation conflicts with this matrix, keep the established
single source of truth and reconcile other surfaces toward it.

Destructive cleanup remains subject to neat-freak's own authorization rules and the
host/user/project permissions. Handoff synchronization itself never grants deletion,
branch/worktree removal, deployment, or remote-write permission.
