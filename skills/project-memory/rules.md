# Memory Management Rules

## File Size Limits
- Each `sessions/*.md` file: **≤ 150 lines**
- `knowledge.md`: **≤ 300 lines**
- `context.md`: **≤ 100 lines** (keep it a working snapshot, not a dump)
- `index.md`: no hard limit, but keep entries to one line each

## Pruning (when session count > 20)
1. Read the 5 oldest session files
2. Extract any lasting knowledge → append to `knowledge.md`
3. Delete those 5 session files
4. Remove their entries from `index.md`
5. Add a note in `index.md`: `<!-- Archived sessions before YYYY-MM-DD into knowledge.md -->`

## Merging
- If two sessions cover the same topic on the same day, merge into one file
- Keep the later timestamp as the filename

## What to Store vs. Skip

### STORE
- User requirements and constraints
- Files read or modified, and why
- Technical decisions with rationale
- Unresolved items and next steps
- User preferences discovered during conversation
- User's "try this" suggestions that worked
- Environment issues and fixes (OS quirks, dependency conflicts)
- Error patterns and their resolutions

### SKIP
- Verbatim code (just reference file paths)
- Trivial exchanges ("hello", "thanks")
- Intermediate tool output that is already reflected in the outcome
- Successful tool outputs already reflected in file changes
- Repetitive "looks good" exchanges
- Full file diffs (reference the commit or file path instead)

## Vibe Coding Specific Rules

### Context Refresh Cadence
- Update `context.md` every 3-5 turns during active development
- Always update `context.md` when switching to a different file or feature
- On user "break"/"pause"/"later": write a detailed context snapshot immediately

### Context.md Must Contain
- **Active files**: list of files currently being edited (with line ranges if focused)
- **Last working state**: key functions/classes/interfaces in flux (names + brief description, not full code)
- **Pending decisions**: open questions the user hasn't resolved yet
- **Next steps**: what was about to happen next
- **Blockers**: anything preventing progress (compilation errors, failing tests, missing info)

### Error Tracking During Vibe Coding
When errors occur during iterative development:
- Record: error message, file:line, what was attempted, what fixed it
- If fix was user-suggested, note that explicitly (builds preference profile)
- If fix involved a workaround, note the proper solution for future reference

## Boundary Conditions

### When NOT to Create a Session File
- Conversation is purely exploratory (no code changes, no decisions)
- User is just asking a question (unless it reveals a new preference)
- Only reading files with no action taken

### When to Update knowledge.md
- A new convention or pattern is established
- A significant architectural decision is made
- User expresses a preference not previously recorded
- A toolchain or dependency version changes
- A recurring workaround is adopted as standard practice

### When to Skip Memory Entirely
- Single-turn trivial tasks ("what does this function do?")
- Tasks fully captured by git history (no additional context needed)
- Conversations where user explicitly says "don't record this"

## File Responsibilities and Boundaries

| File | Role | Lifetime | Size Cap |
|------|------|----------|----------|
| `.memory/context.md` | Current working snapshot | Volatile — rewrite on each update | ≤ 100 lines |
| `.memory/knowledge.md` | Long-term durable project knowledge | Persistent — append only | ≤ 300 lines |
| `.memory/index.md` | Session index with tags | Persistent — append only | No hard limit |
| `.memory/sessions/` | Chronological session records | Persistent — pruned after 20 | ≤ 150 lines each |
| `docs/TASKS.md` | Task tree / milestone / acceptance criteria | Managed by handoff-driven-development | N/A |
| `docs/AGENT_HANDOFF.md` | Agent handoff source of truth | Managed by handoff-driven-development | N/A |
| `docs/TECH_PLAN.md` | Architecture and module boundaries | Managed by handoff-driven-development | N/A |

### Key Boundaries

- `context.md` is a **snapshot**, not a log. Rewrite it each time — do not append.
- `context.md` must **not** duplicate content from `docs/TASKS.md` or `docs/AGENT_HANDOFF.md`. Reference them by path only.
- If the project uses handoff-driven-development docs, `context.md` summarizes the current slice; `TASKS.md` owns the full task tree; `AGENT_HANDOFF.md` owns the handoff details.
- `knowledge.md` stores facts that survive across sessions. `context.md` stores state that changes within a session.

## Conflict Handling
- If `.memory/index.md` is missing but `sessions/` exists, rebuild the index by scanning session files
- If `.memory/context.md` is missing but other memory files exist, create it from template and populate from recent sessions + project docs
- If a session filename already exists (same second), append `-2` before `.md`
- If `context.md` and actual code state diverge, trust the code and update `context.md`
- If `context.md` and `docs/TASKS.md` or `docs/AGENT_HANDOFF.md` contradict, trust the docs and update `context.md`
- If two sessions contradict each other, trust the later session and flag the conflict in `knowledge.md`

## Privacy
- Never store API keys, passwords, or secrets in memory files
- If user shares sensitive info, reference it as "credentials provided" without values
- Do not store full URLs that contain tokens or session IDs
