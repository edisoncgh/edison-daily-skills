# Project Memory v2 — Management Rules

## File Responsibilities

| Surface | Responsibility | Lifetime |
|---|---|---|
| `.memory/index.md` | Retrieval index for historical episodes | Persistent |
| `.memory/knowledge.md` | Distilled historical rationale, lessons, pitfalls, transitions | Persistent, curated |
| `.memory/episodes/` | Evidence-backed development events | Persistent |
| Handoff docs | Current direction, milestone, slice, blockers, verification, next action | Current/operational |
| Code/runtime | What actually exists and behaves now | Current reality |

`.memory/context.md` and `.memory/sessions/` are legacy v1 surfaces only.

## Size Guidance

- Episode: target **40-120 lines**, max **180 lines**. Split unrelated events.
- `knowledge.md`: target **<=300 lines**; refactor by topic when it grows beyond 400.
- `index.md`: one line per episode. Group by month/year when large.

Do not use arbitrary episode-count pruning. **Never automatically delete unique
historical evidence because the count crossed a threshold.**

## Event-Oriented Persistence

### STORE

- Decisions and reversals with rationale.
- Meaningful completed/abandoned slices and their outcome.
- Failed approaches that are likely to be retried.
- Non-obvious bug root causes and fixes.
- Environment/toolchain quirks and reproducible workarounds.
- User/product choices that materially changed project direction.
- Important transitions between architectures, dependencies, providers, schemas, or workflows.
- Verification evidence needed to understand what was true at the time.

### SKIP

- Chat transcripts and routine tool calls.
- "Next step" lists whose only value is current coordination.
- Current milestone/slice/blocker snapshots.
- Raw logs already summarized by an outcome.
- Full source code, diffs, generated output, or copied current docs.
- Trivial edits obvious from git history.
- Repetitive confirmations with no new information.

## Episode Rules

- Use past tense and absolute dates.
- One episode = one coherent event or transition.
- Link related episodes instead of merging unrelated history.
- Cite file paths and commits when available.
- Separate **observed evidence** from **interpretation/rationale**.
- "Unresolved at the time" is allowed, but must explicitly say current status lives elsewhere.
- If a later episode supersedes an earlier decision, keep both and link the transition.

## Knowledge Distillation Rules

`knowledge.md` is curated, not append-only.

Keep:
- decision rationale that remains useful for understanding history;
- recurring pitfalls/failure patterns;
- durable environment quirks;
- important transitions and why they happened;
- project-specific preferences that explain prior choices.

Do not keep:
- a current architecture inventory that duplicates `TECH_PLAN.md`;
- a current task list;
- a current next step;
- active operational rules that belong in CLAUDE.md/AGENTS.md/project docs.

When knowledge becomes an active rule/contract, move the authoritative statement to
the correct current surface and leave only provenance/history in memory.

## Conflict Handling

- **Current-state conflict:** trust verified runtime/code first, then current handoff
  docs. Memory explains history but does not win current-state arbitration.
- **Historical conflict:** preserve both if they describe different dates/stages;
  create a transition episode when needed.
- **Evidence conflict:** mark uncertainty; do not invent a resolution.
- **Legacy v1 conflict:** treat `.memory/context.md` as a staleable historical
  artifact, never as authoritative current state.

## Privacy

- Never store API keys, passwords, tokens, cookies, private keys, or credential values.
- Redact token-bearing URLs and sensitive local paths when unnecessary.
- Reference "credentials configured" rather than copying secrets.
