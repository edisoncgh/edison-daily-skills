# Project Historical Knowledge

## Historical Decisions & Rationale
- **2026-02-09 — Auth strategy boundary introduced.** Session and JWT auth were decoupled to avoid conditional logic spreading through middleware. See `episodes/20260209-1430-auth-strategy-adapter.md`.
- **2026-02-10 — Test runner changed from Jest to Vitest.** The migration improved ESM compatibility and reduced test latency. See the corresponding migration episode.

## Architecture / Product Transitions
- Authentication evolved from Redis-session-only to a multi-strategy boundary. The current auth architecture must be read from `docs/TECH_PLAN.md`, not inferred from this history.

## Lessons Learned
- Cross-cutting auth behavior is safer behind an adapter boundary than inside request middleware.

## Pitfalls & Failure Patterns
- Do not restore old session-only assumptions when touching shared auth middleware.

## Environment / Toolchain Quirks
- None recorded.

## Project-Specific Preference History
- The project has historically favored small explicit interfaces over condition-heavy shared modules. If this is still an active rule, confirm it in the project rule/docs layer.
