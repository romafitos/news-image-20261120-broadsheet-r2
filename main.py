"""news-image-20261120 broadsheet r2 entrypoint.

Copies the pre-rendered front page (entry.png, in this repository) to the
output directory. Deterministic: byte-for-byte copy, no network, no time.
"""
import os
import shutil


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    shutil.copyfile(src, os.path.join(out, "entry.png"))


if __name__ == "__main__":
    main()
