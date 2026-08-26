# Project Contract v0.3

## Purpose

This contract defines the minimum durable state required for a human and multiple AI agents to understand, continue, and review a project without relying on shared conversation history.

It remains intentionally small. v0.3 adds an approved agent-role brief and, for repository-backed projects, an exact synchronized repository copy. Project profiles may add files or properties, but they must preserve this common core.

This contract applies only to finishable projects. Ongoing responsibilities belong under `300 - Areas` and use `area-contract.md`. A possible future project captured in an Area does not become a project until Alan approves its promotion.

## Sources of truth

| Information | Canonical home |
|---|---|
| Objective, scope, ownership, lifecycle, agent role, and cross-tool locations | Project home in Obsidian |
| Current outcome, progress, blockers, and next action | `xPM/Status.md` |
| Accepted PM-governance choices that constrain future work | `xPM/Decisions.md` |
| Restart state between people, agents, or conversations | `xPM/Handoff.md` |
| Code, tests, reusable machinery, and implementation history | Companion Git repository, when present |
| Conversations and provider memory | Supporting context only |

## Required project files

Every v0.3 project retained in `200 - Projects` has one underscore-prefixed, folder-matching human dashboard, one PM support folder, and—when required by its profile—one profile extension:

```text
Project Name/
├── _Project Name.md
├── AGENTS.md
├── CLAUDE.md
├── Product Requirements.md  # software-product only
├── Technical Brief.md       # software-tool only
├── Product Planning/        # software-product only: release UX and technical constraints
├── working files and folders...
└── xPM/
    ├── Status.md
    ├── Decisions.md
    └── Handoff.md
```

The core project-home source template is stored as `templates/project/_Project Name.md`. Substitute `Project Name` while preserving the leading underscore when copying the scaffold; never copy it as a generic `Project.md`.

The two profile documents shown above are alternatives, not universal files. Add only the extension required by `project_profile`. A software-product profile also adds only its bounded-release `Product Planning/Technology & Constraints.md`, `Product Planning/User Experience/User Experience.md`, and contextual User Experience `Assets/` folder. General and software-tool projects do not receive that folder by default.

### Folder-local bootstrap adapters
`AGENTS.md` is a thin provider-neutral cold-start adapter. It names the exact underscore-prefixed project home, routes a newly scoped agent through Status and Handoff, makes Decisions and deeper requirements conditional, and states the minimum authority boundary. It does not duplicate the project role, objective, definition of done, requirements, status, or handoff.

`CLAUDE.md` contains only `@AGENTS.md`. These vault-local adapters make the project folder independently restartable and remain distinct from repository-local agent guidance. A repository adapter carries implementation instructions and the synchronized role copy; a vault adapter only routes project context. They are operational loading files, not project state or schema fields, so Project Contract v0.3 remains current.

Do not scaffold an obvious archive or deletion candidate merely to retire it. Classify it first; apply the current structure only to projects that will remain active, planned, paused, or otherwise intentionally retained.

### Project home

The project home note is named with one leading underscore followed by the exact parent project-folder name: `Project Name/_Project Name.md`. After removing that structural underscore, the base name must equal the folder name exactly. Do not add a `Home -` prefix or use a generic filename. The underscore keeps the main human driver easy to find while `type: project` identifies the note's structural role.

The project home is the only required human-facing PM file. It combines the human dashboard with the stable definition, boundaries, ownership, and navigation point. Detailed requirements belong in the applicable project-profile document. It holds:

- directly editable project tasks;
- an approved agent-role brief;
- objective;
- definition of done;
- important boundaries;
- ownership;
- repository and external work locations.

Human working notes, research, plans, drafts, requirements, documents, deliverables, and domain-meaningful folders may live beside the project home. Do not place them in `xPM/` merely because an agent created or uses them.

Do not turn the project home into a running log. Detailed agent-maintained state belongs in `xPM/Status.md`.
Generated project and repository-guidance Markdown uses tight heading spacing: no blank line immediately before or after a heading. Intentional spacing elsewhere remains untouched, and fenced examples retain their literal formatting.

### Agent role

