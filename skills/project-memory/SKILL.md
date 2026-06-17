---
name: project-memory
description: "Maintain persistent project-level memory across sessions by reading and writing markdown files in the .memory directory. Use when: starting a new project, continuing work after a break, user says 'remember this', 'what did we do about X', 'vibe coding', 'keep track', 'don't forget', 'project context', 'what was the decision on...', or any multi-turn development work. Triggers: project-memory, vibe coding, remember, memory, context, continuity."
---

# Project Memory Skill

You have access to a **project-level persistent memory system** stored in the `.memory/` directory at the project root. This skill ensures continuity across sessions — especially critical for **vibe coding** workflows where development happens over many turns and breaks.

## Memory Directory Layout

```
.memory/
├── context.md                # MANDATORY — current working snapshot (volatile, rewrite on each update)
├── index.md                  # Memory index — lists all session files with one-line summaries + tags
├── knowledge.md              # Long-term knowledge — architecture, user preferences, conventions, decisions
└── sessions/
    ├── 20260209-143022.md    # One file per conversation turn
    ├── 20260210-091500.md
    └── ...
```

`context.md` is **mandatory**. If `.memory/` exists but `context.md` is missing or empty, treat it as a broken memory state and repair immediately (see "Repair Existing Memory" below).

## When to Use This Skill

**ALWAYS activate at session start if `.memory/` exists.**

Also activate when user mentions:
- "remember this", "keep track of", "don't forget"
- "what did we do about X", "what was the decision on..."
- "vibe coding", "continue where we left off"
- Any multi-file, multi-turn development task
- Any modification, development, operation or work finished

---

## Workflow A — Session Start (MUST follow when .memory/ exists)

### Phase 1 — Recall

1. **Read** `.memory/index.md`
   - If missing: `.memory/` not initialized → skip to Workflow C
2. **Read** `.memory/context.md` for active working state
   - If missing or empty: **repair immediately** — do not skip. See "Repair Existing Memory" below.
   - If stale (e.g., Status is ACTIVE but last update was > 7 days ago, or content contradicts `docs/TASKS.md` / `docs/AGENT_HANDOFF.md`): refresh after reading index, knowledge, and recent sessions.
3. **Read** `.memory/knowledge.md` for long-term context
4. **Query relevant sessions** (see Session Query Strategy below)
   - Read no more than 3 session files at a time
   - Prioritize: most recent + tags matching current topic
5. **Summarize recalled context** in 2-3 sentences (internal reasoning)

### Phase 2 — Respond with Memory

- Use recalled memory to avoid redundant questions
- Reference specific past decisions: "As we decided on 2026-02-09, we use the adapter pattern..."
- Check `.memory/context.md` open items — proactively offer to continue

### Phase 3 — Persist (after each turn)

