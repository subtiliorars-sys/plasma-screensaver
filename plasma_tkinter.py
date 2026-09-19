#!/usr/bin/env python3
"""Terminal plasma effect — a little visual fun for a free session."""

import math
import os
import random
import sys
import time
import tkinter as tk


class PlasmaScreensaver:
    """Main screensaver application using tkinter."""

    def __init__(self, mode="plasma", fps=30, idle_timeout=300, root=None):
        self.mode = mode
        self.fps = fps
        self.idle_timeout = idle_timeout
        self.root = root or tk.Tk()
        self.root.title("plasma-screensaver")
        self.root.configure(bg="black")
        self.root.attributes("-topmost", True)
        self.root.bind("<Key>", self.exit)
        self.root.bind("<Motion>", self.exit)
        self.root.bind("<Button>", self.exit)
        self.root.bind("<Escape>", self.exit)

        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_w}x{screen_h}+0+0")
        self.root.overrideredirect(True)

        self.canvas = tk.Canvas(self.root, bg="black", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.time = 0
        self._running = True
        self._last_activity = time.monotonic()
        self._idle_check_interval = 1000

        # Pre-compute character set for matrix mode
        self._matrix_chars = "ﾊﾐﾋｰｳｼﾅﾓﾆｻﾜﾂｵﾘｱﾎﾃﾏｹﾒｴｶｷﾑﾕﾗｾﾈｽﾀﾇﾍ012345789Z:.=\"*+-<>¦|_"

    def run(self):
        """Start the screensaver."""
        self.root.withdraw()
        self._check_idle()
        self.root.mainloop()

    def _check_idle(self):
        """Check if idle timeout reached."""
        if not self._running:
            return
        elapsed = time.monotonic() - self._last_activity
        if elapsed >= self.idle_timeout:
            self._show_plasma()
        else:
            self.root.after(self._idle_check_interval, self._check_idle)

    def _show_plasma(self):
        """Show fullscreen plasma."""
        self.root.deiconify()
        self._animate()

    def _animate(self):
        """Animation loop."""
        if not self._running:
            return
        self.time += 0.033
        self._render()
        delay = max(16, 1000 // self.fps)
        self.root.after(delay, self._animate)

    def _render(self):
        """Render current frame based on selected mode."""
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()
        if w < 10 or h < 10:
            return

        try:
            from PIL import Image, ImageTk
            use_pil = True
        except ImportError:
            use_pil = False

        if self.mode == "plasma":
            self._render_plasma(w, h, use_pil)
        elif self.mode == "fire":
            self._render_fire(w, h, use_pil)
        elif self.mode == "matrix":
            self._render_matrix(w, h)
        elif self.mode == "waves":
            self._render_waves(w, h, use_pil)
        elif self.mode == "kaleidoscope":
            self._render_kaleidoscope(w, h, use_pil)
        else:
            self._render_plasma(w, h, use_pil)

    def _render_plasma(self, w, h, use_pil):
        """Classic plasma - overlapping sine waves with HSV cycling."""
        if use_pil:
            scale = 4
            rw, rh = w // scale, h // scale
            try:
                import numpy as np
                img = Image.new("RGB", (rw, rh))
                pixels = img.load()
                t = self.time
                for y in range(rh):
                    ny = y / rh
                    for x in range(rw):
                        nx = x / rw
                        v1 = math.sin(nx * 10 + t)
                        v2 = math.sin(ny * 8 + t * 0.7)
                        v3 = math.sin((nx + ny) * 6 + t * 1.3)
                        v4 = math.sin(math.sqrt(((nx-0.5)**2 + (ny-0.5)**2) * 50) + t * 0.5)
                        v = (v1 + v2 + v3 + v4) / 4
                        v = (v + 1) / 2
                        hue = (v * 360 + t * 30) % 360
                        r, g, b = self._hsv_to_rgb(hue, 0.85, 0.95)
                        pixels[x, y] = (r, g, b)
                img = img.resize((w, h), Image.BILINEAR)
                self._photo = ImageTk.PhotoImage(img)
                self.canvas.create_image(0, 0, anchor=tk.NW, image=self._photo)
            except ImportError:
                self._render_plasma_canvas(w, h)
        else:
            self._render_plasma_canvas(w, h)

    def _render_fire(self, w, h, use_pil):
        """Rising flames with turbulence and ember flicker."""
        if use_pil:
            try:
                import numpy as np
                scale = 4
                rw, rh = w // scale, h // scale
                img = Image.new("RGB", (rw, rh))
                pixels = img.load()
                t = self.time

                if not hasattr(self, '_fire_buffer'):
                    self._fire_buffer = [[0.0] * rw for _ in range(rh)]

                buf = self._fire_buffer

                # Set bottom row to hot values
                for x in range(rw):
                    buf[rh-1][x] = random.uniform(0.7, 1.0)

                # Propagate fire upward with cooling
                for y in range(rh - 2, -1, -1):
                    for x in range(rw):
                        # Sample below with some spread
                        below = buf[y+1][x]
                        left = buf[y+1][x-1] if x > 0 else below
                        right = buf[y+1][x+1] if x < rw-1 else below
                        below2 = buf[y+2][x] if y < rh-2 else 0

                        val = (below + left + right + below2) / 4.0
                        val -= random.uniform(0.01, 0.05)
                        buf[y][x] = max(0, val)

                # Render fire colors
                for y in range(rh):
                    for x in range(rw):
                        v = buf[y][x]
                        if v < 0.15:
                            r, g, b = 0, 0, 0
                        elif v < 0.3:
                            r, g, b = int(v * 5 * 255), 0, 0
                        elif v < 0.6:
                            r, g = 255, int((v - 0.3) * 5 * 255)
                            b = 0
                        elif v < 0.8:
                            r, g = 255, 255
                            b = int((v - 0.6) * 3 * 255)
                        else:
                            r, g, b = 255, 255, min(255, int((v - 0.8) * 5 * 255))
                        pixels[x, y] = (r, g, b)

                img = img.resize((w, h), Image.BILINEAR)
                self._photo = ImageTk.PhotoImage(img)
                self.canvas.create_image(0, 0, anchor=tk.NW, image=self._photo)
            except ImportError:
                self._render_fire_canvas(w, h)
        else:
            self._render_fire_canvas(w, h)

    def _render_matrix(self, w, h):
        """Falling green code with phosphor glow trails."""
        self.canvas.delete("all")
        char_w = 14
        char_h = 18
        cols = w // char_w
        t = self.time

        if not hasattr(self, '_matrix_drops'):
            self._matrix_drops = []
            for c in range(cols):
                if random.random() < 0.3:
                    self._matrix_drops.append({
                        'col': c,
                        'y': random.randint(-50, 0),
                        'speed': random.uniform(0.3, 1.5),
                        'length': random.randint(8, 25),
                        'chars': [random.choice(self._matrix_chars) for _ in range(30)]
                    })

        drops = self._matrix_drops

        for drop in drops:
            drop['y'] += drop['speed']
            # Reset when off screen
            if drop['y'] - drop['length'] > h // char_h:
                drop['y'] = random.randint(-30, 0)
                drop['speed'] = random.uniform(0.3, 1.5)
                drop['length'] = random.randint(8, 25)
                drop['chars'] = [random.choice(self._matrix_chars) for _ in range(30)]

            cx = drop['col'] * char_w
            for i in range(drop['length']):
                cy = int((drop['y'] - i) * char_h)
                if cy < 0 or cy > h - char_h:
                    continue
                intensity = max(0, 255 - int(i * 255 / drop['length']))
                if intensity > 200:
                    color = "#ffffff"
                elif intensity > 100:
                    color = f"#{intensity:02x}ff{intensity:02x}"
                else:
                    color = f"#00{intensity:02x}00"

                # Occasionally mutate characters
                if random.random() < 0.02:
                    drop['chars'][i % len(drop['chars'])] = random.choice(self._matrix_chars)
                ch = drop['chars'][i % len(drop['chars'])]
                self.canvas.create_text(cx, cy, text=ch, fill=color, font=("JetBrains Mono", 12))

    def _render_waves(self, w, h, use_pil):
        """Ocean waves with foam and depth gradient."""
        if use_pil:
            try:
                import numpy as np
                scale = 4
                rw, rh = w // scale, h // scale
                img = Image.new("RGB", (rw, rh))
                pixels = img.load()
                t = self.time

                for y in range(rh):
                    ny = y / rh
                    for x in range(rw):
                        nx = x / rw
                        # Multiple wave layers
                        wave1 = math.sin(nx * 8 + t * 0.8) * 0.3
                        wave2 = math.sin(nx * 12 - t * 0.6) * 0.2
                        wave3 = math.sin(nx * 20 + t * 1.2) * 0.1
                        wave_y = ny + wave1 + wave2 + wave3

                        # Depth-based coloring
                        depth = wave_y
                        if depth < 0.4:
                            # Deep water - dark blue
                            r, g, b = 0, int(20 + depth * 60), int(80 + depth * 150)
                        elif depth < 0.7:
                            # Mid water - teal
                            r, g, b = 0, int(80 + depth * 100), int(150 + depth * 100)
                        else:
                            # Surface/foam - light
                            foam = max(0, min(1, (depth - 0.7) * 3))
                            foam_intensity = int(foam * 255 * (0.7 + 0.3 * math.sin(nx * 30 + t * 2)))
                            r, g, b = foam_intensity, min(255, 180 + foam_intensity // 2), min(255, 200 + foam_intensity // 3)

                        pixels[x, y] = (r, g, b)

                img = img.resize((w, h), Image.BILINEAR)
                self._photo = ImageTk.PhotoImage(img)
                self.canvas.create_image(0, 0, anchor=tk.NW, image=self._photo)
            except ImportError:
                self._render_waves_canvas(w, h)
        else:
            self._render_waves_canvas(w, h)

    def _render_kaleidoscope(self, w, h, use_pil):
        """6-fold mirrored symmetry with polar plasma."""
        if use_pil:
            try:
                import numpy as np
                scale = 4
                rw, rh = w // scale, h // scale
                img = Image.new("RGB", (rw, rh))
                pixels = img.load()
                t = self.time

                cx, cy = rw // 2, rh // 2
                sectors = 6

                for y in range(rh):
                    for x in range(rw):
                        dx, dy = x - cx, y - cy
                        angle = math.atan2(dy, dx)
                        dist = math.sqrt(dx * dx + dy * dy)

                        # Fold angle into sector
                        sector_angle = (2 * math.pi) / sectors
                        folded = abs((angle % sector_angle) - sector_angle / 2)

                        # Polar plasma
                        v = (math.sin(dist * 0.1 + t * 0.5) +
                             math.sin(folded * 3 + t * 0.3) +
                             math.cos(dist * 0.05 - folded * 2 + t * 0.7) +
                             math.sin(folded * 6 + dist * 0.15 + t))
                        v = (v / 4 + 1) / 2

                        hue = (v * 360 + t * 20 + dist * 2) % 360
                        r, g, b = self._hsv_to_rgb(hue, 0.9, 0.9)
                        pixels[x, y] = (r, g, b)

                img = img.resize((w, h), Image.BILINEAR)
                self._photo = ImageTk.PhotoImage(img)
                self.canvas.create_image(0, 0, anchor=tk.NW, image=self._photo)
            except ImportError:
                self._render_kaleidoscope_canvas(w, h)
        else:
            self._render_kaleidoscope_canvas(w, h)

    def _render_plasma_canvas(self, w, h):
        """Fallback canvas rendering for plasma."""
        self.canvas.delete("all")
        t = self.time
        step = 20
        for y in range(0, h, step):
            ny = y / h
            for x in range(0, w, step):
                nx = x / w
                v = (math.sin(nx * 10 + t) + math.sin(ny * 8 + t * 0.7)) / 2
                v = (v + 1) / 2
                r = int(128 + 127 * math.sin(v * 3.14))
                g = int(128 + 127 * math.sin(v * 3.14 + 2))
                b = int(128 + 127 * math.sin(v * 3.14 + 4))
                color = f"#{r:02x}{g:02x}{b:02x}"
                self.canvas.create_rectangle(x, y, x+step, y+step, fill=color, outline="")

    def _render_fire_canvas(self, w, h):
        """Fallback canvas rendering for fire."""
        self.canvas.delete("all")
        step = 20
        t = self.time
        for y in range(0, h, step):
            ny = y / h
            for x in range(0, w, step):
                nx = x / w
                intensity = max(0, min(1, 1.0 - ny + 0.3 * math.sin(nx * 5 + t * 3) * math.sin(t * 2 + nx)))
                r = min(255, int(intensity * 255 * 1.5))
                g = min(255, int(intensity * intensity * 255))
                b = int(intensity * intensity * intensity * 255 * 0.5)
                color = f"#{min(255,r):02x}{min(255,g):02x}{min(255,b):02x}"
                self.canvas.create_rectangle(x, y, x+step, y+step, fill=color, outline="")

    def _render_waves_canvas(self, w, h):
        """Fallback canvas rendering for waves."""
        self.canvas.delete("all")
        t = self.time
        step = 20
        for y in range(0, h, step):
            ny = y / h
            for x in range(0, w, step):
                nx = x / w
                wave = math.sin(nx * 8 + t * 0.8) * 0.3
                depth = ny + wave
                if depth < 0.4:
                    r, g, b = 0, 30, 80
                elif depth < 0.7:
                    r, g, b = 0, 100, 160
                else:
                    foam = max(0, min(255, int((depth - 0.7) * 3 * 200)))
                    r, g, b = foam, 200, 220
                color = f"#{r:02x}{g:02x}{b:02x}"
                self.canvas.create_rectangle(x, y, x+step, y+step, fill=color, outline="")

    def _render_kaleidoscope_canvas(self, w, h):
        """Fallback canvas rendering for kaleidoscope."""
        self.canvas.delete("all")
        t = self.time
        step = 20
        cx, cy = w // 2, h // 2
        for y in range(0, h, step):
            for x in range(0, w, step):
                dx, dy = x - cx, y - cy
                angle = math.atan2(dy, dx)
                dist = math.sqrt(dx * dx + dy * dy)
                folded = abs((angle % (math.pi / 3)) - (math.pi / 6))
                v = (math.sin(dist * 0.1 + t) + math.sin(folded * 3 + t * 0.5)) / 2
                v = (v + 1) / 2
                r = min(255, int(v * 255 * 0.8))
                g = min(255, int((1 - v) * 255 * 0.6))
                b = min(255, int(v * 255))
                color = f"#{r:02x}{g:02x}{b:02x}"
                self.canvas.create_rectangle(x, y, x+step, y+step, fill=color, outline="")

    def _hsv_to_rgb(self, h, s, v):
        """HSV to RGB."""
        c = v * s
        x = c * (1 - abs((h / 60) % 2 - 1))
        m = v - c
        if h < 60: r, g, b = c, x, 0
        elif h < 120: r, g, b = x, c, 0
        elif h < 180: r, g, b = 0, c, x
        elif h < 240: r, g, b = 0, x, c
        elif h < 300: r, g, b = x, 0, c
        else: r, g, b = c, 0, x
        return (int((r+m)*255), int((g+m)*255), int((b+m)*255))

    def exit(self, event=None):
        """Exit screensaver."""
        self._running = False
        self.root.destroy()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", default="plasma", choices=["plasma", "fire", "matrix", "waves", "kaleidoscope"])
    parser.add_argument("--fps", type=int, default=30)
    parser.add_argument("--idle-timeout", type=int, default=300)
    parser.add_argument("--no-idle", action="store_true")
    args = parser.parse_args()

    app = PlasmaScreensaver(
        mode=args.mode,
        fps=args.fps,
        idle_timeout=10 if args.no_idle else args.idle_timeout,
    )
    if args.no_idle:
        app._last_activity = time.monotonic() - args.idle_timeout - 1
    app.run()
