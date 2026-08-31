#!/bin/sh
# Construye el sitio y lo sirve en local. Sin dependencias: sólo python3, que ya viene en macOS.
set -e
cd "$(dirname "$0")"
python3 build.py

PORT=8000
while lsof -i :$PORT >/dev/null 2>&1; do PORT=$((PORT+1)); done
echo "→ http://localhost:$PORT       (English)"
echo "→ http://localhost:$PORT/es/   (Español)"
echo "  Ctrl+C para parar."
( sleep 1; open "http://localhost:$PORT" ) &
python3 -m http.server "$PORT" --directory dist
