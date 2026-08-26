# Migration from Handoff-Driven Development v2

The current skill uses a stricter split between **historical continuity** and the
**operational control plane**, and exposes a clean interface to the optional `project-continue`
orchestrator.

## Semantic Changes

1. Stop reading or writing `.memory/context.md` as current state. Legacy memory is
   historical migration input only.
2. `PROJECT_BRIEF.md` owns durable direction/boundaries.
3. `TASKS.md` owns active milestone/slice/blocker/next work.
4. `TECH_PLAN.md` owns the current technical contract, not architecture history.
5. `QUALITY.md` (when used) owns concise verification evidence.
6. `AGENT_HANDOFF.md` is the current baton and is written last during synchronization.
7. Handoff-Driven Development no longer orchestrates Memory or Neat-freak itself.
   `project-continue` owns multi-skill closeout/resume orchestration when installed.
8. The stable skill name is `handoff-driven-development`; version numbers belong to
   package release notes, not invocation names.
9. Rules files point to operational docs but do not duplicate current status.

## Migration Checklist

- [ ] Stop refreshing `.memory/context.md`.
- [ ] Move current goal/slice/blocker/next action into `TASKS.md` / `AGENT_HANDOFF.md`.
- [ ] Keep current architecture/contracts in `TECH_PLAN.md`.
- [ ] Keep only durable north-star statements in `PROJECT_BRIEF.md`.
- [ ] Separate implemented versus verified status.
- [ ] Remove old Project Continue workflow prompts from the Handoff skill.
- [ ] Update saved references to the stable name `handoff-driven-development`.
- [ ] If using Project Continuity Suite, invoke `project-continue closeout` / `project-continue resume`
      instead of manually chaining the three skills.

Do not silently delete unique historical material during migration. Distill it into
Project Memory episodes/knowledge first when appropriate.