Every project home contains a non-empty `## Agent role` section after `## Tasks`, with `### Primary role`, `### Expertise to apply`, and `### Working approach` subsections. The role brief is explicitly approved during intake. It may define professional perspectives, subject-matter knowledge, evidence standards, and useful methods, but it never grants credentials, tool access, decision rights, or authority beyond this contract and the current task.

Agents may propose a provisional role brief from approved context, but must label it provisional and obtain approval before writing it. A project promoted from an Area receives a project-specific brief; do not copy the Area role blindly.

### Project tasks

The project home's `## Tasks` section is the canonical human-editable task surface for work that drives the project forward. A bare checkbox is valid. Direct human markers, wording, additions, deletions, dates, attention tags, and urgency tags override derived xPM state.

An empty `## Tasks` section is valid. Do not retain an empty checkbox as a capture placeholder in a Project home: task aggregators correctly treat it as a real task and surface a blank result. Add a checkbox only when it names actual work, and capture each task directly in the appropriate Area or Project home rather than a PM-dashboard Inbox.

Use the same attention vocabulary as managed Areas: mutually exclusive `#now`, `#up-next`, or untagged backlog stages plus a rare independent `#urgent` alert that may overlap any stage. `#now` means selected current focus rather than merely started work; `[/]` remains the in-progress marker. The PM recommends tag changes during read-only review or focus work and applies them only during explicitly authorized record maintenance; Alan never has to classify a task before capturing it. `📅` remains a real deadline and `⏳` remains the date work becomes actionable. Dates inform judgment without automatically assigning urgency or an attention stage.

A vault-level Tasks-plugin dashboard may aggregate tasks from underscore-prefixed, folder-matching Project and Area homes. Now, Up Next, and Backlog are non-overlapping; Urgent may intentionally overlap any of them. It is a derived interaction view, not another task store.

### Status

`xPM/Status.md` answers:

- What is true now?
- What outcome is currently active?
- What is the next concrete action?
- What is blocked?
- What comes later but is not active now?

Replace outdated status rather than accumulating a diary. Historical detail belongs in Git, completed task artifacts, daily notes, or an optional project log.

### Current-state synchronization

The project home frontmatter `status` is canonical for lifecycle. `xPM/Status.md` frontmatter `status` mirrors that approved value. `xPM/Status.md` is canonical for detailed agent-maintained outcome, progress, blockers, and next action; the project home frontmatter fields `next_action` and `blocked_by` are compact portfolio-index mirrors and must be synchronized whenever that detailed state changes. Direct human task edits in the project home remain authoritative over derived PM state.

`xPM/Handoff.md` records the recommended restart action at the moment of handoff. When a meaningful handoff is written or replaced, its recommendation must match the canonical next action. A later approved task may supersede an older handoff, but PM Status and the project-home mirrors must not conflict.

### Decisions

`xPM/Decisions.md` records accepted PM-governance choices that a future participant could otherwise reopen accidentally. Substantive product, design, or business decisions may remain with the working material they govern. A PM decision entry should include a stable ID, title, date, status, decision, and short rationale.

Use these statuses:

- `accepted`
- `superseded`
- `reversed`

Do not record brainstorms as decisions. A proposed choice remains in the task discussion or brief until Alan accepts it.

### Handoff

`xPM/Handoff.md` is a replaceable restart packet, not a permanent transcript. Keep only the latest meaningful handoff unless the project has a demonstrated need for history.

It must state:

1. task and intended outcome;
2. current state;
3. files consulted;
4. decisions made;
5. artifacts changed;
6. verification performed;
7. unresolved questions or risks;
8. recommended next action.

### Working material and contextual assets

The common project scaffold does not require a root `Assets/` folder. Human working notes, research, screenshots, canvases, exports, source documents, and other project material should live in the domain-meaningful folder that owns or uses them. Create an `Assets/` folder only where a demonstrated workflow benefits from one.

- Existing meaningful asset folders remain valid and must not be removed merely because the default changed.
- Runtime assets required by software stay in the companion repository.
- Durable reusable or library assets stay in the established asset system and are linked from the project.
- Do not duplicate an asset across locations without a specific operational reason.

## Project frontmatter

The project home uses the schema in `schemas/project.schema.json`.

For a compact setup reference with every accepted value, see `project-frontmatter-cheat-sheet.md`.

