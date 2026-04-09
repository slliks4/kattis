#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Current shell: $SHELL"

# ==========================
# Dependency check (NO install)
# ==========================
check_dep() {
    if ! command -v "$1" >/dev/null 2>&1; then
        echo "Missing dependency: $1"
        return 1
    fi
    return 0
}

missing=false

for dep in curl unzip diff; do
    if ! check_dep "$dep"; then
        missing=true
    fi
done

if $missing; then
    echo ""
    echo "Some dependencies are missing."
    echo "Please install them manually:"
    echo "  Required: curl, unzip, diff"
    echo ""
    echo "Examples:"
    echo "  Arch: sudo pacman -S curl unzip diffutils"
    echo "  macOS: brew install curl unzip diffutils"
    echo ""
    echo "Continuing installation anyway..."
fi

# ==========================
# Install binary
# ==========================
mkdir -p "$HOME/.local/bin"
ln -sf "$SCRIPT_DIR/kattis-new" "$HOME/.local/bin/knew"

echo "Installed knew -> ~/.local/bin/knew"

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
if ! grep -q 'export PATH="$HOME/.local/bin:$PATH"' "$SHELL_RC" 2>/dev/null; then
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$SHELL_RC"
    echo "Added ~/.local/bin to PATH in $SHELL_RC"
fi

# ==========================
# Set default KATTIS_DIR
# ==========================
if ! grep -q "export KATTIS_DIR=" "$SHELL_RC" 2>/dev/null; then
    echo 'export KATTIS_DIR="$HOME/kattis"' >> "$SHELL_RC"
    echo "Added KATTIS_DIR to $SHELL_RC"
fi

# ==========================
# Final message
# ==========================
echo ""
echo "Installation complete."
echo "Restart your shell or run:"
echo "  source $SHELL_RC"
