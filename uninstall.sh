#!/usr/bin/env bash
# Plasma Screensaver — uninstaller
set -euo pipefail

INSTALL_DIR="$HOME/.local/share/plasma-screensaver"
BIN_DIR="$HOME/.local/bin"
SYSTEMD_DIR="$HOME/.config/systemd/user"
HYPR_DIR="$HOME/.config/hypr"

echo "==> Plasma Screensaver uninstaller"

# Stop and disable systemd service
if systemctl --user is-enabled plasma-screensaver &>/dev/null; then
    echo "==> Stopping systemd service"
    systemctl --user stop plasma-screensaver 2>/dev/null || true
    systemctl --user disable plasma-screensaver 2>/dev/null || true
fi

# Remove files
rm -f "$SYSTEMD_DIR/plasma-screensaver.service"
rm -f "$BIN_DIR/plasma-screensaver"
rm -f "$HYPR_DIR/plasma-screensaver.conf"
rm -rf "$INSTALL_DIR"

# Remove include from hyprland.lua
if [[ -f "$HYPR_DIR/hyprland.lua" ]]; then
    sed -i '/plasma-screensaver/d' "$HYPR_DIR/hyprland.lua"
fi

systemctl --user daemon-reload 2>/dev/null || true

echo "==> Uninstalled. Plasma Screensaver has been removed."
