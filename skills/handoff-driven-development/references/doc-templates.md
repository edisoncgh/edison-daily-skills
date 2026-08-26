# Handoff-Driven Development — Operational Doc Templates

Adapt headings to the project. Keep one authoritative current answer per fact.

## docs/PROJECT_BRIEF.md

```markdown
# Project Brief

## North Star
[One or two sentences: what outcome this project exists to create.]

## Product / Users
- Product:
- Primary users / environment:

## Durable Boundaries
- In scope:
- Out of scope:

## Runtime / Platform Constraints
- Language/runtime:
- Frameworks/tools:
- Target platform:

## Core Capabilities
- [Capability]

## Domain Terms
- `[term]`: [meaning]

## Source of Truth
- Current tasks: `docs/TASKS.md`
- Current architecture/contracts: `docs/TECH_PLAN.md`
- Current baton: `docs/AGENT_HANDOFF.md`
- Verification: `docs/QUALITY.md` if present
- Historical rationale/lessons: `.memory/` if project-memory is installed

## Update Rule
Change this file only when stable direction, users, durable boundaries, runtime constraints, or domain language changes. Do not record current blockers or next action here.
```

## docs/TASKS.md

```markdown
# Tasks

## Current Milestone: [name]

### Goal
[Observable milestone outcome.]

### Scope
- [included]

### Explicitly NOT in Scope
- [excluded]

### Acceptance Criteria
- [ ] [observable check]

## Current Slice: [name]
- [ ] Implement: [specific change]
- [ ] Verify: [specific evidence]

## Blockers / Unverified
- [ ] [current blocker or unverified claim]

## Near Backlog
- [ ] [next likely slice]

## Debt / Later
- [ ] [non-blocking debt]

## Archive Pointer
- [where completed history lives, if needed]
```

## docs/TECH_PLAN.md

```markdown
# Technical Plan

## Current Architecture Summary
[Current components and boundaries only.]

## File / Module Map
- `path`: responsibility

## Data / Control Flow
[Current flow.]

## Interfaces / Contracts
[Current APIs/types/events/state transitions.]

## Runtime / Verification Strategy
- Start/run:
- Tests:
- Integration/runtime checks:
- Manual acceptance:

## Current Risks / Constraints
- [risk/constraint and mitigation]
```

## docs/AGENT_HANDOFF.md

```markdown
# Agent Handoff

## Current Direction
[One sentence linking current work to the project north star.]

## Current State
[What currently works / is in progress.]

## Last Completed & Verified
- Work:
- Commit (if any):
- Evidence:

## Current Blockers / Unverified
- [item]

## Next Recommended Step
[One slice only.]

## Explicit Non-Goals
- [do not do yet]

## Files of Interest
- `path`: why

## Run / Verify
1. [command/action]
2. [expected observation]
```

## docs/QUALITY.md

```markdown
# Quality / Verification

## Current Milestone Evidence
- `[command or scenario]` — [result and what it proves]

## Manual Acceptance
- [scenario] — [observed / pending]

## Known Unverified Claims
- [claim and required evidence]

## Archive Pointer
- [older verification detail]
```

## docs/DECISIONS.md / ADR

Use for decisions that remain operationally/normatively relevant. Keep historical
journeys and supersession rationale in project-memory.
