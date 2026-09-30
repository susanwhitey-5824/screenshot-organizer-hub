#!/usr/bin/env python3
"""Pindahkan screenshot ke folder per tanggal (dari modified time)."""
import os, shutil, datetime, sys
src = sys.argv[1] if len(sys.argv) > 1 else "."
for name in os.listdir(src):
      p = os.path.join(src, name)
      if not os.path.isfile(p): continue
            d = datetime.datetime.fromtimestamp(os.path.getmtime(p)).strftime("%Y-%m-%d")
    dst = os.path.join(src, d); os.makedirs(dst, exist_ok=True)
    shutil.move(p, os.path.join(dst, name))
    print(name, "->", d + "/")
