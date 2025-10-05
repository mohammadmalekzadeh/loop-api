#!/bin/bash

echo "[Liara] Running pre-build hook..."

pip install --upgrade pip

pip install -r requirements.txt

python3 --version
pip --version

echo "[Liara] pre-build completed."
