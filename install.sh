#!/bin/bash
set -euo pipefail
echo "🚀 Installing DevEnv..."
mkdir -p ~/.local/bin
cd "$(dirname "$0")"
pip install -e . --target=~/.local/lib/python3.14/site-packages 2>/dev/null || pip3 install -e . --target=~/.local/lib/python3.14/site-packages 2>/dev/null || {
    echo "Installing deps..."
    pip3 install click rich questionary --target=~/.local/lib/python3.14/site-packages 2>/dev/null || {
        echo "Using bundled deps..."
        cp -r /tmp/devenv-deps/* ~/.local/lib/python3.14/site-packages/ 2>/dev/null || true
    }
}
cp devenv/cli.py ~/.local/bin/devenv
chmod +x ~/.local/bin/devenv
echo "✅ DevEnv installed! Run 'devenv' to start."
