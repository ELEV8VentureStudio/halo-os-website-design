#!/usr/bin/env python3
"""Track the Service Management screen in the Halo film and blur the Customer column.

The screen is a flat plane under perspective, so each frame is matched to a
reference frame with ORB features + a RANSAC homography, and the Customer
column polygon (defined once on the reference) is mapped into every frame.

Usage: track_blur.py FRAMES_DIR FIRST LAST OUT_JSON
"""
import json
import sys

import cv2
import numpy as np

REF = 1200  # 40.0s
# Customer column on the reference frame (full-res px), extended well below the
# frame edge so rows that scroll into view on other frames are covered too.
POLY = np.float32([[540, 640], [790, 615], [800, 1700], [545, 1720]])

frames_dir, first, last, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
orb = cv2.ORB_create(6000)
ref = cv2.imread(f"{frames_dir}/{REF:05d}.png", cv2.IMREAD_GRAYSCALE)
kr, dr = orb.detectAndCompute(ref, None)
bf = cv2.BFMatcher(cv2.NORM_HAMMING)
res = {}
for n in range(first, last + 1):
    img = cv2.imread(f"{frames_dir}/{n:05d}.png", cv2.IMREAD_GRAYSCALE)
    k, d = orb.detectAndCompute(img, None)
    if d is None:
        res[n] = None
        continue
    good = [m for m, m2 in bf.knnMatch(dr, d, k=2) if m.distance < 0.75 * m2.distance]
    if len(good) < 25:
        res[n] = {"inliers": len(good), "poly": None}
        continue
    src = np.float32([kr[m.queryIdx].pt for m in good])
    dst = np.float32([k[m.trainIdx].pt for m in good])
    H, mask = cv2.findHomography(src, dst, cv2.RANSAC, 4.0)
    inl = int(mask.sum()) if mask is not None else 0
    poly = cv2.perspectiveTransform(POLY.reshape(-1, 1, 2), H).reshape(-1, 2).tolist() if H is not None else None
    res[n] = {"inliers": inl, "poly": poly}
json.dump(res, open(out, "w"))
for n, r in res.items():
    print(n, r and r["inliers"])
