# Project Guidelines

## Code Style
- Keep backend changes in Python with FastAPI patterns already used in `src/app.py`.
- Keep frontend behavior in `src/static/app.js` and UI assets in `src/static/`.
- Favor small, focused functions and straightforward request/response handling.
- When adding tests, prefer `pytest` and structure tests using AAA (Arrange-Act-Assert).

## Architecture
- The app is a single FastAPI service in `src/app.py`.
- Static frontend files are served by FastAPI from `src/static/` via the `/static` mount.
- Root path (`/`) redirects to `src/static/index.html`.
- Activity data is stored in-memory (`activities` dict), so server restarts reset all signups.

## Build and Test
- Install dependencies: `pip install -r requirements.txt`
- Run locally (preferred): `uvicorn src.app:app --reload --reload-include src/static/*`
- Alternative debug/run path is defined in `.vscode/launch.json` (`Launch Mergington WebApp`).
- Run tests: `pytest`

## Environment
- This dev container includes an up-to-date version of Git available on `PATH`.
- This dev container includes `node`, `npm`, and `eslint` on `PATH` for Node.js and JavaScript development.
- This dev container includes `python3` and `pip3` on `PATH`, plus Python language extensions.
- Workspace OS: Debian GNU/Linux 13 (trixie).
- To open URLs in the host browser, use `"$BROWSER" <url>`.
- Common CLI tools on `PATH` include: `apt`, `dpkg`, `git`, `curl`, `wget`, `ssh`, `scp`, `rsync`, `gpg`, `ps`, `lsof`, `netstat`, `top`, `tree`, `find`, `grep`, `zip`, `unzip`, `tar`, `gzip`, `bzip2`, `xz`.

## Conventions
- Keep API behavior centered on current routes:
- `GET /activities` returns the activities map.
- `POST /activities/{activity_name}/signup?email=...` signs up a student and returns a message.
- For unknown activity names, return `HTTPException(status_code=404, detail="Activity not found")`.
- If you add validation (duplicates/capacity/email checks), add corresponding tests under `tests/`.
- Preserve beginner-friendly readability because this repository is a GitHub Skills learning exercise.
