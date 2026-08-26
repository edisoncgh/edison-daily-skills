# Project Continue Portability and Host Adapters

This reference is installation/invocation convenience only. Project Continue's core behavior
must remain independent of every path and syntax listed here.

## Canonical cross-host invocation

Use ordinary text everywhere:

```text
project-continue closeout
project-continue resume
project-continue checkpoint
project-continue status
```

If the host offers a native skill selector, tag, or slash command, it may be used as
a shortcut. Do not encode that shortcut into Project Continue's core workflow.

## Canonical skill format

All four suite components follow the Agent Skills directory model:

```text
skill-name/
└── SKILL.md
```

The suite-owned skills intentionally rely only on the required `name` and
`description` frontmatter fields plus Markdown instructions. This is the lowest
common denominator of the Agent Skills specification.

## Shared source strategy

Prefer **one canonical copy** of each skill plus symlinks/imports where the host
supports them. Avoid maintaining manually edited vendor forks.

A good shared location on hosts that support the open standard directly is:

```text
~/.agents/skills/
```

or the repository equivalent:

```text
<repo>/.agents/skills/
```

When a host does not scan that location, expose the same folders through its native
skill location or import mechanism.

## Host notes

These are adapters, not protocol requirements. Re-check host documentation when a
product changes.

### OpenAI Codex

Codex supports explicit skill selection with `$` and `/skills`, and scans
`$HOME/.agents/skills` plus repository `.agents/skills` locations. Symlinked skill
folders are supported.

Recommended shared setup: put the canonical suite under `~/.agents/skills/` or the
repo's `.agents/skills/` and invoke with ordinary `project-continue closeout` or the native
skill selector.

### OpenCode

OpenCode scans both `~/.agents/skills/` and project `.agents/skills/` in addition to
its native skill directories. Its agents load skills through the native skill tool.

Recommended shared setup: use the same `.agents/skills` canonical copy as Codex.
A custom `/project-continue` command is optional sugar and is not required.

### Kimi Code CLI

Kimi Code scans `~/.agents/skills/` and project `.agents/skills/` in addition to
Kimi-specific directories. Native `/skill:<name>` invocation and automatic
selection are available.

Recommended shared setup: use the same `.agents/skills` canonical copy. Prefer the
host-neutral text `project-continue closeout` when you want identical muscle memory everywhere.

### Qoder

Qoder uses `~/.qoder/skills/` for user skills and `.qoder/skills/` for project
skills, with manual `/skill-name` and automatic invocation.

Expose/copy the same suite folders into Qoder's native location. Do not rewrite the
SKILL.md files for Qoder.

### ZCode

ZCode uses `~/.zcode/skills/` for user skills. It can import skills from external
coding agents and supports Symlink or Copy import modes; imported skills are invoked
with `$skill-name` or through the slash menu.

Prefer Symlink/import from a canonical copy when available so ZCode does not become
an independently edited fork.

### Unknown / future Agent Skills host

1. Check whether it supports the Agent Skills `SKILL.md` format.
2. Install the four folders in its documented skill discovery location.
3. Verify the four names appear: `project-continue`, `project-memory`,
   `handoff-driven-development`, `neat-freak`.
4. Start with plain `project-continue status`, then test `project-continue resume` or `project-continue closeout` in a
   disposable project.
5. If it does not support nested skill activation, ensure the active agent can still
   load the named companion skill files in one session.

## Host without Agent Skills support

Use the SKILL.md files as project instructions or paste/load them on demand. Project Continue
still works conceptually because it relies on semantic workflow composition, not on
a specific command parser. In this mode, explicitly provide all four skills to the
agent and use `project-continue closeout` / `project-continue resume` as ordinary text.
