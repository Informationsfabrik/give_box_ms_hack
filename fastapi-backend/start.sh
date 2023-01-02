#!/usr/bin/env bash
set -ex

# Let the DB start
python backend_pre_start.py

# Run migrations
alembic upgrade head

# populater with initial data
python init_db.py

# Run program
if [[ -z "${DEV}" ]]; then
  uvicorn main:app --host 0.0.0.0 --port 8081 --proxy-headers
else
  echo "Starting dev server"
  uvicorn main:app --host 0.0.0.0 --port 8081 --proxy-headers --reload-dir .
fi
