#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DMG_PATH="$ROOT_DIR/third_party/openbci/openbcigui_v6.0.0-beta.1_macosx.dmg"
APP_NAME="OpenBCI_GUI.app"

echo "==> Bootstrapping BCI stack in $ROOT_DIR"

if [[ ! -d "$ROOT_DIR/.venv" ]]; then
  echo "==> Creating Python virtual environment"
  python3 -m venv "$ROOT_DIR/.venv"
fi

echo "==> Installing Python packages"
"$ROOT_DIR/.venv/bin/pip" install --upgrade pip
"$ROOT_DIR/.venv/bin/pip" install -r "$ROOT_DIR/requirements-alpha.txt"

if [[ ! -f "$DMG_PATH" ]]; then
  echo "==> OpenBCI GUI DMG not found at: $DMG_PATH"
  echo "    Download it first or update DMG_PATH in this script."
  exit 1
fi

echo "==> To install OpenBCI GUI:"
echo "    1) Double-click $DMG_PATH in Finder"
echo "    2) Drag $APP_NAME to /Applications"
echo "    3) Open once and allow any security prompts"

echo "==> Bootstrap complete"
