---
name: project-continue
description: Use when the user says "project-continue closeout" or "project-continue resume", or wants to switch coding agents/sessions, prepare a handoff, restore work in a fresh context, checkpoint continuity, or inspect continuity health. Also trigger on "准备交接", "换会话", "接力开发", "上下文快满了", or "额度快耗尽".
---

# Project Continue — Portable Project Continuity Orchestrator

Project Continue is the **user-facing orchestration layer** for project continuity across coding
agents and fresh sessions.

It owns no project facts. It coordinates three independent companion skills:

- `project-memory` — historical continuity: how and why the project got here;
- `handoff-driven-development` — current direction/state: where the project is now
  and what happens next;
- `neat-freak` — reconciliation/governance: whether project knowledge surfaces agree
  with verified reality.

## Portability Contract

Project Continue must remain useful on any Agent Skills-compatible host and degrade gracefully
on hosts with weaker skill support.

1. The canonical invocation is ordinary user text: `project-continue <mode>`.
2. Never require a slash command, sigil-based skill selector, vendor-specific argument
   expansion, a specific command registry, or vendor-only frontmatter.
3. Native slash/tag/skill selectors are optional shortcuts only.
4. Use the host's normal skill-discovery/invocation mechanism to load companion
   skills by their exact names. Do not guess vendor-specific install paths from this
   skill.
5. If the host cannot nest skill invocations but can read installed skill files,
   load the named companion `SKILL.md` instructions through the host's normal file or
   skill discovery mechanism and follow them in the same agent loop.
6. If a companion skill is unavailable, never invent its hidden contents. Follow the
   degraded-mode rules below and report the missing component.
7. Host/system/user/project permissions always override Project Continue. Project Continue coordinates
   work; it does not grant filesystem, network, deletion, deployment, credential, or
   remote-write permission.

See `references/portability.md` for host adapters and installation guidance. The
core workflow below must not depend on that reference.

## Modes

Infer the mode from the user's invocation or intent.

| Mode | Meaning | Writes? |
|---|---|---|
| `closeout` | Prepare this project for transfer to another agent/session | Yes, non-destructive continuity updates |
| `resume` | Restore continuity in a fresh agent/session | Read-first; normal development only after alignment |
| `checkpoint` | Synchronize continuity without ending the session | Yes, lightweight |
| `status` | Inspect continuity health | No |

Natural-language equivalents are valid. Examples:

- closeout: `project-continue closeout`, `准备交接`, `换个 agent`, `上下文快满了，准备接力`
- resume: `project-continue resume`, `接棒`, `继续上一个 agent 的开发`, `恢复项目上下文`
- checkpoint: `project-continue checkpoint`, `同步一下连续性状态但不换会话`
- status: `project-continue status`, `检查一下交接状态，不要改文件`

If the requested mode is genuinely ambiguous, prefer the least destructive
interpretation: `status` over `checkpoint`, and `checkpoint` over `closeout`.

## Source-of-Truth Contract

| Question | Owner |
|---|---|
| What actually exists/works now? | verified code/runtime |
| Why did we get here / what failed before? | `project-memory` |
| Current north star, milestone, slice, blocker, verification, next action | `handoff-driven-development` operational docs |
| Are docs/rules/memory/workspace mutually consistent? | `neat-freak` audit; it owns no project state |

For current-state conflicts use:

**verified code/runtime -> current handoff docs -> historical memory**.

Do not "merge" contradictory time slices into an invented compromise. Historical
memory may be perfectly correct for an earlier date while being stale as current
state.

## Cross-Skill Interoperability Guard

Whenever Project Continue uses `neat-freak`, provide this suite-specific constraint:

> This project uses Project Continuity Suite. `docs/TASKS.md` and
> `docs/AGENT_HANDOFF.md` own current milestone/slice/blocker/verification/next
> action. `docs/TECH_PLAN.md` owns the current technical contract with code.
> `.memory/` is project-owned historical continuity. CLAUDE.md, AGENTS.md, rules,
> and similar instruction files contain durable constraints, commands, workflow
> entry points, and short pointers — not a duplicate current-state snapshot.
> Reconcile against those ownership boundaries; do not create another source of
> current truth.

This guard specializes generic neat-freak cleanup behavior without modifying its
upstream skill.

## Mode: `closeout`

Use when context/quota is ending, the user is switching coding agents, or the user
intentionally pauses multi-session development.

Execute stages in order. Re-running closeout should converge toward the same state.

### 1. Freeze Reality

Inspect enough repository/runtime evidence to know what is actually true now:

- working tree / branch / recent relevant commits when git exists;
- modified and untracked files relevant to the current work;
- implementation state of the active slice;
- tests, build, lint, runtime, deployment, or other verification evidence that is
  relevant and available.

Do not reconstruct current repository state from chat memory alone.

### 2. Persist Historical Continuity

Use `project-memory` in **persist/closeout** intent.

Persist only historically useful developments from this work period: decisions and
rationale, meaningful transitions, failed approaches, non-obvious fixes, important
requirement changes, environment/toolchain quirks, and reusable pitfalls.

Do not put current milestone, blocker, slice, verification status, or next action in
memory. "No meaningful new memory" is a valid result.

Before creating an episode, check whether the same event was already persisted by a
partial earlier closeout.

### 3. Synchronize the Operational Control Plane

Use `handoff-driven-development` in **closeout/sync** intent.

Synchronize current project truth, especially:

- `PROJECT_BRIEF.md` only if durable direction/boundaries changed;
- `TASKS.md` for active milestone/slice, acceptance, blocker, near backlog;
- `TECH_PLAN.md` only when the current technical contract changed;
- `QUALITY.md` when the project uses it and verification evidence changed;
- `AGENT_HANDOFF.md` last, as the concise current baton.

