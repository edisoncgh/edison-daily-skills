# Episode: Authentication moved behind a strategy adapter

- Date: 2026-02-09
- Scope: Auth subsystem
- Tags: #auth #decision #refactor
- Related files: `src/auth/handler.ts`, `src/auth/jwt-adapter.ts`, `src/middleware/auth.ts`
- Related commit(s): `a1b2c3d`

## Trigger / Context
The existing request middleware was tightly coupled to Redis-backed sessions while the project needed JWT support without breaking session users.

## Attempts / Options
- Adding JWT conditionals directly in middleware was considered but would have increased coupling.
- A strategy/adapter boundary was chosen so authentication mechanisms could vary behind one interface.

## Decision / Change
The auth flow was refactored around an `AuthStrategy` abstraction and a JWT adapter. This kept strategy selection out of downstream request handling and made future auth mechanisms less invasive.

## Outcome & Evidence
- Existing session behavior remained intact.
- 12 pre-existing auth tests and 5 JWT tests passed at the time.
- JWT configuration was moved to `JWT_SECRET` rather than hard-coded values.

## Lessons / Pitfalls
- Avoid strategy-specific branching in shared middleware; keep it behind the auth boundary.
- Secret values belong in environment configuration and must never be copied into memory.

## Unresolved at the Time
- Token refresh had not yet been implemented. Its present status must be checked in current `TASKS.md` / `AGENT_HANDOFF.md`.

## Related Memory
- Distilled rationale: `../knowledge.md#historical-decisions--rationale`
