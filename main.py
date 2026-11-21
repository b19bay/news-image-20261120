#!/usr/bin/env python3
"""Copy the bundled entry image to /output/entry.png.

Deterministic: the output is a byte-for-byte copy of entry.png, so two
runs always write identical bytes. Standard library only; no network.
The output directory defaults to /output and can be overridden with the
ENTRY_OUTPUT_DIR environment variable (used by the local test runs).
"""
import os
import sys

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
MAX_ENTRY_BYTES = 1_048_576  # 1 MiB cap on the entry image


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    return 1


def validate(src):
    """Return an error string if the entry image is unusable, else None."""
    if not os.path.isfile(src):
        return f"entry image not found: {src}"
    size = os.path.getsize(src)
    if size > MAX_ENTRY_BYTES:
        return f"entry image is {size} bytes, over the 1 MiB limit"
    with open(src, "rb") as f:
        head = f.read(len(PNG_SIGNATURE))
    if head != PNG_SIGNATURE:
        return "entry image does not start with the PNG signature"
    return None


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    problem = validate(src)
    if problem is not None:
        return fail(problem)
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