1. **Create** `.memory/sessions/<YYYYMMDD-HHmmss>.md` using `template/session.md`
2. **Update** `.memory/index.md` — append entry with tags
3. **Update** `.memory/knowledge.md** — if lasting insight gained
4. **Update** `.memory/context.md` — **MANDATORY** at every meaningful development step:
   - Rewrite the file (do not append). Use `template/context.md` as structure.
   - Record: current goal, current slice, last known good state, active files, working state, blocker, next action, verification status, scope guardrails.
   - If project uses `docs/TASKS.md` / `docs/AGENT_HANDOFF.md`, reference them by path — do not copy their content.
   - Max 100 lines. If over, trim history and move durable facts to `knowledge.md`.
5. **User checkpoint** — if significant decision made, ask: "Should I record this in long-term memory?"

---

## Workflow B — Vibe Coding Mode (continuous development)

For extended coding sessions where user is iteratively building:

### Every 3-5 turns OR at natural break points:

1. **Rewrite** `.memory/context.md` (use `template/context.md` structure):
   - Current goal and slice
   - Active files
   - Working state (key functions/classes, not full code)
   - Current blocker (if any)
   - Next action
   - Verification status
   - Scope guardrails (Do Not Do)

2. **Tag the session** in index.md with `vibe-coding` tag

3. **If user says "break"/"pause"/"later"**:
   - Write detailed context summary
   - List all files modified in this session
   - Note: "User paused work, will continue later"

---

## Workflow C — First Time Initialization

When `.memory/` does NOT exist and user starts a project:

1. **Ask user**: "Should I set up project memory to track our work?"
2. If yes, create structure:
   ```bash
   .memory/
   ├── context.md        (from template/context.md — NEVER create empty)
   ├── index.md          (from template/index.md)
   ├── knowledge.md      (from template/knowledge.md)
   └── sessions/
   ```
3. **Seed context.md** with initial working state:
   - Current goal (from user request or conversation)
   - Current slice (if known)
   - Active files (if any)
   - Status (ACTIVE)
4. **Seed knowledge.md** with initial project info:
   - Tech stack (ask if unknown)
   - User preferences (language, style)
   - Project goals

---

## Repair Existing Memory

When `.memory/` already exists but expected files are missing:

1. **Do not recreate the entire memory directory.** Preserve existing `index.md`, `knowledge.md`, and `sessions/`.
2. **Create only missing files** from templates:
   - Missing `context.md` → create from `template/context.md`, then populate from recent sessions + project docs (`docs/TASKS.md`, `docs/AGENT_HANDOFF.md`, `docs/TECH_PLAN.md` if they exist).
   - Missing `index.md` → rebuild by scanning `sessions/*.md` files.
   - Missing `knowledge.md` → create from `template/knowledge.md`, seed from sessions if available.
   - Missing `sessions/` → create empty directory.
3. **After creating `context.md`**, populate it with:
   - Most recent session's outcome and open items
   - Current state from `docs/AGENT_HANDOFF.md` (if exists)
   - Current slice from `docs/TASKS.md` (if exists)
   - Status set to PAUSED (since we are recovering, not actively working)
4. **Record the repair** in `index.md` as a note: `<!-- Memory repair: context.md recreated on YYYY-MM-DD -->`
5. **Inform user**: "I noticed `context.md` was missing from project memory. I've created it based on recent sessions and project docs."

---

## Session Query Strategy

When user asks about past work, don't just read sequentially. Use these strategies:

### 1. Tag-Based Search
- Scan `.memory/index.md` for tags matching current topic
- Tags to use: `#auth`, `#ui`, `#refactor`, `#bug`, `#decision`, `#vibe-coding`

### 2. Temporal Search
- "What did we do last time?" → read most recent 2-3 sessions
- "What did we decide about X?" → search knowledge.md Decisions Log

### 3. Keyword Search
- Use Grep tool to search sessions for keywords
- Example: `Grep(pattern: "JWT|auth", path: ".memory/sessions")`

### 4. Relevance Ranking
If too many sessions match, rank by:
1. Exact keyword match in title/request
2. Same file paths mentioned
3. Recency (within last 7 days)
4. Tagged with current topic

---

## Memory Quality Rules

See `rules.md` for:
- File size limits and pruning
- What to store vs. skip
- Conflict handling
- Privacy (no secrets)

### Critical Additions:

**Store in vibe coding:**
- Current file being edited
- Last working state before error
- User's "try this" suggestions that worked
- Environment issues and fixes

**Skip in vibe coding:**
- Full file contents (use relative paths)
- Successful tool outputs that are reflected in file changes
- Repetitive "looks good" exchanges

---

## Templates & Examples

- `template/` — structural templates (MUST follow format)
- `examples/` — filled-in examples for reference:
  - `examples/context-example.md` — example of a populated context.md snapshot
  - `examples/session-example.md` — example of a session record
  - `examples/knowledge-example.md` — example of accumulated knowledge

**Before creating any memory file, read the corresponding template.**

---

## Effectiveness Check (self-verification)

After using memory for 3+ turns, verify:
1. Did I avoid asking redundant questions?
2. Did I reference past decisions correctly?
3. Is `.memory/context.md` present, non-empty, and up-to-date with current working state?
4. Does `context.md` stay under 100 lines?
5. Does `context.md` reference `docs/TASKS.md` / `docs/AGENT_HANDOFF.md` by path rather than duplicating their content?
6. If any answer is no — repair `context.md` immediately.
