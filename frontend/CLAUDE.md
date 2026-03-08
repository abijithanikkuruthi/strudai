# Frontend

Lightweight web UI for StrudelGPT.

## Responsibilities

- Embed the Strudel live-coding environment in an iframe (https://strudel.cc/)
- Provide UI controls for interacting with the backend (prompt input, pattern display)
- Relay generated/modified patterns into the Strudel iframe

## Conventions

- Keep it minimal — Strudel does the heavy lifting
- Static HTML + TypeScript; no framework unless complexity demands it
- Package manager TBD (npm or bun)
