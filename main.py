"""Entry program for make.fun news-image-20261119 (Python 3.13, stdlib only).

The finished front page, entry.png, sits beside this file. The program
copies it to /output/entry.png (or $MAKEFUN_OUTPUT_DIR when set) and
checks the copy byte-for-byte against the source. The image is a static
asset: no network access, and every run writes identical bytes.

Before copying, the program also verifies the entry itself: a whole JPEG
or PNG, at most 1 MiB, and exactly 1024 by 1024 pixels.
"""

import hashlib
import os
import shutil
import struct
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
MAX_BYTES = 1_048_576
MAGIC = (b"\xff\xd8\xff", b"\x89PNG\r\n\x1a\n")  # JPEG, PNG
WANT_W, WANT_H = 1024, 1024


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        while True:
            chunk = handle.read(1 << 20)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def jpeg_dimensions(data):
    """Read width and height out of a JPEG's first SOF segment."""
    pos = 2
    while pos + 9 < len(data):
        if data[pos] != 0xFF:
            raise SystemExit("malformed JPEG: bad marker")
        marker = data[pos + 1]
        if marker in (0xC0, 0xC1, 0xC2):  # SOF0/1/2
            height, width = struct.unpack(">HH", data[pos + 5:pos + 9])
            return width, height
        size = struct.unpack(">H", data[pos + 2:pos + 4])[0]
        pos += 2 + size
    raise SystemExit("malformed JPEG: no SOF segment found")


def png_dimensions(data):
    """Read width and height out of a PNG's IHDR chunk."""
    if len(data) < 24 or data[12:16] != b"IHDR":
        raise SystemExit("malformed PNG: no IHDR chunk")
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def check_image(path):
    """Gate checks the entry must pass: a whole JPEG or PNG, at most
    1 MiB, and exactly 1024 by 1024 pixels."""
    data = path.read_bytes()
    if data.startswith(MAGIC[0]):
        width, height = jpeg_dimensions(data)
    elif data.startswith(MAGIC[1]):
        width, height = png_dimensions(data)
    else:
        raise SystemExit(f"{path} is neither a JPEG nor a PNG")
    if path.stat().st_size > MAX_BYTES:
        raise SystemExit(f"{path} is over the 1 MiB limit")
    if (width, height) != (WANT_W, WANT_H):
        raise SystemExit(f"{path} is {width}x{height}, not 1024x1024")


def main():
    if not SOURCE.is_file():
        print(f"entry.png not found beside main.py: {SOURCE}", file=sys.stderr)
        raise SystemExit(1)
    check_image(SOURCE)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    target = OUTPUT_DIR / "entry.png"
    shutil.copyfile(SOURCE, target)
    if sha256_of(SOURCE) != sha256_of(target):
        print("copied entry.png does not match the source", file=sys.stderr)
        raise SystemExit(1)
    print(f"wrote {target} ({target.stat().st_size} bytes, "
          f"sha256 {sha256_of(target)})")


if __name__ == "__main__":
    main()