Update authoritative sections; do not append duplicate snapshots.

### 4. Reconcile Knowledge Surfaces

If `neat-freak` is available, use it with the interoperability guard above.

Project Continue closeout authorizes routine, non-destructive project-local knowledge sync
needed for handoff. It does **not** by itself authorize deleting files, branches,
worktrees, backups, remote resources, deployments, credentials, or other destructive
or external actions. Let neat-freak report cleanup candidates under its own rules.

If neat-freak is unavailable, perform only this minimal fallback audit:

- active handoff docs do not conflict with verified reality;
- rule/instruction files do not duplicate current milestone/blocker/next action;
- memory does not masquerade as current state;
- no obvious stale pointer introduced by this closeout remains unreported.

Report the missing neat-freak component; do not fail the whole project-continue solely for it.

### 5. Continuity Audit

Confirm:

- current state is represented once in the handoff control plane;
- historical memory remains historical;
- "implemented" is not mislabeled "verified";
- the next action is specific enough for a fresh agent;
- `AGENT_HANDOFF.md` is concise enough to act as a baton, not a transcript;
- no companion stage silently failed or was unavailable.

### 6. Finish

Return a concise readiness report, for example:

```text
PROJECT CONTINUE READY
Memory: synchronized | no new historical event | unavailable
Handoff: synchronized
Knowledge audit: passed | pending: <reason>
Verification: <verified evidence or explicit pending>
Working tree: <brief factual state>
Next session: project-continue resume
```

The next-session instruction is **stateless**. Do not embed another copy of the
current milestone/blocker/next action into a generated resume prompt unless the user
explicitly asks for a snapshot. `project-continue resume` should recover truth from the project.

## Mode: `resume`

Use in a fresh session/agent after a prior handoff or whenever the user wants to
restore project continuity.

**Do not edit implementation code until continuity restoration completes.** Reading,
status inspection, and non-mutating verification are allowed.

### 1. Recall Relevant History

Use `project-memory` in **recall** intent. Recover only history relevant to the
current work: decisions, previous attempts, transitions, pitfalls, and non-obvious
lessons. Do not treat a historical unresolved item as today's next action.

If project-memory is unavailable but `.memory/` is visibly present, report the
missing skill rather than reverse-engineering or mutating the store. You may read
clearly indexed historical material only when safe and necessary for degraded-mode
resume.

### 2. Align Current State

Use `handoff-driven-development` in **resume/align** intent. Read the operational
control plane and identify current direction, milestone/slice, verification state,
blockers/uncertainties, and the next action.

If the handoff skill is unavailable, do not claim a full Project Continue resume. Inspect the
project's known operational docs if they are self-evident, report degraded mode, and
avoid inventing a substitute state schema.

### 3. Verify Reality

Inspect enough current code/git/runtime evidence to validate material current-state
claims. Resolve contradictions using the Source-of-Truth Contract.

Do not rewrite historical memory merely because the project has moved on.

### 4. Produce Resume Brief

Report before continuing:

- project direction;
- current milestone and active slice;
- latest verified result;
- blocker, uncertainty, or unverified item;
- one recommended next action;
- relevant historical warning/lesson, if any;
- any continuity inconsistency discovered.

### 5. Continue

If the user's request already authorizes continued development and no decision is
needed, resume normal work after the brief. Otherwise stop at the aligned state and
wait for the user's next instruction.

## Mode: `checkpoint`

Use for a lightweight in-session synchronization without declaring a handoff.

1. Inspect the current slice and verification evidence.
2. Use `project-memory` only if a meaningful historical event was created.
3. Use `handoff-driven-development` to refresh current operational state.
4. Do not run full neat-freak by default unless the user requested cleanup or a
   contradiction is already visible.
5. Report what changed and continue the current session.

Checkpoint is not a substitute for closeout when another agent must take over.

## Mode: `status`

Read-only.

Inspect whether the continuity surfaces exist and agree sufficiently to support a
handoff/resume. Do not modify memory, handoff docs, rules, source files, branches,
worktrees, or remote state.

Report:

- companion skills detected/available when the host exposes that information;
- memory state: present/missing/legacy/uncertain;
- handoff state: present/missing/stale/uncertain;
- current-state contradictions found;
- whether a `closeout`, `resume`, migration, or manual repair is recommended.

## Idempotency

- Do not create duplicate memory episodes for the same event.
- Synchronize current docs in place; do not append repeated handoff blocks.
- Repeated `closeout` should converge, not accumulate narrative.
- Repeated `resume` is read-first and should not mutate the project merely because it
  was run twice.

## Failure / Degraded Mode

A companion skill can be unavailable, disabled, unsupported by a subagent, or
blocked by host permissions.

- Say which component is unavailable.
- Complete independent safe stages when possible.
- Never claim `PROJECT CONTINUE READY` if the mandatory handoff control plane could not be
  synchronized or material current-state contradictions remain unresolved.
- `neat-freak` is optional for functional handoff; `project-memory` and
  `handoff-driven-development` are core suite dependencies for full-fidelity Project Continue.
- A host without Agent Skills can still use Project Continue by supplying this SKILL.md plus the
  companion SKILL.md files as project instructions; the ownership and permission
  contracts remain unchanged.

## Completion Contracts

### Closeout is complete only when

- repository/current reality was inspected;
- meaningful history was persisted or explicitly judged unnecessary;
- current handoff state was synchronized;
- verification status is honest;
- reconciliation ran or its degraded fallback is explicitly reported;
- cross-surface contradictions are resolved or clearly pending;
- a concise readiness report is produced.

### Resume is complete only when

- relevant history was recalled or explicitly unavailable;
- current handoff state was read/aligned;
- material current claims were checked against reality;
- contradictions were resolved or reported;
- a resume brief was produced before implementation edits.