### Required properties

| Property | Meaning |
|---|---|
| `type` | Always `project` for the project home |
| `schema_version` | Contract version used to interpret the frontmatter |
| `project_id` | Stable, globally unique, lowercase kebab-case identifier |
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

`pm_scope` is independent of project lifecycle and operates inside the project's required `domain`:

| Value | Meaning |
|---|---|
| `managed` | The Agentic PM may load the project state and use it in portfolio analysis and recommendations |
| `excluded` | The Agentic PM must ignore the project unless Alan explicitly brings it into the current task |

A project without a recognized `pm_scope` is unclassified. During inventory, report it without loading deeper project content or using it in recommendations. Do not infer `managed` from folder location, activity, commercial relevance, or prior conversation history.

A normal Agentic PM session selects one domain and may use only managed projects in that domain. `pm_scope: managed` does not authorize cross-domain aggregation. Cross-domain capacity review requires Alan's explicit request and uses compact commitments rather than loading every project's detailed state.

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
| `software-product` | The project produces software for an end user or customer | A bounded-release `Product Requirements.md`, User Experience note, Technology & Constraints note, and contextual User Experience assets from `templates/project-profiles/software-product/` |
| `software-tool` | The project produces a script, library, integration, internal tool, or reusable technical capability | `Technical Brief.md` from `templates/project-profiles/software-tool/` |

A coded project must use one of the two software profiles. A software-product project is valid without a related Area when its PRD minimally defines one bounded release. When an explicitly supplied stewardship Area exists, the project may link its home and relevant product-direction notes. The relationship does not imply Area-candidate promotion, and Area-owned users and needs, product-wide feature direction, business and monetization, and incubated possibilities are linked rather than copied. Product intent and user-facing release requirements remain in the Obsidian project; implementation architecture, code, tests, and detailed technical documentation remain in the companion repository. Link the locations instead of duplicating them.

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
- `AGENTS.md` contains concise, provider-neutral repository instructions and an exact copy of the canonical project's `## Agent role` content, clearly marked as synchronized from the project home.
- `CLAUDE.md` imports `AGENTS.md` and adds only demonstrated Claude-specific differences.

The project home remains canonical. If the repository role copy differs, stop role-dependent work, report the drift, and synchronize only with authorization to edit the affected files. Do not merge conflicting wording or let repository guidance overwrite the project home.

Do not duplicate the full project status or portfolio state into the repository. The role brief is the narrow, intentional exception that makes the approved perspective available to repository-only agents. Link all other durable state to the project home.

## Context-loading contract

Start with the smallest useful context stack:

1. global working preferences;
2. relevant domain context;
3. project-local `AGENTS.md`, when present;
4. project home;
5. `xPM/Status.md` and the latest `xPM/Handoff.md`;
6. `xPM/Decisions.md` when the task could affect or reopen a prior PM-governance choice;
7. the current task brief or source material;
8. repository-local instructions when implementation is involved.

Load deeper research, logs, and historical artifacts only when the task requires them.

## Authority boundaries

### Routine work within an approved task

An agent may:

- read relevant project and repository files;
- create or edit artifacts inside the approved task scope;
- run proportionate tests and inspections;
- update factual progress in `xPM/Status.md`;
- replace `xPM/Handoff.md` after meaningful work;
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

## v0.3 acceptance test

The contract passes when:

1. one general project and one software project can be manually represented without unnecessary files;
2. a domain-scoped Agentic PM session includes only projects marked `pm_scope: managed` inside the selected domain;
3. excluded and unclassified projects do not influence recommendations;
4. a software project points to the correct requirements profile and companion repository without duplicating implementation state;
5. working material and contextual assets have an unambiguous domain-meaningful home without requiring unused root folders;
6. the portfolio inventory can classify archive and deletion candidates without scaffolding them first;
7. the manual workflow reveals no missing field that would block prioritization.
8. a managed project in another domain remains unloaded unless Alan explicitly requests cross-domain capacity review.
9. every project has a complete approved role brief that does not expand agent authority.
10. every repository-backed project has an exact derived role copy in `AGENTS.md`, and validation detects drift from the canonical project home.

Run this test during the first read-only portfolio inventory and migration pilot before building a scaffolding skill.
