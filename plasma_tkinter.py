#!/usr/bin/env python3
"""Terminal plasma effect — a little visual fun for a free session."""

import math
import os
import sys
import time
import tkinter as tk
from tkinter import ttk


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
        """Render plasma frame."""
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()
        if w < 10 or h < 10:
            return

        try:
            from PIL import Image, ImageTk
        except ImportError:
            self._render_canvas(w, h)
            return

        scale = 4
        rw, rh = w // scale, h // scale
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

    def _render_canvas(self, w, h):
        """Fallback rendering using canvas rectangles."""
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
    parser.add_argument("--mode", default="plasma")
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
