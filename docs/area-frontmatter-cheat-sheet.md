# Area Frontmatter Cheat Sheet

Use this when creating or updating an Agentic Work System v0.1 Area home. The schema is `schemas/area.schema.json`; the full rules are in `docs/area-contract.md`.

## Copyable starting point

```yaml
---
type: area
schema_version: "0.1"
area_id: area-name
status: active
domain: domain-id
pm_scope: excluded
# income_role: unknown
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
next_action: Define the first maintenance action
blocked_by: []
---
```

Uncomment `income_role` when `pm_scope: managed`. Replace every placeholder before treating the file as an Area instance.

## Accepted values

| Field | Accepted value |
| --- | --- |
| `type` | `area` |
| `schema_version` | `"0.1"` |
| `area_id` | Globally unique lowercase kebab-case, normally domain-prefixed, such as `spectra-studio-business-admin` |
| `status` | `active`, `paused`, or `retired` |
| `domain` | Lowercase kebab-case |
| `pm_scope` | `managed` or `excluded` |
| `income_role` | `direct`, `enabling`, `none`, or `unknown`; required when managed |
| `created` | Quoted `"YYYY-MM-DD"` in `America/New_York` |
| `updated` | Quoted `"YYYY-MM-DD"` in `America/New_York` |
| `next_action` | One non-empty concrete action |
| `blocked_by` | YAML list or `[]` |

`active` means the responsibility still exists. It does not mean the Area is the current primary focus.

`pm_scope: managed` applies only inside the Area's required `domain`. A normal PM session selects one domain and does not load managed records from other domains.

Time available and current energy belong to the active PM conversation or task brief, not Area frontmatter.

Only Alan or an explicitly authorized PM workflow changes Area lifecycle, `pm_scope`, or `income_role`.
