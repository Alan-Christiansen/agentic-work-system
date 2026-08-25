# System Architecture

The editable visual map is [system-architecture.excalidraw](system-architecture.excalidraw). Open it with the standalone Excalidraw app or [Excalidraw on the web](https://excalidraw.com/).

The drawing distinguishes human-owned canonical records, derived interfaces, agent-maintained restart support, reusable machinery, and deferred adapters.

Connectors are bound to their source and destination nodes so they follow blocks when the drawing is rearranged.

## Reading the map

- Blue: human-owned canonical context or working material.
- Green: derived interface; the Tasks and Portfolio Dashboards do not own canonical state.
- Orange: agent behavior and agent-maintained restart support.
- Purple: reusable or implementation machinery in Git.
- Gray dashed: deferred adapters.

## Core rules

- Underscore-prefixed Area and Project homes whose remaining names match their parent folders are authoritative human PM surfaces.
- `xPM/` supports agents and restartability but cannot override or resurrect deleted human state.
- Reusable Agentic PM behavior lives in Git; personal PM configuration and live state remain in the user's knowledge workspace.
- The Tasks Dashboard is a live task query; the Portfolio Dashboard is a generated cross-domain inventory. Neither authorizes source-record changes or cross-domain prioritization.
- `xPM/` is shared coordination infrastructure rather than private storage owned by one PM role.
- Normal PM work stays inside one selected domain and only loads `pm_scope: managed` records.
- Proposed Projects become active Projects only after explicit agreement.
- User-owned work context stays in the knowledge workspace; reusable machinery and implementation history stay in independent Git repositories.
- Areas and Projects are not tied to one LLM, provider, or conversation. Any compatible agent may continue by reloading the same durable files.
- Conversations provide interaction, not durable state.

## Export policy

The native `.excalidraw` drawing is canonical and intentionally uses Excalidraw's standard interchange format. Exported SVG, PNG, PDF, or other formats are user-managed derivatives and are not stored by default.
