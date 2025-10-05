#!/bin/bash

echo "[Liara] Running post-build hook..."

echo "Applying Alembic migrations..."
if alembic upgrade head; then
  echo "Alembic migrations applied successfully."
else
  echo "Alembic not configured properly, skipping migration."
fi

echo "Initializing database schema..."
if python3 -c "from app.db.init_db import init_db; init_db()"; then
  echo "Database initialized successfully."
else
  echo "init_db() skipped or failed."
fi

echo "[Liara] post-build completed."
