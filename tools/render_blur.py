#!/usr/bin/env python3
"""Re-encode the Halo film with the tracked Customer column blurred.

Reads raw BGR frames on stdin, writes raw BGR frames on stdout.
Usage: ffmpeg ... -f rawvideo -pix_fmt bgr24 - | render_blur.py TRACK_JSON FIRST LAST | ffmpeg ...
"""
import json
import sys

import cv2
import numpy as np

W, H = 1920, 1080
track = json.load(open(sys.argv[1]))
first, last = int(sys.argv[2]), int(sys.argv[3])
size = W * H * 3
inp, out = sys.stdin.buffer, sys.stdout.buffer
n = 0
while True:
    buf = inp.read(size)
    if len(buf) < size:
        break
    if first <= n <= last and track.get(str(n), {}).get("poly"):
        f = np.frombuffer(buf, np.uint8).reshape(H, W, 3).copy()
        mask = np.zeros((H, W), np.uint8)
        cv2.fillPoly(mask, [np.int32(track[str(n)]["poly"])], 255)
        mask = cv2.dilate(mask, np.ones((25, 25), np.uint8))
        mask = cv2.GaussianBlur(mask, (31, 31), 0).astype(np.float32)[..., None] / 255.0
        # Pixelate then blur: unreadable at any zoom, still looks like soft UI.
        small = cv2.resize(f, (W // 24, H // 24), interpolation=cv2.INTER_AREA)
        heavy = cv2.GaussianBlur(cv2.resize(small, (W, H), interpolation=cv2.INTER_LINEAR), (0, 0), 6)
        f = (heavy * mask + f * (1 - mask)).astype(np.uint8)
        buf = f.tobytes()
    out.write(buf)
    n += 1
sys.stderr.write(f"frames: {n}\n")
