import getpass
import os
from glob import glob
import shutil

from clickgen.parser import open_blob
from clickgen.writer import to_win, to_x11

from typing import List
from pathlib import Path

def frames_to_cursor(frames_path: Path, output_path=Path("cursor_temp")) -> Path:
    """ Create x11 cursor at output_path from frames in frames_path. Returns output_path """

    # Clickgen does not export working animations at time of writing!!!
    
    fnames = glob(f"{frames_path.absolute()}/*.png")
    pngs: List[bytes] = []

    # Reading as bytes
    for f in sorted(fnames):
        with open(f, "rb") as p:
            print(f"Appending file {f} to cursor")
            pngs.append(p.read())

    cur = open_blob(pngs, hotspot=(0, 0))

    # save X11 animated cursor
    result = to_x11(cur.frames)
    with open(output_path, "wb") as o:
        o.write(result)

    return output_path

