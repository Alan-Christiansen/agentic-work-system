# Agentic PM Plugin

Provider-neutral project, Area, and portfolio-management skills built on the Agentic Work System contracts.

## Included skills

- `agentic-pm:portfolio-review`: compare managed commitments inside one domain and recommend focus.
- `agentic-pm:plan-week`: choose a realistic primary weekly outcome and, when justified, one secondary maintenance outcome.
- `agentic-pm:choose-next-action`: select one concrete action that fits the available time and attention.
- `agentic-pm:stuck-rescue`: diagnose the active constraint and reduce it to one finishable move.
- `agentic-pm:review-area`: review one ongoing responsibility without turning it into a finishable project.
- `agentic-pm:review-project-candidate`: shape or compare an inactive Area proposal without silently promoting it.

All skills use the shared policy in `references/operating-policy.md`. Personal goals, constraints, priorities, business context, and live work state remain in the user's own knowledge workspace.

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
