#!/usr/bin/env python3
"""Sum 23 entrypoint: publish the bundled broadsheet image.

The repository ships the finished front page as entry.png. This program
copies it, byte for byte, into the harness output directory and checks
the SHA-256 of what it wrote, so a corrupt copy fails loudly instead
of silently entering a wrong image.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

EXPECTED_SHA256 = "ed361a4efd1a71f275c15e9e3f7e4605680979b3702eb9a5613b4da7c27c4ad9"
IMAGE_NAME = "entry.png"


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    here = Path(__file__).resolve().parent
    source = here / IMAGE_NAME
    if not source.is_file():
        print("error: bundled image not found: %s" % source, file=sys.stderr)
        return 1
    source_digest = sha256_of(source)
    if source_digest != EXPECTED_SHA256:
        print(
            "error: bundled image is corrupt: %s has sha256 %s"
            % (source, source_digest),
            file=sys.stderr,
        )
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / IMAGE_NAME
    shutil.copyfile(source, target)
    digest = sha256_of(target)
    if digest != EXPECTED_SHA256:
        print(
            "error: sha256 mismatch for %s: got %s" % (target, digest),
            file=sys.stderr,
        )
        return 1
    print("wrote %s sha256=%s" % (target, digest))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
