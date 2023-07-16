import getpass
import os
from glob import glob

from clickgen.parser import open_blob
from clickgen.writer import to_x11
from typing import List
from pathlib import Path

def frames_to_cursor(frames_path: Path, output_path=Path("./test.ani")):
    # Get .png files from directory
    fnames = glob(f"{frames_path.absolute()}/*.png")
    pngs: List[bytes] = []

    # Reading as bytes
    for f in sorted(fnames):
        with open(f, "rb") as p:
            pngs.append(p.read())

    cur = open_blob(pngs, hotspot=(100, 100))

    # save X11 animated cursor
    result = to_x11(cur.frames)
    with open("animated-xtest", "wb") as o:
        o.write(result)

