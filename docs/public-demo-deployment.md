# Public Demo Deployment

The public portfolio demo uses the standalone FastAPI service in `deployment/demo_api` and the React/Vite application in `frontend`. The full local application continues to use its production database and integrations; those are not part of this deployment.

## Render API

`render.yaml` describes a Free web service with:

- Root directory: `deployment/demo_api`
- Python version: `3.12.0` (from `.python-version`)
- Build command: `pip install -r requirements.txt`
- Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- Health check: `/health`

The service installs only the dependencies in `deployment/demo_api/requirements.txt`. It reads the committed precomputed JSON files from `deployment/demo_api/data/` and does not require MySQL, Gemini, or private environment variables. Render may sleep while idle, so the first request can take longer while it starts.

## Vercel frontend

Create a Vercel project with root directory `frontend`, install command `npm ci`, build command `npm run build`, and output directory `dist`. Set the build-time environment variable:

```text
VITE_API_BASE_URL=https://<actual-render-service>.onrender.com
VITE_DEMO_MODE=true
```

Replace the placeholder only after Render creates the service. Set the value for the Vercel environments that should use the public API, then redeploy so Vite embeds it in the frontend build. Do not use a localhost URL for a public deployment. `frontend/vercel.json` rewrites client routes to `index.html` for direct navigation and refresh.

## Local public-demo smoke test

From the repository root in PowerShell:

```powershell
.\venv\python.exe -m uvicorn main:app --app-dir deployment/demo_api --host 127.0.0.1 --port 8001
```

In another PowerShell terminal, use `Invoke-RestMethod` against `http://127.0.0.1:8001/health`, all `/analytics/*` routes, `/forecast/model-comparison`, `/forecast/historical-holdout`, and the POST demo routes. For the frontend, set `VITE_API_BASE_URL` in Vercel; keep local demo environment files untracked.

Before public release, verify all five pages, direct route refresh, CORS, chart data, demo labels, and the first request after the Render service has been idle.
