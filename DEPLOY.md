# DEPLOY.md — Plasma Screensaver Launch Checklist

## Pre-Launch

- [ ] **Screenshots recorded** — 3 plasma frames + animated GIF in `landing/assets/`
- [ ] **Landing page updated** — OG tags, Twitter card, GIF embedded
- [ ] **Stripe payment link active** — https://buy.stripe.com/fZu00b4g154K4IManK93y02
- [ ] **GitHub Pages deployed** — `gh-pages` branch up to date
- [ ] **README monetization section added** — Stripe link + GitHub Sponsors
- [ ] **Google Analytics / Plausible** — uncomment tracking in `index.html`
- [ ] **Cross-browser tested** — Chrome, Firefox, Safari
- [ ] **Mobile-responsive** — test on phone viewport

## Launch Day

### Reddit (highest ROI)

**r/unixporn** — your exact audience
```
Title: I built a native Wayland screensaver for Hyprland — $9.99, open source
Body: 
After years of xscreensaver hacks on Wayland, I built something native.

Plasma Screensaver:
- Real-time animated plasma effect (30fps)
- Idle detection (activates after N minutes, exits on any input)
- Systemd service for auto-start
- Hyprland window rules built in
- MIT licensed, one-command install

$9.99 one-time. Pay once, use forever.

https://subtiliorars-sys.github.io/plasma-screensaver/

GitHub: https://github.com/subtiliorars-sys/plasma-screensaver
```

**r/hyprland**
```
Title: Native plasma screensaver for Hyprland — $9.99
Body:
Built a native Wayland screensaver that works with Hyprland out of the box.

Features:
- Plasma visual mode (smooth 30fps)
- Auto-activates on idle
- Hyprland window rules pre-configured
- systemd service for auto-start

Install: just clone and ./install.sh

https://subtiliorars-sys.github.io/plasma-screensaver/
```

**r/linux**
```
Title: Plasma Screensaver — native Wayland screensaver, open source, $9.99
Body:
After struggling with xscreensaver on Wayland, I built Plasma Screensaver from scratch. Native Wayland, smooth 30fps, idle detection, systemd service, Hyprland support.

$9.99 one-time payment via Stripe. Free updates forever.

https://subtiliorars-sys.github.io/plasma-screensaver/
```

### Hacker News — Show HN

```
Title: Show HN: Native Wayland screensaver for Hyprland/Sway — $9.99
Body:
I built Plasma Screensaver after years of xscreensaver not working on Wayland.

- Real-time plasma effect (sine wave math, bilinear upscaling for smooth 30fps)
- Native Wayland idle detection via pywayland
- Systemd user service for auto-start
- Hyprland window rules for fullscreen special workspace
- One-command installer
- MIT licensed

The $9.99 price covers Stripe fees and keeps me motivated to maintain it. If you're a student or can't afford it, just DM me — I'll send you a license.

https://subtiliorars-sys.github.io/plasma-screensaver/
GitHub: https://github.com/subtiliorars-sys/plasma-screensaver

Tech stack: Python 3.13, tkinter, pywayland, systemd, Hyprland IPC.
```

### Product Hunt

```
Tagline: Beautiful, native screensaver for Wayland compositors
Description:
Plasma Screensaver brings the classic plasma effect to Wayland. Native idle detection, smooth 30fps rendering, systemd auto-start, and Hyprland window rules — all in a single ./install.sh.

$9.99 one-time. Pay once, use forever.
```

### YouTube / PeerTube (60-second video)

```
Title: Install Plasma Screensaver on Hyprland in 30 seconds
Script:
[0:00] Show plasma effect fullscreen
[0:05] Terminal: git clone ...
[0:10] Terminal: ./install.sh
[0:15] Terminal: systemctl --user start plasma-screensaver
[0:20] Show it activating on idle
[0:25] Link to Stripe checkout
```

### Newsletters to Pitch

- Linux Unplugged (Podcast/Newsletter)
- This Week in Linux
- The Linux Experiment
- 9to5Linux
- OMG! Ubuntu

## Post-Launch

- [ ] Reply to every Reddit comment within 1 hour
- [ ] Monitor Stripe dashboard for first sales
- [ ] Track landing page analytics (GA/Plausible)
- [ ] Ask first buyers for testimonials
- [ ] Write a "How I built Plasma Screensaver" blog post
- [ ] Set up automated Twitter/Discord posts on sale (Stripe webhook)

## Future Platforms

- [ ] Gumroad — upload zip, add URL to landing page
- [ ] itch.io — create page, add URL to landing page
- [ ] Flathub — Flatpak package for easy install
- [ ] AUR — `plasma-screensaver` package for Arch users
- [ ] Coinbase Commerce — accept crypto
- [ ] PayPal — broader payment reach

---

*Last updated: 2026-09-19*
