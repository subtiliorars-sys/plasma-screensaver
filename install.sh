#!/usr/bin/env bash
# Plasma Screensaver — one-command installer
# Usage: ./install.sh [--no-systemd] [--no-hyprland]

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INSTALL_DIR="$HOME/.local/share/plasma-screensaver"
BIN_DIR="$HOME/.local/bin"
SYSTEMD_DIR="$HOME/.config/systemd/user"
HYPR_DIR="$HOME/.config/hypr"

echo "==> Plasma Screensaver installer"

# Create directories
mkdir -p "$INSTALL_DIR" "$BIN_DIR" "$SYSTEMD_DIR" "$HYPR_DIR"

# Copy source
echo "==> Copying source to $INSTALL_DIR"
cp -r "$REPO_DIR"/plasma_tkinter.py "$INSTALL_DIR/"
cp -r "$REPO_DIR"/landing "$INSTALL_DIR/" 2>/dev/null || true

# Create launcher script
cat > "$BIN_DIR/plasma-screensaver" << 'LAUNCHER'
#!/usr/bin/env bash
# Plasma Screensaver launcher
INSTALL_DIR="$HOME/.local/share/plasma-screensaver"
cd "$INSTALL_DIR"
exec python3 plasma_tkinter.py "$@"
LAUNCHER
chmod +x "$BIN_DIR/plasma-screensaver"

# Install systemd service
if [[ "${1:-}" != "--no-systemd" ]]; then
    echo "==> Installing systemd user service"
    cat > "$SYSTEMD_DIR/plasma-screensaver.service" << SERVICE
[Unit]
Description=Plasma Screensaver
After=graphical-session.target

[Service]
Type=simple
ExecStart=%h/.local/bin/plasma-screensaver --idle-timeout 300
Restart=on-failure
RestartSec=5

[Install]
WantedBy=graphical-session.target
SERVICE

    systemctl --user daemon-reload
    systemctl --user enable plasma-screensaver
    echo "==> Systemd service installed (not started — start with: systemctl --user start plasma-screensaver)"
fi

# Install Hyprland rules
if [[ "${1:-}" != "--no-hyprland" ]]; then
    echo "==> Installing Hyprland window rules"
    cat > "$HYPR_DIR/plasma-screensaver.conf" << 'HYPR'
# Plasma Screensaver — Hyprland window rules
windowrulev2 = fullscreen,class:^(plasma-screensaver)$
windowrulev2 = nofocus,class:^(plasma-screensaver)$
windowrulev2 = noblur,class:^(plasma-screensaver)$
windowrulev2 = noshadow,class:^(plasma-screensaver)$
windowrulev2 = special:workspace,class:^(plasma-screensaver)$
HYPR

    # Source from hyprland.lua if it exists
    if [[ -f "$HYPR_DIR/hyprland.lua" ]]; then
        if ! grep -q "plasma-screensaver" "$HYPR_DIR/hyprland.lua"; then
            echo 'include = ~/.config/hypr/plasma-screensaver.conf' >> "$HYPR_DIR/hyprland.lua"
        fi
    else
        echo 'include = ~/.config/hypr/plasma-screensaver.conf' > "$HYPR_DIR/hyprland.lua"
    fi
    echo "==> Hyprland rules installed"
fi

echo ""
echo "==> Installation complete!"
echo ""
echo "Usage:"
echo "  plasma-screensaver              # Run once"
echo "  plasma-screensaver --mode fire  # Run with specific mode"
echo "  plasma-screensaver --no-idle    # Run immediately (no idle wait)"
echo ""
echo "Systemd:"
echo "  systemctl --user start plasma-screensaver"
echo "  systemctl --user status plasma-screensaver"
echo ""
echo "Uninstall:"
echo "  ./uninstall.sh"
