# Agentic PM Plugin

Provider-neutral project, Area, and portfolio-management skills built on the Agentic Work System contracts.

## Included skills
- `agentic-pm:review`: review managed work at the appropriate portfolio, domain, Area, Project, or inactive-candidate scope and recommend what deserves attention.
- `agentic-pm:focus`: turn an accepted direction into a realistic weekly plan or one finishable session move, diagnosing stuckness when needed.
- `agentic-pm:refresh-dashboards`: refresh every configured generated PM dashboard and verify live-query dashboards without changing canonical records.
All skills use the shared policy in `references/operating-policy.md`. `review` and `focus` route internally by target, horizon, and working state so the user does not need to select fine-grained management modes. Personal goals, constraints, priorities, business context, and live work state remain in the user's own knowledge workspace.

## Codex

This repository's marketplace is named `spectra-studio`. Install the marketplace and plugin with:

```sh
codex plugin marketplace add "<path-to-agentic-work-system>"
codex plugin add agentic-pm@spectra-studio
```

Start a new task after installation so Codex discovers the skills.

## Claude and Cowork

Upload `dist/agentic-pm.plugin` independently from `agentic-work`. Its source contains no required personal data or installation-specific vault path.

## Placeholder branding

The Codex plugin currently uses `assets/spectra-studio-placeholder.png` for both its marketplace logo and composer icon. Replace that file in place when the final Spectra Studio icon is ready; the manifest paths can remain unchanged.
