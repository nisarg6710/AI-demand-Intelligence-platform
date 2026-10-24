# Public Demo Deployment

The public portfolio demo uses the standalone FastAPI service in
`deployment/demo_api` and the React/Vite application in `frontend`. The full
local application and its production database integrations remain separate.
The public demo reads a packaged, read-only SQLite aggregate snapshot and does
not connect to local MySQL.

## Render API

The checked-in `render.yaml` configures a Free web service with:

- Root directory: `deployment/demo_api`
- Python version: `3.12.0` from `deployment/demo_api/.python-version`
- Build command: `pip install -r requirements.txt`
- Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- Health check: `/health`
- `PUBLIC_DEMO_SNAPSHOT_DIR=snapshot`

Because the service root is `deployment/demo_api`, the build installs
`deployment/demo_api/requirements.txt`, and the relative snapshot setting
resolves to `deployment/demo_api/snapshot`. That directory must include
`aggregate_current.json` and the generation-specific SQLite database named in
its manifest. Both are packaged beneath the service root. When readiness or an
analytics operation constructs the SQLite repository, it validates the
pointer, manifest, schema, and database, then opens SQLite in read-only mode.
The application startup hook loads the JSON benchmark and historical holdout
artifacts. It does not regenerate or repair snapshot files. Render may sleep
while idle, so the first request can take longer during a cold start.

The repository configuration does not establish what values are currently
set in the Render dashboard. Confirm the service root, environment variables,
and latest deployment there before relying on hosted behavior.

## Vercel frontend configuration

The frontend reads these build-time variables in
`frontend/src/services/api.js`:

- `VITE_DEMO_MODE=true` selects public-demo frontend behavior, including the
  demo forecast request contract.
- `VITE_API_BASE_URL` is the API base URL used for requests.

For local development, the checked-in `frontend/.env.example` points at the
local full API (`http://127.0.0.1:8000`) with demo mode disabled. The local
`frontend/.env.demo` points at the standalone demo API (`http://127.0.0.1:8001`);
use Vite's `demo` mode to load that file. These are local values, not hosted
Vercel settings.

For the hosted frontend, configure the Vercel project with root directory
`frontend`, install command `npm ci`, build command `npm run build`, and output
directory `dist`. Set these variables in the Vercel project for each intended
deployment environment:

```text
VITE_API_BASE_URL=https://<your-render-service>.onrender.com
VITE_DEMO_MODE=true
```

Replace the placeholder with the actual Render service URL. The repository
does not verify the current Vercel dashboard values or the deployed API URL.
Vite embeds these values into the frontend build, so redeploy Vercel after
changing them. Do not use a localhost API URL for a public deployment. The
frontend must not contain server-side credentials. Client-side routing is
rewritten to `index.html` by `frontend/vercel.json`.

## Optional Gemini guidance

Deterministic analytics questions use approved operations against the
read-only SQLite snapshot. Forecast requests use the seasonal-naive baseline
described below. A narrow set of general project-capability questions may
receive Gemini-generated business guidance; this guidance uses the bounded
question and fixed project context, not live data access.

Gemini is optional and is called only when both dedicated server-side
variables are configured:

```text
DEMO_GEMINI_API_KEY=<configure privately in Render>
DEMO_GEMINI_MODEL=<configure a supported model in Render>
```

No model name is prescribed here. Configure these only in Render's private
service environment settings if Gemini guidance is wanted. Never commit the
key or expose it through a `VITE_` variable. General guidance may consume
Gemini quota. If either setting is absent, the API uses its clearly labelled
fixed project-capability fallback without making a Gemini request. If a
configured provider request fails or returns no usable answer, the API uses
the same honest fallback. Snapshot-backed answers, AI-generated guidance,
and fallback responses are distinct. Snapshot freshness against MySQL remains
unverified (`freshness_verified: false`); neither guidance nor analytics
implies that the snapshot is current.

The checked-in Render configuration does not declare either Gemini variable.
Whether they have been added in the Render dashboard cannot be verified from
repository files.

## Forecast behavior

`POST /forecast` computes a seasonal-naive baseline from the snapshot's monthly
aggregate series. It repeats each calendar month's units from 12 months
earlier, requires at least 24 ordered consecutive monthly observations, and
supports horizons from 1 to 12 months (default 3). Historical observations
and future forecast periods are returned separately. The result represents
units sold, not currency or revenue. This is an inexpensive baseline, not a
trained model; it has not been independently backtested here and makes no
accuracy or model-superiority claim. The same calculation is exposed by
`GET /forecast/predictions`; recorded benchmark comparisons and historical
holdout results are separate artifacts, not future forecasts.

## Local API smoke test

From the repository root in PowerShell, start the demo API:

```powershell
.\venv\python.exe -m uvicorn main:app --app-dir deployment/demo_api --host 127.0.0.1 --port 8001
```

In a second terminal, check `http://127.0.0.1:8001/live` and `/health`, then
exercise the analytics routes, `POST /analytics`, `POST /forecast`,
`GET /forecast/predictions`, and `POST /chat`. `/health` is readiness and
should fail when the required snapshot is unavailable; `/live` reports process
liveness.

## Post-deployment smoke-test checklist

After deploying, use the actual Render service URL and verify:

1. `GET /live` returns a successful liveness response, and `GET /health`
   returns success only when the packaged snapshot is ready.
2. `GET /analytics/summary` and `GET /analytics/monthly-sales` return
   snapshot-backed data with `freshness_verified: false` and units described
   as units sold.
3. `POST /forecast` with a valid horizon returns separate historical and
   future periods, the seasonal-naive method, and snapshot metadata. Try an
   invalid horizon and confirm it is rejected.
4. Ask a supported deterministic question in `POST /chat` and confirm it is
   answered from the snapshot. Ask a general project-capability question:
   when both Gemini variables are configured it may return labelled
   AI-generated guidance; without configuration or when Gemini is unavailable
   it should return the labelled fixed fallback without claiming an AI answer.
5. In the hosted frontend, confirm `VITE_DEMO_MODE=true`, the configured API
   base URL is the actual Render URL, and Dashboard, Analytics, Forecasting,
   Chat, and Agents load. Check direct route refresh and the first API request
   after Render has been idle.

Dashboard values, deployment environment variables, CORS behavior, and
hosted cold-start behavior must be verified in the respective hosting
services; this guide does not assert those dashboard settings have been
checked.
