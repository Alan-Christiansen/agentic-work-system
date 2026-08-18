# Agentic Work Plugin

Reusable Claude, Cowork, ChatGPT, and Codex skills for projects that follow the Agentic Work System protocol.

## Included skills

- `/agentic-work:record-checkpoint`: verify a reviewed human-created commit, synchronize the Obsidian project checkpoint, and stop.

## Install in Claude Cowork

1. Open **Customize → Plugins**.
2. Choose the option to add or upload a plugin from a file.
3. Select `dist/agentic-work.plugin` from this repository.
4. Confirm that the `record-checkpoint` skill is enabled.
5. Open a new task with access to the individual Obsidian project folder and its companion repository.
6. Run `/agentic-work:record-checkpoint`.

The skill does not create a commit, push, deploy, or begin the next task.

## Install in Codex

The repository includes a local Codex marketplace at `.agents/plugins/marketplace.json`. From any folder, run:

```sh
codex plugin marketplace add "/Users/alanc/_Dev/Studio-Dev/200 - Projects/270 - Tech & Systems/agentic-work-system"
codex plugin add agentic-work@personal
```

Start a new Codex task after installation so the skill is discovered.

Invoke the skill as `$agentic-work:record-checkpoint` or select it from the installed plugin.
