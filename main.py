#!/usr/bin/env python3
"""Sum 23 R2 entry runner (standard library only).

Copies the shipped entry.png to the output entry.png byte-for-byte and
verifies the copy's SHA-256 against the hash baked into this program.
The output directory comes from MAKEFUN_OUTPUT_DIR, falling back to
/output when that variable is absent. Exits non-zero on any mismatch.
"""

import hashlib
import os
import shutil
import sys

EXPECTED_SHA256 = "07e8de569d3e0bae523957c6b8afafd0a92021c4d23e8cb0207447849cae70e4"
# Hash of the rendered repo-r2b/entry.png (1024x1024, 202654 bytes).
# If the image is re-rendered, this value must be updated to match.


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    digest = hashlib.sha256(open(dst, "rb").read()).hexdigest()
    if digest != EXPECTED_SHA256:
        print("hash mismatch: got %s, expected %s" % (digest, EXPECTED_SHA256),
              file=sys.stderr)
        return 1
    print("wrote %s sha256=%s" % (dst, digest))
    return 0


if __name__ == "__main__":
    sys.exit(main())
