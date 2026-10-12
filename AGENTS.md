# AGENTS.md

Scratch/demo repo for local LLMs (Ollama) and MCP. No build, test, lint, CI, or packaging — scripts run directly.

## Running scripts
- Python 3.14 venv at `.venv/` (untracked, gitignored). A fresh clone won't have it; recreate with
  `python3.14 -m venv .venv && .venv/bin/pip install -r requirements.txt`.
- Run via `.venv/bin/python <script>.py`, or `source .venv/bin/activate`.
- All demos talk to a local Ollama server at `http://localhost:11434`; it must already be running.
- `requirements.txt` is a full `pip freeze` (includes `ollama`, `mcp`, `openai`).

## Models (see `ollama list`)
- `llama3`: `llama3-demo.py`, `ollama-demo.py`, `sotd.py`, `asyncio-mcp-demo.py`.
- `SeekerThe3rd/chatmusician`: `chatmusician-demo.py`.

## Scripts
- `sotd.py` — two chained llama3 calls (lyrics -> chord progression); writes `output/sotd-<timestamp>.txt` (`output/` gitignored). Tune via top-of-file knobs `theme1/theme2`, `adjective1`, `adverb1`, `terseness` and `DEBUG`.
- `asyncio-mcp-demo.py` — MCP client: spawns `@modelcontextprotocol/server-sqlite` via `npx`, maps its tools to llama3, calls one; creates `./my_database.db`. Needs Node/npx, which is NOT installed here, so it cannot run.
- `llama3-demo.py`, `ollama-demo.py`, `chatmusician-demo.py` — minimal single-call prompt demos.

## Faux website
- `.opencode/agent/faux*.md` define a `faux` orchestrator (+ editor/validator subagents) that pulls the live `https://sayitaintfaux.com/` page into repo-root `faux/` and edits it. The live site's TLS cert is expired, so it must be fetched with `curl -k`. Read those agent files for the full workflow.
- `opencode/faux/index.html` is the older hand-written W3.CSS page (assets in `opencode/faux/images/`); open directly in a browser, no build step.

## Misc
- `.backup-venv.delme/` is a stale untracked venv backup; ignore it.
- `README.ipynb` holds setup notes, not code.
