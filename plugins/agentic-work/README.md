# Agentic Work Plugin

Reusable Claude, Cowork, ChatGPT, and Codex skills for Areas and projects that follow the Agentic Work System protocol.

## Included skills

- `/agentic-work:start-area`: create or initialize an ongoing Area without turning it into a finishable project or activating its project candidates.
- `/agentic-work:start-project`: directly initialize a project or promote an approved Area candidate, applying profile-specific records and a required local repository for software projects.
- `/agentic-work:record-checkpoint`: verify a reviewed human-created commit, synchronize the Obsidian project checkpoint, and stop.

## Install in Claude Cowork

1. Open **Customize → Plugins**.
2. Choose the option to add or upload a plugin from a file.
3. Select `dist/agentic-work.plugin` from this repository.
4. Confirm that the `start-area`, `start-project`, and `record-checkpoint` skills are enabled.
5. Open a new task with access to the intended project or Area location and, when applicable, the approved companion-repository parent or existing repository.
6. Run `/agentic-work:start-area`, `/agentic-work:start-project`, or `/agentic-work:record-checkpoint`.

`start-area` requires a reviewed preflight before writing. It creates an Area Contract v0.1 record for ongoing responsibility, keeps Area tasks separate from inactive project candidates, and does not convert or delete an existing project, promote candidates, or perform the represented next action.

`start-project` requires a reviewed preflight before writing. For `software-product` and `software-tool`, it creates an approved local stub repository or links an existing local repository. It does not add a remote, dependency, commit, publication, deployment, or installation change, and it does not begin the represented next action.

`record-checkpoint` does not create a commit, push, deploy, or begin the next task.

## Install in Codex

The repository includes a local Codex marketplace at `.agents/plugins/marketplace.json`. From any folder, run:

```sh
codex plugin marketplace add "<path-to-agentic-work-system>"
codex plugin add agentic-work@spectra-studio
```

Start a new Codex task after installation so the skill is discovered.

Invoke `$agentic-work:start-area`, `$agentic-work:start-project`, or `$agentic-work:record-checkpoint`, or select the skill from the installed plugin.

## Placeholder branding

The Codex plugin currently uses `assets/spectra-studio-placeholder.png` for both its marketplace logo and composer icon. Replace that file in place when the final Spectra Studio icon is ready; the manifest paths can remain unchanged.
