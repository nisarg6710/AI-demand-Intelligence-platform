# M13 — CI/CD

## Overview

This milestone introduces automated Continuous Integration (CI) for the
AI Demand Intelligence Platform using GitHub Actions.

The objective is to automatically validate backend and frontend changes
whenever code is pushed to `main` or a pull request targets `main`.

---

## Objectives

- Automate backend test execution.
- Validate the configuration loader independently of local secrets.
- Validate MLflow tracking functionality.
- Lint the React frontend.
- Build the production frontend.
- Prevent broken code from being merged unnoticed.
- Establish a reproducible CI workflow.

---

## CI Architecture

```text
                    Git Push / Pull Request
                              |
                              v
                    GitHub Actions Workflow
                         (.github/workflows)
                              |
                 +------------+------------+
                 |                         |
                 v                         v
          Backend Tests             Frontend CI
                 |                         |
        Install Python deps          npm ci
                 |                         |
        Run pytest tests             ESLint
                 |                         |
                 |                  Production Build
                 |                         |
                 +------------+------------+
                              |
                              v
                         CI Result


GitHub Actions Workflow

Workflow:

.github/workflows/ci.yml

The workflow is triggered by:

Pushes to main
Pull requests targeting main
Backend CI

The backend job uses:

Ubuntu latest
Python 3.12
requirements.txt
Pytest

The following tests are executed:

tests/test_config_loader.py
tests/test_moving_average.py
tests/test_arima.py
tests/mlops/test_mlflow_tracking.py

The configuration loader test uses a temporary configuration file instead
of depending on the developer's private database.yaml.

This allows CI to test configuration loading without exposing database
credentials.

Frontend CI

The frontend job uses:

Ubuntu latest
Node.js 22
npm

The following commands are executed:

npm ci
npm run lint
npm run build

This ensures that the React application:

Installs successfully from the lockfile.
Passes ESLint validation.
Produces a valid production build.
Security Considerations

Private configuration files are intentionally excluded from Git.

Examples include:

configs/database.yaml
configs/paths.yaml
configs/etl.yaml

The repository contains example configuration files for setup purposes,
while CI tests use temporary test configurations.

No database credentials or API keys are required by the CI workflow.

CI Result

The GitHub Actions workflow was successfully validated with:

Backend Tests — Passed
Frontend Lint and Build — Passed

The workflow therefore provides automated validation for both major
application layers.

Technologies
GitHub Actions
Python
Pytest
Node.js
npm
ESLint
React
MLflow

                  Forecasting Pipeline
                         |
                         v
                      MLflow
                         |
              +----------+----------+
              |                     |
          Parameters             Metrics
              |                     |
              +----------+----------+
                         |
                         v
                    Artifacts
                         |
                         v
                  GitHub Repository
                         |
                         v
                  GitHub Actions
                         |
             +-----------+-----------+
             |                       |
        Backend Tests          Frontend Build
             |                       |
             +-----------+-----------+
                         |
                         v
                    CI Result