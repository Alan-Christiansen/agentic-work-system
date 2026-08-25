---
name: refresh-dashboards
description: Refresh every configured derived PM dashboard from canonical Area and Project homes. Use when the user asks to refresh or update dashboards. Do not perform portfolio analysis or change source records.
---
# Refresh Dashboards
Read [the shared operating policy](../../references/operating-policy.md) completely before acting.
## Authority
A refresh request authorizes writes only to generated dashboards named in the user's local PM configuration. It authorizes read-only verification of live-query dashboards. It does not authorize changes to Area or Project homes, `xPM/` state, tasks, classifications, priorities, lifecycle, or represented work.
## Configuration
Locate the user-owned Agentic PM configuration and require:
- vault or knowledge-workspace root;
- one or more source roots containing Area and Project records;
- each generated dashboard target and its defined dashboard type;
- each live-query dashboard to verify without rewriting;
- optional ordered domain-label mappings.
Do not put personal paths or domain mappings into this reusable skill. If required configuration is absent or ambiguous, ask once rather than guessing.
## Refresh
1. Resolve every configured target and source root. Stop on a missing source root, symlinked target folder, duplicate target, or existing target that is not the configured generated-dashboard type.
2. For a portfolio dashboard, run `scripts/refresh_dashboards.py` with the configured vault root, source roots, target, and domain labels. Prefer the script because it makes discovery and Markdown rendering deterministic. If Python 3 is unavailable, reproduce the contract below exactly with available file tools.
3. Inventory only underscore-prefixed Markdown homes whose remaining filename exactly matches their parent folder. Include records with `type: area` or `type: project`; ignore project tracks and other notes.
4. Include every discovered Area and Project regardless of `pm_scope`. Put a missing or unrecognized domain under `Unclassified`, and display missing overview fields visibly rather than inferring them.
5. Group by domain in configured order, then append newly discovered domains alphabetically. Within each domain, render nonempty Areas and Projects tables separately and sort rows by visible name. Omit an empty table and its heading.
6. Display linked name, `status`, `pm_scope`, `income_role`, and the home-frontmatter `next_action`. Use vault-relative wikilinks without `.md`; escape every literal table-cell pipe, including the wikilink alias separator, as `\|`. Preserve metadata wording and punctuation.
7. Keep the dashboard minimal: frontmatter, title, domain headings, and populated tables. Do not add an explanatory callout or empty-state prose.
8. Verify configured live-query dashboards without rewriting them.
## Verification
- Confirm every generated row links to an existing canonical home and exactly matches its overview metadata.
- Confirm all discovered canonical homes appear once and only once.
- Run the renderer in `--check` mode after writing; a second refresh must produce no content change.
- Confirm source records and live-query dashboards are unchanged.
- Report refreshed files, verified live dashboards, record count, and any unclassified or invalid records.
