# Standalone demo API

The analytics endpoints read the published aggregate SQLite snapshot in
read-only mode. Locally, the API uses the repository's
`exports/public_demo/` directory by default.

Set `PUBLIC_DEMO_SNAPSHOT_DIR` to override that location. The configured
directory must contain `aggregate_current.json` and the generation-specific
SQLite file referenced by that manifest. The API validates the manifest,
schema, and snapshot before returning analytics. It does not create, repair, or
replace the pointer or database. The snapshot manifest's
`freshness_verified: false` status is preserved in analytics responses.

Relative values for `PUBLIC_DEMO_SNAPSHOT_DIR` are resolved from the demo API
service directory, independent of the process working directory. If the local
export directory is absent and the variable is unset, the API uses the
packaged `snapshot/` directory when present.

The Render service must be supplied with a directory containing both files;
the local `exports/public_demo/` directory is not a deployed data source by
itself. No MySQL connection or production query engine is used by this API.

## Optional Gemini answers in Business Chat

Deterministic analytics questions continue to query the validated read-only
SQLite snapshot, and forecast questions continue to compute the seasonal-naive
baseline described below. A narrow set of general project-capability questions
(for example, how the project can help an organization) may use Gemini. Those
answers use only a fixed project description and the bounded question; they do
not query snapshot rows, MySQL, production agents, or arbitrary SQL.

Gemini is not called unless both dedicated variables are configured. Set these
in a local environment or in Render's service environment settings:

```text
DEMO_GEMINI_API_KEY=<your Gemini API key>
DEMO_GEMINI_MODEL=<supported Gemini model name>
```

Never commit either value or put the key in a `VITE_` frontend variable. Store
the key in Render's private environment settings. General business questions
can consume Gemini quota when configured. Without the dedicated key and model,
the API returns a fixed, clearly labelled project-capability fallback and makes
no Gemini call. Snapshot-backed answers and AI-generated general explanations
are labelled separately; neither implies that snapshot freshness has been
verified.

## Public forecast baseline

`POST /forecast` computes a seasonal-naive baseline from the read-only monthly
aggregate table. The method repeats each calendar month's units from 12 months
earlier. It requires at least 24 ordered, consecutive monthly observations and
returns an error if periods are missing, duplicated, or irregular. The request
body accepts an optional integer `horizon` from 1 to 12; the default is 3.
Historical observations and future forecast periods are returned separately.

This is an inexpensive explanatory baseline, not a trained model. It has not
been backtested here, and the endpoint makes no accuracy or model-superiority
claim. Forecasts are units sold, not revenue or currency. Snapshot freshness
remains unverified. Recorded model-comparison metrics and historical holdout
predictions remain separate endpoints and are not reused as future forecasts.
