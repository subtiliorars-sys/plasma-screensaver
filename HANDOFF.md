# Plasma Screensaver — Handoff Summary

**Date:** 2026-09-09  
**Account:** subtilior.ars@gmail.com (Stripe)  
**Product:** Plasma Screensaver v1.0  
**Price:** $9.99 USD one-time  

## Live Payment Link

**https://buy.stripe.com/fZu00b4g154K4IManK93y02**

## GitHub Pages Deployed

**Landing page:** https://subtiliorars-sys.github.io/plasma-screensaver/  
**Repo:** https://github.com/subtiliorars-sys/plasma-screensaver  
- `master` branch — all source code  
- `gh-pages` branch — landing page + assets  

## What's Built

| Component | File | Status |
|-----------|------|--------|
| Screensaver app (5 modes) | `plasma_tkinter.py` | ✅ Working |
| Cairo rendering engine | `plasma_screensaver/renderer.py` | ✅ Working |
| Product dashboard | `plasma_screensaver/dashboard.py` | ✅ Working |
| Payment router (8 processors) | `plasma_screensaver/payments.py` | ✅ Working |
| API key setup wizard | `plasma_screensaver/setup_payments.py` | ✅ Working |
| Landing page (GitHub Pages) | `landing/index.html` | ✅ Live |
| Product images | `landing/assets/` | ✅ 6 images |
| Systemd auto-start | `plasma-screensaver.service` | ✅ Written |
| Installer | `install.sh` | ✅ Working |
| Uninstaller | `uninstall.sh` | ✅ Working |
| Hyprland rules | `~/.config/hypr/hyprland.lua` | ✅ Active |

## To Do Next

1. **Test purchase flow**
   - Open https://buy.stripe.com/fZu00b4g154K4IManK93y02
   - Complete test purchase with card `4242 4242 4242 4242`

2. **Set up Gumroad/itch.io** (see DEPLOY.md for exact steps)
   - Upload `dist/plasma-screensaver.zip` to each platform
   - Add their URLs as additional "Buy" buttons on landing page

3. **Enable auto-start**
   ```bash
   cp plasma-screensaver/plasma-screensaver.service ~/.config/systemd/user/
   systemctl --user daemon-reload
   systemctl --user enable plasma-screensaver
   ```

## Key Locations

```
Project:      /home/daniel/plasma-screensaver/
Config:       ~/.config/plasma-screensaver/
  payments.json    — Stripe product IDs, payment URL
  products.json    — Local product tracking (dashboard)
Hyprland:     ~/.config/hypr/hyprland.lua
Skills:       ~/.hermes/skills/
  plasma-screensaver   — Full project reference
  stripe-payments      — Reusable Stripe patterns
  hyprland-patterns    — Window rules, systemd, GUI
```

## Environment Variables

```bash
# Required for dashboard.py
export STRIPE_SECRET_KEY=sk_liv...g4as...

# Required for screensaver (Hyprland sets these)
export DISPLAY=:0
export WAYPR_DISPLAY=wayland-1
```

## Quick Commands

```bash
# Run screensaver
python3 plasma_tkinter.py --no-idle --mode plasma

# Create new product (auto-generates Stripe link)
python3 plasma_screensaver/dashboard.py create

# Manage existing products
python3 plasma_screensaver/dashboard.py list

# Install locally
./install.sh
```

## Payment Processor Status

| Processor | Status | Action Needed |
|-----------|--------|---------------|
| Stripe | ✅ Live | None — $9.99 product active |
| Gumroad | ❌ Setup | Sign up, create product |
| itch.io | ❌ Setup | Sign up, create page |
| Coinbase | ❌ Setup | API keys |
| Kraken | ❌ Setup | API keys |
| Paymentcloud | ❌ Setup | Apply (3-7 days) |
| Kurv | ❌ Research | Verify platform |
| BYDFI | ❌ Setup | API keys |

## Verification History

- ✅ 2026-09-09: Renderer produces valid surfaces for all 5 modes
- ✅ 2026-09-09: GTK4 window stays mapped and visible in Hyprland
- ✅ 2026-09-09: Tkinter plasma renders fullscreen at 1920x1080
- ✅ 2026-09-09: Hyprland window rules apply (fullscreen, special workspace, no focus)
- ✅ 2026-09-12: Landing page deployed to GitHub Pages (gh-pages branch)
- ✅ 2026-09-12: Source code pushed to master branch
- ✅ 2026-09-12: CNAME configured (plasma-screensaver.netlify.app)

---

For questions: check DEPLOY.md, CHECKLIST.md, or ask any Hermes agent (skills loaded automatically).
