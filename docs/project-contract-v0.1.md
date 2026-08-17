# Project Contract v0.1

## Purpose

This contract defines the minimum durable state required for a human and multiple AI agents to understand, continue, and review a project without relying on shared conversation history.

It is intentionally small. Project types may add files or properties, but they must preserve this common core.

## Sources of truth

| Information | Canonical home |
|---|---|
| Objective, scope, ownership, lifecycle, and cross-tool locations | Project home in Obsidian |
| Current outcome, progress, blockers, and next action | `Status.md` |
| Accepted choices that constrain future work | `Decisions.md` |
| Restart state between people, agents, or conversations | `Handoff.md` |
| Code, tests, reusable machinery, and implementation history | Companion Git repository, when present |
| Conversations and provider memory | Supporting context only |

## Required project files

Every active project has one folder containing four required files:

```text
Project Name/
├── Project Name.md
├── Status.md
├── Decisions.md
└── Handoff.md
```

### Project home

The root note holds stable information:

- objective;
- definition of done;
- important boundaries;
- ownership;
- links to project state;
- repository and external work locations.

Do not turn it into a running log. Frequently changing information belongs in `Status.md`.

### Status

`Status.md` answers:

- What is true now?
- What outcome is currently active?
- What is the next concrete action?
- What is blocked?
- What comes later but is not active now?

Replace outdated status rather than accumulating a diary. Historical detail belongs in Git, completed task artifacts, daily notes, or an optional project log.

### Decisions

`Decisions.md` records accepted choices that a future participant could otherwise reopen accidentally. A decision entry should include a stable ID, title, date, status, decision, and short rationale.

Use these statuses:

- `accepted`
- `superseded`
- `reversed`

Do not record brainstorms as decisions. A proposed choice remains in the task discussion or brief until Alan accepts it.

### Handoff

`Handoff.md` is a replaceable restart packet, not a permanent transcript. Keep only the latest meaningful handoff unless the project has a demonstrated need for history.

It must state:

1. task and intended outcome;
2. current state;
3. files consulted;
4. decisions made;
5. artifacts changed;
6. verification performed;
7. unresolved questions or risks;
8. recommended next action.

## Project frontmatter

The project home uses the schema in `schemas/project.schema.json`.

### Required properties

| Property | Meaning |
|---|---|
| `type` | Always `project` for the project home |
| `schema_version` | Contract version used to interpret the frontmatter |
| `project_id` | Stable, unique, lowercase kebab-case identifier |
| `status` | Project lifecycle state |
| `domain` | Stable domain identifier aligned with the vault domain |
| `created` | Creation date in `YYYY-MM-DD` form |
| `updated` | Last material project-state update |
| `next_action` | One concrete action that can move the project |
| `blocked_by` | Project IDs or external blockers; use `[]` when clear |

### Optional properties

| Property | Meaning |
|---|---|
| `priority` | Human- or PM-assigned relative priority; `1` is highest |
| `goals` | Goal IDs advanced by the project |
| `deadline` | Real external or chosen deadline |
| `repo` | Local path to a companion repository |
| `repo_remote` | Remote repository URL |
| `owner` | Responsible person when ownership is not obvious |

Do not add properties merely because they might be useful someday. Extend the schema only after a real project needs the information.

## Lifecycle states

| Status | Meaning |
|---|---|
| `planned` | Defined but not currently receiving active effort |
| `active` | Receiving current effort |
| `blocked` | Cannot advance until a named blocker changes |
| `paused` | Intentionally inactive despite being otherwise actionable |
| `complete` | Definition of done has been met |
| `cancelled` | Intentionally ended without meeting the definition of done |
| `archived` | Retained for history after completion or cancellation |

Only Alan or an explicitly authorized PM workflow changes project lifecycle, priority, goals, deadline, or definition of done.

## Companion repository contract

A repository is optional. Create one when the project produces code, reusable machinery, or technical artifacts that benefit from independent version history.

The minimum repository guidance is:

```text
repository/
├── README.md
├── AGENTS.md
└── CLAUDE.md
```

- `README.md` explains the repository purpose and points to the Obsidian project home.
- `AGENTS.md` contains concise, provider-neutral repository instructions.
- `CLAUDE.md` imports `AGENTS.md` and adds only demonstrated Claude-specific differences.

Do not duplicate the full project status or portfolio state into the repository. Link to the project home.

## Context-loading contract

Start with the smallest useful context stack:

1. global working preferences;
2. relevant domain context;
3. project home;
4. `Status.md` and the latest `Handoff.md`;
5. `Decisions.md` when the task could affect or reopen a prior choice;
6. the current task brief or source material;
7. repository-local instructions when implementation is involved.

Load deeper research, logs, and historical artifacts only when the task requires them.

## Authority boundaries

### Routine work within an approved task

An agent may:

- read relevant project and repository files;
- create or edit artifacts inside the approved task scope;
- run proportionate tests and inspections;
- update factual progress in `Status.md`;
- replace `Handoff.md` after meaningful work;
- report discovered risks and proposed decisions.

### Changes that require Alan's approval

An agent must propose before changing:

- objective, definition of done, or major scope;
- project status, priority, goals, or deadline;
- accepted decisions;
- project or repository structure beyond the current contract;
- production dependencies or foundational technologies;
- the canonical location of project data;
- another project or Area.

### Explicit authorization required

An agent must never infer permission to:

- delete or irreversibly overwrite material;
- publish, deploy, purchase, or send externally;
- expose private or unrelated context;
- create accounts, remotes, or external integrations;
- weaken security or approval boundaries.

## Completion checklist

Before handing off meaningful work:

- verify changed artifacts in proportion to risk;
- update factual project status;
- record only decisions Alan has accepted;
- replace the handoff with a concise restart packet;
- ensure the next action is concrete;
- leave unrelated files untouched.

## v0.1 acceptance test

The contract passes when:

1. Agent A receives a bounded task and records a handoff.
2. Agent B starts without Agent A's conversation and continues correctly from the files.
3. Agent C reviews the result using the same project state and repository evidence.
4. Alan does not need to reconstruct material context verbally.
5. The test identifies any context that was missing or unnecessarily loaded.

Run this test on one real Spectra Studio project before expanding the protocol.
