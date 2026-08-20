# Project Frontmatter Cheat Sheet

Use this when creating or updating an Agentic Work System v0.2 project home. The machine-readable source is `schemas/project.schema.json`; the full human-readable rules are in `docs/project-contract-v0.2.md`.

## Copyable starting point

```yaml
---
type: project
schema_version: "0.2"
project_id: project-name
status: planned
domain: domain-id
pm_scope: excluded
income_role: unknown
project_profile: general
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
next_action: Define the first concrete action
blocked_by: []
---
```

Uncomment `income_role` when `pm_scope` is `managed`. Replace every placeholder before treating the file as a project instance.

## Required fields

| Field             | Accepted value                                    | Meaning                                                                   |     |
| ----------------- | ------------------------------------------------- | ------------------------------------------------------------------------- | --- |
| `type`            | `project`                                         | Fixed value identifying a project home.                                   |     |
| `schema_version`  | `"0.2"`                                           | Fixed contract version. Keep it quoted.                                   |     |
| `project_id`      | Lowercase kebab-case, such as `website-refresh`   | Stable unique identifier. Do not change it when the display name changes. |     |
| `status`          | See lifecycle values below                        | Current project lifecycle.                                                |     |
| `domain`          | Lowercase kebab-case, such as `tech-and-systems`  | Stable vault-aligned domain identifier.                                   |     |
| `pm_scope`        | `managed` or `excluded`                           | Whether the Agentic PM may use the project in portfolio analysis.         |     |
| `project_profile` | `general`, `software-product`, or `software-tool` | Selects the proportional requirements structure.                          |     |
| `created`         | `"YYYY-MM-DD"`                                    | Original creation date in `America/New_York`. Keep it quoted.             |     |
| `updated`         | `"YYYY-MM-DD"`                                    | Last material project-state update. Keep it quoted.                       |     |
| `next_action`     | Non-empty text                                    | One concrete action that can move the project.                            |     |
| `blocked_by`      | YAML list, such as `[]` or `[project-id]`         | Project IDs or external blockers. Use `[]` when clear.                    |     |

## Conditional field

`income_role` is required when `pm_scope: managed`. Omit it when the project is excluded.

| Value | Use when |
| --- | --- |
| `direct` | The project itself is expected to generate income. |
| `enabling` | The project supports work that generates income. |
| `none` | The project has no intended income role. |
| `unknown` | The income relationship has not been determined. |

`income_role` informs portfolio judgment but never determines priority by itself.

## Lifecycle values

| `status` | Use when |
| --- | --- |
| `planned` | Defined but not receiving active effort. |
| `active` | Receiving current effort. |
| `blocked` | Cannot advance until a named blocker changes. |
| `paused` | Intentionally inactive despite being actionable. |
| `complete` | The definition of done has been met. |
| `cancelled` | Intentionally ended without meeting the definition of done. |
| `archived` | Retained for history after completion or cancellation. |

## Project profile values

| `project_profile` | Use when | Additional file |
| --- | --- | --- |
| `general` | The project does not produce software. | None |
| `software-product` | The project produces software for an end user or customer. | `Product Requirements.md` |
| `software-tool` | The project produces a script, library, integration, or internal technical capability. | `Technical Brief.md` |

A coded project must use `software-product` or `software-tool`.

## Optional fields

| Field | Accepted value |
| --- | --- |
| `priority` | Integer `1` through `5`, where `1` is highest. |
| `goals` | YAML list of goal IDs. |
| `deadline` | Real deadline as quoted `"YYYY-MM-DD"`. |
| `repo` | Non-empty local companion-repository path. |
| `repo_remote` | Full repository URL. |
| `owner` | Responsible person when ownership is not obvious. |

Do not add optional fields merely because they exist. Add them only when the project needs them.

## Authority reminders

Only Alan or an explicitly authorized PM workflow changes project lifecycle, priority, goals, deadline, `pm_scope`, `income_role`, or `project_profile`.

Keep these synchronized:

- Project-home `status` and `Status.md` status
- Project-home `next_action`, the detailed Status next action, and the latest Handoff recommendation
- Project-home `blocked_by` and the detailed Status blockers
