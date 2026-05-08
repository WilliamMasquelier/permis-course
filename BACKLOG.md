# Backlog — permis-course

## Workstreams

| ID | Label | Description |
|----|-------|-------------|
| UX | User Experience | Cowork integration, HTML artifacts, smooth non-technical delivery |
| SYNC | Multi-User Sync | Collaborative teacher/student workflows, progress visibility |
| PLUGIN | Plugin Packaging | Claude Code plugin distribution and maintenance |

---

## Backlog Items

### UX-001: Cowork artifact rendering for lessons

- **Status**: planned
- **Workstream**: UX
- **Priority**: high
- **Description**: Modify `/permis-tutor` to emit lesson HTML as a Cowork artifact instead of starting an HTTP server + Playwright. Cowork renders HTML/CSS/JS artifacts inline but cannot load from localhost or use localStorage. The skill should read the rendered HTML file and output it as artifact content directly.
- **Constraints**: localStorage is sandboxed in Cowork — browser-side progress tracking won't work. The authoritative `student-progress.json` (file-based) is unaffected.
- **Depends on**: Cowork GA availability on user's plan

### UX-002: Side-by-side chat + lesson layout

- **Status**: blocked
- **Workstream**: UX
- **Priority**: medium
- **Description**: Investigate whether Cowork supports a persistent split-pane view (artifact + chat side by side). Currently undocumented — appears to be modal/overlay. If not supported, consider filing a feature request with Anthropic or designing the artifact to include a compact "tutor prompt" panel.
- **Notes**: As of May 2026, no official documentation confirms configurable two-column layout in Cowork.

### UX-003: Live artifact progress dashboard

- **Status**: planned
- **Workstream**: UX
- **Priority**: low
- **Description**: Build a live artifact (Cowork April 2026 feature) that displays student progress pulled from an MCP server or local files. Shows completed lessons, FSRS flashcard stats, exam scores, scenario results. Refreshes on open.
- **Depends on**: SYNC-001 (MCP server) or local-file-only mode

### SYNC-001: MCP sync server for multi-user progress

- **Status**: planned
- **Workstream**: SYNC
- **Priority**: medium
- **Description**: Build a lightweight FastMCP Python server backed by SQLite/Supabase exposing tools: `get_lesson`, `list_lessons`, `submit_progress`, `get_student_progress`, `get_class_overview`, `update_lesson`. Teacher and student Claude instances both connect to the same server. Deploy on existing infra or Railway (~$10/month).
- **Notes**: Only needed when multiple students are active and teacher wants centralized progress visibility. Not required for single-user local study.

### SYNC-002: Teacher progress visibility (without MCP)

- **Status**: planned
- **Workstream**: SYNC
- **Priority**: low
- **Description**: Lightweight alternative to SYNC-001 — students commit their `student-progress.json` to a shared repo branch. Teacher runs a reporting skill that aggregates progress across branches. No server needed, but requires students to push regularly.

### PLUGIN-001: Fix plugin metadata

- **Status**: planned
- **Workstream**: PLUGIN
- **Priority**: high
- **Description**: Update `.claude-plugin/plugin.json` — description says "5 sessions" but the course now has 21 sessions across 8 modules. Update version, description, and verify skill list matches current skills.

### PLUGIN-002: Cowork plugin registration

- **Status**: planned
- **Workstream**: PLUGIN
- **Priority**: medium
- **Description**: Cowork does not auto-discover `.claude/skills/` from a cloned repo. Skills must be delivered via plugin installation. Package `permis-course` as an installable plugin for Cowork users. Students run `/install permis-course` and get all skills registered. Teacher pushes updates to GitHub; students re-install to get new content.
- **Notes**: Plugin auto-update for third-party marketplaces defaults to disabled. Explicit re-install is the reliable path.

### PLUGIN-003: Create AGENTS.md

- **Status**: planned
- **Workstream**: PLUGIN
- **Priority**: medium
- **Description**: `AGENTS.md` is missing but referenced by `.gemini/settings.json` and `.codex/config.toml`. Create a self-contained AGENTS.md (no `.claude/rules/` refs) mirroring the essential content from CLAUDE.md for Codex/Gemini parity.
