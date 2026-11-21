#!/usr/bin/env python3
"""Copy the bundled entry image to /output/entry.png.

Deterministic: the output is a byte-for-byte copy of entry.png, so two
runs always write identical bytes. Standard library only; no network.
The output directory defaults to /output and can be overridden with the
ENTRY_OUTPUT_DIR environment variable (used by the local test runs).
"""
import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    outdir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    dst = os.path.join(outdir, "entry.png")
    with open(src, "rb") as f:
        data = f.read()
    with open(dst, "wb") as f:
        f.write(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
