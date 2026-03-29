#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Current shell: $SHELL"

# ==========================
# Dependency installers
# ==========================
ensure_pkg_pacman() {
    if ! pacman -Qi "$1" >/dev/null 2>&1; then
        echo "Installing missing dependency: $1 (pacman)"
        sudo pacman -S --noconfirm "$1"
    fi
}

ensure_pkg_brew() {
    if ! brew list "$1" >/dev/null 2>&1; then
        echo "Installing missing dependency: $1 (brew)"
        brew install "$1"
    fi
}

# ==========================
# Detect package manager
# ==========================
if command -v pacman >/dev/null 2>&1; then
    ensure_pkg_pacman curl
    ensure_pkg_pacman unzip

elif command -v brew >/dev/null 2>&1; then
    ensure_pkg_brew curl
    ensure_pkg_brew unzip

else
    echo "No supported package manager found."
    echo "Please ensure curl and unzip are installed."
    echo "Continuing installation..."
fi

# ==========================
# Install binary
# ==========================
mkdir -p "$HOME/.local/bin"
ln -sf "$SCRIPT_DIR/kattis-new" "$HOME/.local/bin/knew"

# ==========================
# Detect shell config file
# ==========================
SHELL_NAME="$(basename "$SHELL")"

case "$SHELL_NAME" in
    zsh)
        SHELL_RC="$HOME/.zshrc"
        ;;
    bash)
        SHELL_RC="$HOME/.bashrc"
        ;;
    *)
        SHELL_RC="$HOME/.profile"
        echo "Unknown shell: $SHELL_NAME"
        echo "Using $SHELL_RC"
        ;;
esac

echo "Detected shell: $SHELL_NAME"
echo "Using config: $SHELL_RC"

# ==========================
# Ensure PATH
# ==========================
if ! grep -q '.local/bin' "$SHELL_RC" 2>/dev/null; then
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$SHELL_RC"
    echo "Added ~/.local/bin to $SHELL_RC"
fi

# ==========================
# Set default KATTIS_DIR
# ==========================
if ! grep -q "KATTIS_DIR" "$SHELL_RC" 2>/dev/null; then
    echo 'export KATTIS_DIR="$HOME/kattis"' >> "$SHELL_RC"
    echo "Added KATTIS_DIR to $SHELL_RC"
fi

echo "Installed kattis-new as 'knew'"
echo "Restart your shell or run: source $SHELL_RC"
