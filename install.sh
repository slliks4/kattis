#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# ==========================
# Dependencies (Arch)
# ==========================
ensure_pkg() {
    if ! pacman -Qi "$1" >/dev/null 2>&1; then
        echo "Installing missing dependency: $1"
        sudo pacman -S --noconfirm "$1"
    fi
}

if command -v pacman >/dev/null 2>&1; then
    ensure_pkg curl
    ensure_pkg unzip
else
    echo "Please ensure curl and unzip are installed"
fi

# ==========================
# Install binary
# ==========================
mkdir -p "$HOME/.local/bin"
ln -sf "$SCRIPT_DIR/kattis-new" "$HOME/.local/bin/knew"

# ==========================
# Set default KATTIS_DIR
# ==========================
if ! grep -q "KATTIS_DIR" "$HOME/.zshrc" 2>/dev/null; then
    echo 'export KATTIS_DIR="$HOME/kattis"' >> "$HOME/.zshrc"
    echo "Added KATTIS_DIR to ~/.zshrc"
fi

echo "Installed kattis-new as 'knew'"
echo "Restart your shell or run: source ~/.zshrc"
