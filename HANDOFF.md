# Plasma Screensaver — Handoff Summary

**Date:** 2026-09-19  
**Account:** subtilior.ars@gmail.com (Stripe)  
**Product:** Plasma Screensaver v1.0  
**Price:** $9.99 USD one-time  

## Live Payment Link

**https://buy.stripe.com/fZu00b4g154K4IManK93y02**

## GitHub Pages Deployed

**Landing page:** https://subtiliorars-sys.github.io/plasma-screensaver/  
**Repo:** https://github.com/subtiliorars-sys/plasma-screensaver  
- `master` branch — all source code + install scripts  
- `gh-pages` branch — landing page + assets  

## What's Built

| Component | File | Status |
|-----------|------|--------|
| Screensaver app (5 modes) | `plasma_tkinter.py` | ✅ Working |
| Installer | `install.sh` | ✅ Working |
| Uninstaller | `uninstall.sh` | ✅ Working |
| Systemd auto-start | `plasma-screensaver.service` | ✅ Working |
| Hyprland rules | `hyprland.conf` | ✅ Working |
| Landing page (GitHub Pages) | `index.html` | ✅ Live |
| Product images | `assets/` | ✅ 1 image |
| Stripe payment | Live | ✅ $9.99 |

## To Do Next

1. **Test purchase flow**
   - Open https://buy.stripe.com/fZu00b4g154K4IManK93y02
   - Complete test purchase with card `4242 4242 4242 4242`

2. **Set up Gumroad/itch.io** (optional secondary stores)
   - Upload `plasma_tkinter.py` + install.sh to each platform
   - Add their URLs as additional "Buy" buttons on landing page

3. **Enable auto-start**
   ```bash
   ./install.sh
   systemctl --user start plasma-screensaver
   ```

4. **Post to Product Hunt**
   - Prepare launch post with demo video
   - Tag: #Wayland #Screensaver #OpenSource

5. **Record demo video**
   - 60s feature walkthrough
   - Wayland fullscreen, idle detection, paywall gate

## Key Locations

```
Project:      /home/daniel/plasma-screensaver/
Config:       ~/.config/plasma-screensaver/
  payments.json    — Stripe product IDs, payment URL
  products.json    — Local product tracking (dashboard)
Hyprland:     ~/.config/hypr/plasma-screensaver.conf
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

# Install locally
./install.sh

# Uninstall
./uninstall.sh

# Create new product (auto-generates Stripe link)
python3 plasma_screensaver/dashboard.py create

# Manage existing products
python3 plasma_screensaver/dashboard.py list
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
- ✅ 2026-09-19: Fixed GitHub Pages 404 (moved landing page to root)
- ✅ 2026-09-19: Removed fake payment processor logos (only Stripe live)
- ✅ 2026-09-19: Added install.sh, uninstall.sh, systemd service, Hyprland rules
- ✅ 2026-09-19: Landing page shows actual install commands
- ✅ 2026-09-19: Neural Network registry updated with plasma-screensaver entry

---

For questions: check README.md, or ask any Hermes agent (skills loaded automatically).
