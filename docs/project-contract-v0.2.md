# Project Contract v0.2

## Purpose

This contract defines the minimum durable state required for a human and multiple AI agents to understand, continue, and review a project without relying on shared conversation history.

It remains intentionally small. v0.2 adds only the information and folders demonstrated as necessary for portfolio management and repeatable project setup. Project profiles may add files or properties, but they must preserve this common core.

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

Every v0.2 project retained in `200 - Projects` has one folder containing four required core notes, one project-local assets folder, and—when required by its profile—one profile document:

```text
Project Name/
├── Project Name.md
├── Status.md
├── Decisions.md
├── Handoff.md
├── Product Requirements.md  # software-product only
├── Technical Brief.md       # software-tool only
└── Assets/
```

The core project-home source template is stored as `templates/project/Project Name.md`. Preserve or substitute that filename when copying the scaffold; never copy it as a generic `Project.md`.

The two profile documents shown above are alternatives, not universal files. Add only the document required by `project_profile`.

Do not scaffold an obvious archive or deletion candidate merely to retire it. Classify it first; apply the current structure only to projects that will remain active, planned, paused, or otherwise intentionally retained.

### Project home

The project home note has the same base name as its parent project folder: `Project Name/Project Name.md`. Keep that relationship rather than adding a `Home -` prefix or using a generic filename. The project name provides a unique, natural Obsidian link, while `type: project` identifies the note's structural role.

The project home is the stable definition, boundaries, ownership, and navigation point for the project. Detailed requirements belong in the applicable project-profile document. It holds stable information:

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

### Current-state synchronization

The project home frontmatter `status` is canonical for lifecycle. `Status.md` frontmatter `status` mirrors that approved value. `Status.md` is canonical for detailed current outcome, progress, blockers, and next action; the project home frontmatter fields `next_action` and `blocked_by` are compact portfolio-index mirrors and must be synchronized whenever that detailed state changes. Synchronizing an already-approved lifecycle value is factual mirroring, not authority to choose or change the lifecycle.

`Handoff.md` records the recommended restart action at the moment of handoff. When a meaningful handoff is written or replaced, its recommendation must match the canonical next action. A later approved task may supersede an older handoff, but Status and the project-home mirrors must not conflict.

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

### Assets

`Assets/` holds project-local working material such as selected references, exports, source documents, and deliverables that belong with the project but not in its Git repository.

- Runtime assets required by software stay in the companion repository.
- Durable reusable or library assets stay in the established asset system and are linked from the project.
- Do not duplicate an asset across locations without a specific operational reason.
- The folder may remain empty until the project needs it.

## Project frontmatter

The project home uses the schema in `schemas/project.schema.json`.

For a compact setup reference with every accepted value, see `project-frontmatter-cheat-sheet.md`.

### Required properties

| Property | Meaning |
|---|---|
| `type` | Always `project` for the project home |
| `schema_version` | Contract version used to interpret the frontmatter |
| `project_id` | Stable, unique, lowercase kebab-case identifier |
| `status` | Project lifecycle state |
| `domain` | Stable domain identifier aligned with the vault domain |
| `pm_scope` | Whether the Agentic PM may use the project in portfolio analysis |
| `project_profile` | The requirements profile applied to the project |
| `created` | Creation date in `YYYY-MM-DD` form |
| `updated` | Last material project-state update |
| `next_action` | One concrete action that can move the project |
| `blocked_by` | Project IDs or external blockers; use `[]` when clear |

### Conditional property

| Property | Requirement |
|---|---|
| `income_role` | Required when `pm_scope` is `managed`; may be omitted when excluded |

### Optional properties

| Property | Meaning |
|---|---|
| `priority` | Human- or PM-assigned relative priority from `1` (highest) through `5` (lowest) |
| `goals` | Goal IDs advanced by the project |
| `deadline` | Real external or chosen deadline |
| `repo` | Local path to a companion repository |
| `repo_remote` | Remote repository URL |
| `owner` | Responsible person when ownership is not obvious |

Quote `created`, `updated`, and `deadline` values as `"YYYY-MM-DD"` strings in YAML so JSON Schema validators receive strings rather than YAML date objects. For date-only metadata describing current work, use the calendar date in `America/New_York`; do not substitute the UTC calendar date when it differs locally.

Source templates may contain placeholders such as `"YYYY-MM-DD"` and are not valid project instances until instantiated. Validation tooling must substitute concrete values or exclude source templates from instance-validation runs.

Do not add properties merely because they might be useful someday. Extend the schema only after a real project needs the information.

## Agentic PM scope

`pm_scope` is independent of project lifecycle:

| Value | Meaning |
|---|---|
| `managed` | The Agentic PM may load the project state and use it in portfolio analysis and recommendations |
| `excluded` | The Agentic PM must ignore the project unless Alan explicitly brings it into the current task |

A project without a recognized `pm_scope` is unclassified. During inventory, report it without loading deeper project content or using it in recommendations. Do not infer `managed` from folder location, activity, commercial relevance, or prior conversation history.

Managed projects must set `income_role` to `direct`, `enabling`, `none`, or `unknown`. It helps the PM distinguish direct revenue work from enabling infrastructure and noncommercial work, but never determines priority by itself.

Only Alan or an explicitly authorized PM workflow may change `pm_scope`, `income_role`, `project_profile`, or `priority`.

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

## Project profiles

The required `project_profile` selects the smallest useful requirements extension:

| Profile | Use when | Added requirement |
|---|---|---|
| `general` | The project does not produce software | No additional required note |
| `software-product` | The project produces software for an end user or customer | `Product Requirements.md` from `templates/project-profiles/software-product/` |
| `software-tool` | The project produces a script, library, integration, internal tool, or reusable technical capability | `Technical Brief.md` from `templates/project-profiles/software-tool/` |

A coded project must use one of the two software profiles. Product intent and user-facing requirements remain in the Obsidian project home; implementation architecture, code, tests, and detailed technical documentation remain in the companion repository. Link the two locations instead of duplicating them.

Profiles may be extended only after a real project demonstrates a repeated need. Do not add empty profile documents to projects that do not use them.

## Internal capability tracks

A note with `type: project-track` describes a bounded capability or workstream inside one parent project. It is not a project home, does not use the project schema, carries `track_id` rather than `project_id`, and must not define portfolio `priority`, `pm_scope`, or `income_role`. Portfolio inventory ignores project-track notes.

A track may record its own status, dependencies, and next action without changing the parent project's canonical state. Describe a track as a capability track, not as a separate project.

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
3. project-local `AGENTS.md`, when present;
4. project home;
5. `Status.md` and the latest `Handoff.md`;
6. `Decisions.md` when the task could affect or reopen a prior choice;
7. the current task brief or source material;
8. repository-local instructions when implementation is involved.

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
- project status, priority, goals, deadline, `pm_scope`, `income_role`, or `project_profile`;
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

## v0.2 acceptance test

The contract passes when:

1. one general project and one software project can be manually represented without unnecessary files;
2. the Agentic PM includes only projects marked `pm_scope: managed`;
3. excluded and unclassified projects do not influence recommendations;
4. a software project points to the correct requirements profile and companion repository without duplicating implementation state;
5. project-local assets have an unambiguous home;
6. the portfolio inventory can classify archive and deletion candidates without scaffolding them first;
7. the manual workflow reveals no missing field that would block prioritization.

Run this test during the first read-only portfolio inventory and migration pilot before building a scaffolding skill.
