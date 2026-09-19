# Plasma Screensaver

Real-time animated plasma effect screensaver for Wayland compositors. Smooth 30fps, idle detection, easy install.

## Features

- **Plasma Mode**: Classic overlapping sine waves with HSV color cycling
- **Smooth 30fps**: Downscaled rendering with bilinear upscaling
- **Fullscreen**: Takes over your entire display
- **Idle Detection**: Activates after configurable idle timeout
- **Privacy First**: No telemetry, no network calls, no accounts
- **Open Source**: MIT licensed
- **Easy Install**: One command to install, systemd service for auto-start

## Install

```bash
git clone https://github.com/subtiliorars-sys/plasma-screensaver.git
cd plasma-screensaver
./install.sh
```

This installs:
- `~/.local/bin/plasma-screensaver` — launcher script
- `~/.config/systemd/user/plasma-screensaver.service` — auto-start on idle
- `~/.config/hypr/plasma-screensaver.conf` — Hyprland window rules

## Usage

```bash
# Run once (no idle wait)
plasma-screensaver --no-idle

# Run with custom idle timeout (seconds)
plasma-screensaver --idle-timeout 600

# Run immediately, no idle detection
plasma-screensaver --no-idle
```

## Systemd

```bash
# Start now
systemctl --user start plasma-screensaver

# Enable auto-start on login
systemctl --user enable plasma-screensaver

# Check status
systemctl --user status plasma-screensaver

# Stop
systemctl --user stop plasma-screensaver
```

## Hyprland

The installer adds window rules to `~/.config/hypr/plasma-screensaver.conf`:
- Fullscreen
- No focus
- No blur/shadow
- Special workspace

Include in your `hyprland.lua`:
```lua
include = ~/.config/hypr/plasma-screensaver.conf
```

## Uninstall

```bash
./uninstall.sh
```

## Buy

**$9.99 one-time** — https://buy.stripe.com/fZu00b4g154K4IManK93y02

## License

MIT
