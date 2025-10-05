#!/bin/bash

echo "[Liara] Running pre-start hook..."

find . -type d -name "__pycache__" -exec rm -rf {} + || true

echo "[Liara] pre-start completed."
