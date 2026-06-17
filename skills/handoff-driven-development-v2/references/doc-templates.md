# Document Templates

Use these flexible templates when creating or repairing project docs. Adapt headings to the project; do not fill with noise. Keep active docs within their budgets.

## docs/PROJECT_BRIEF.md

Target: 100-180 lines. Max: 250 lines. This is stable project identity, not current session state.

```markdown
# Project Brief

## Product
[What the product is and why it exists.]

## Users
- [Primary user and environment]

## Runtime / Stack
- Language/runtime:
- Frameworks/tools:
- Target platform:

## Product Boundaries
- In scope:
- Out of scope:

## Core Capabilities
- [Capability]

## Domain Terms
- `[term]`: [meaning]

## Source Of Truth
- Tasks:
- Technical plan:
- Handoff:
- Memory:

## Update Rules
- Update this file only when stable project identity, runtime, domain language, or long-lived boundaries change.
- Do not record current slice status, session notes, or temporary blockers here.
```

## docs/TASKS.md

Target: <=180 lines. Max: 220 lines. Keep only active milestone and current backlog; archive completed history.

```markdown
# Tasks

## Current Milestone: [Name]

### Goal
[One-sentence outcome.]

### Scope
- [What is included.]

### Explicitly NOT in Scope
- [What the next agent must not implement.]

### Acceptance Criteria
- [ ] [Observable check]
- [ ] [Test/manual verification]

## Current Slice: [Name]
- [ ] Implement: [file/module/task]
- [ ] Verify: [specific verification]

## Bugs / Stabilization
- [ ] [Issue and acceptance criteria]

## Technical Debt / Polish Debt
- [ ] [Debt item, why it is not blocking]

## Later / Backlog
- [ ] [Deferred work]

## Archives
- [Completed history moved to docs/archive/...]
```

## docs/TECH_PLAN.md

Target: <=600 lines. Max: 700 lines. Split domain detail when it grows too large.

```markdown
# Technical Plan

## Architecture Summary
[Main components and boundaries.]

## File / Module Map
- `path`: responsibility

## Data / Control Flow
[Key runtime flow or request flow.]

## Interfaces / Contracts
[Important types, APIs, events, state transitions.]

## Testing and Verification Strategy
- Pure logic:
- Integration/runtime:
- Manual acceptance:

## Known Risks
- [Risk and mitigation.]
```

## docs/AGENT_HANDOFF.md

Target: <=50 lines. Max: 80 lines. A new agent should know the next action within two minutes.

```markdown
# Agent Handoff

## Current State
[What currently works.]

## Last Completed Work
- Commit:
- Files changed:
- Verified behavior:

## Current Blockers / Known Issues
- [Issue, evidence, next diagnostic step.]

## Next Recommended Step
[One slice only.]

## Explicit Non-Goals for Next Agent
- [Do not do these yet.]

## Files of Interest
- `path`: why it matters

## Run / Verify Steps
1. [Command/action]
2. [Expected result]
```

## docs/DECISIONS.md

```markdown
# Decisions

## YYYY-MM-DD - [Decision Title]

Decision: [What was decided.]

Rationale:
- [Reason]

Consequences:
- [Tradeoff or follow-up]
```

## docs/QUALITY.md / docs/TEST_PLAN.md

Keep current milestone evidence concise. Archive or summarize when the file exceeds 1500 lines.

```markdown
# Quality Plan

## Automated Checks
- [Command] - [What it proves]

## Manual Acceptance
- [Scenario] - [What to observe]

## Regression Checklist
- [ ] [Critical behavior]

## Archive Links
- [Older verification detail moved to docs/archive/...]
```
