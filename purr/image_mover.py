import sys
import shutil
from pathlib import Path

with open("results-cut.txt", "r") as f:
    for line in f:
        filepath, label = line.split(":")
        filepath = Path(filepath.strip())
        if label.strip() == "cut":
            # move the file to the cut folder
            dest_folder = filepath.parent.joinpath("cut")
        else:
            # move the file to the uncut folder
            dest_folder = filepath.parent.joinpath("uncut")
        if not dest_folder.exists():
            dest_folder.mkdir()
        dest_folder = dest_folder.joinpath(filepath.name)
        print(f"Moving {filepath} to {dest_folder}")
        shutil.copy(filepath, dest_folder, follow_symlinks=True)
