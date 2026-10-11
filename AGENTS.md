# AGENTS.md

Scratch/demo repo for local LLMs (Ollama) and MCP. No build, test, lint, CI, or packaging.

## Running scripts
- Use the local venv (Python 3.14): `.venv/bin/python <script>.py`, or `source .venv/bin/activate`. It is NOT tracked (self-ignored via `.venv/.gitignore`), so a fresh clone won't have it.
- Every demo talks to a local Ollama server at `http://localhost:11434`; it must already be running.
- `requirements.txt` is incomplete: it omits `mcp` and `openai`, which `asyncio-mcp-demo.py` imports. Both are installed in `.venv`, but a fresh `pip install -r requirements.txt` will break that demo.

## Models (already pulled locally, see `ollama list`)
- `llama3-demo.py`, `ollama-demo.py`, `sotd.py` use `llama3`.
- `chatmusician-demo.py` uses `SeekerThe3rd/chatmusician`.

## Scripts
- `sotd.py` — "song of the day": two chained llama3 calls (lyrics -> chord progression), writes timestamped files to `output/` (gitignored, local-only). Tune via the knobs at the top (`theme1/theme2`, `adjective1`, `adverb1`, `terseness`) and `DEBUG`.
- `asyncio-mcp-demo.py` — MCP client that spawns `@modelcontextprotocol/server-sqlite` via `npx`, converts its tools for llama3, and executes a call; creates `./my_database.db`. Needs Node/npx, which is NOT installed on this machine.
- `llama3-demo.py`, `ollama-demo.py`, `chatmusician-demo.py` — minimal single-call prompt demos.

## Static site
- `opencode/faux/index.html` is a hand-written W3.CSS page with assets in `opencode/faux/images/`; open it directly in a browser, no build step. A prior version lived at `opencode/index.html` (see git history).

## Misc
- `.backup-venv.delme/` is a stale untracked venv backup; ignore it.
- `README.ipynb` holds setup notes, not code.
