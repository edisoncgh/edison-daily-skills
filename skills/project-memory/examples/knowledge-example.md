# Project Knowledge

## Architecture
- Monorepo managed by Turborepo (`apps/` + `packages/`)
- Backend: Express 5 + TypeScript 5.4, runs on Node 22
- Database: PostgreSQL 16 via Drizzle ORM
- Auth: Dual strategy — session (Redis) and JWT (added 2026-02-09)
- Frontend: Next.js 15 with App Router

## Conventions
- File naming: kebab-case for files, PascalCase for components
- Tests: co-located as `*.test.ts`, using Vitest
- Commits: Conventional Commits (`feat:`, `fix:`, `chore:`)
- Branches: `feature/<name>`, `fix/<name>`

## User Preferences
- Prefers functional programming style over class-based
- Wants comprehensive error handling with custom error types
- Likes code comments in Chinese (中文注释)
- Prefers responses in Chinese

## Decisions Log
- **2026-02-09**: Chose adapter pattern for dual auth — allows future auth strategies without touching middleware
- **2026-02-10**: Migrated from Jest to Vitest — 3x faster test execution, native ESM support