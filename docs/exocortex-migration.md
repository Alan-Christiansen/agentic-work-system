# Exocortex Migration

## Goal

Retire the old `601 - Exocortex` system after its useful principles and content have safe, reviewed destinations.

## Do not migrate wholesale

Translate generic ideas into this repository. Relocate personal and venture data into appropriate vault homes. Keep the old folder intact until live consumers have been rewired and tested.

## Principles to translate

- Minimal context loading
- Specific context overriding broader defaults
- Canonical sources separated from derived summaries
- Human approval for consequential writes
- Privacy boundaries
- Concise agent handoffs

## Content to review for relocation

- Global working preferences
- Career candidate profile and resume guidance
- AEF marketing standards
- Active project definitions
- Other unique personal or venture context

## Known cutover dependency

The Job Search workflow currently references Exocortex candidate-profile, resume-guidance, and operating-preference files. Do not archive or delete the old folder until replacement sources are established and a workflow test passes.

## Current manual loading path

Alan's vault uses a compact working profile plus a routing index as the project-orientation entry point. The profile is a declared derived view; the index loads deeper personal or domain context only when the task matches. Non-private source copies in the AI Context Area are authoritative for ordinary project work, so those tasks do not require Exocortex access.

The existing Exocortex remains unchanged as a temporary compatibility source for Job Search. Private-tier context, AEF content, Job Search profiles, and Job Search dependencies are outside this staged cutover.

The baseline and deeper routed loading both passed a fresh-project test on 2026-08-20 without Exocortex access. Continue gathering real-use evidence before automating the loading process or migrating Job Search.

The loading path demonstrated:

- enough personal context to tailor a fresh project task;
- routed access to deeper task-relevant context without Exocortex;
- materially lower context use than loading the full source collection;
- no automatic loading of private-tier sources;
- successful orientation without conversation history.

Do not automate or broaden the migration until repeated project tasks reveal a stable procedure and what the baseline misses or loads unnecessarily.

## Exclusion

The downloaded `claude-obsidian` project is unrelated to this migration implementation. Do not invoke its skills, copy its code, or adopt its managed wiki structure.
