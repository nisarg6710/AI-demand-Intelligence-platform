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
