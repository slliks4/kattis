#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# ==========================
# Dependencies
# ==========================
ensure_pkg() {
    if ! pacman -Qi "$1" >/dev/null 2>&1; then
        echo "Installing missing dependency: $1"
        sudo pacman -S --noconfirm "$1"
    fi
}

ensure_pkg curl
ensure_pkg unzip

# ==========================
# Install
# ==========================
mkdir -p "$HOME/.local/bin"

ln -sf "$SCRIPT_DIR/kattis-new" "$HOME/.local/bin/knew"

echo "Installed kattis-new to ~/.local/bin as knew"
