#!/bin/bash

set -e

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
INSTALL_DIR="$HOME/.local/bin"

echo "Installing NetScope..."

mkdir -p "$INSTALL_DIR"

cp "$PROJECT_DIR/src/main.py" "$INSTALL_DIR/netscope"
chmod +x "$INSTALL_DIR/netscope"

echo "NetScope installed to $INSTALL_DIR/netscope"

if [[ ":$PATH:" != *":$INSTALL_DIR:"* ]]; then
    echo
    echo "Add this to your shell configuration:"
    echo 'export PATH="$HOME/.local/bin:$PATH"'
fi

echo
echo "Done!"
