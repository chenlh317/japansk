
"""
Remove redundant <br> in .md files.

Run in terminal with `python remove_empty_br.py`.

"""

import os

from pathlib import Path


def remove_empty_line_break(file_name: Path):
    """
    Search for and remove redundant line breaks `<br>` and `<br>\n`.

    Args:
        file_name(Path): file to process
    Returns:
        None
    """

    lines = []

    # read in all lines of the file
    with open(file_name, "r") as f:
        lines = f.readlines()

    with open(file_name, "w") as f:

        # check redundant line breaks for each line
        for line_nr, line in enumerate(lines):

            msg = f"Removed empty line break in {file_name}: Line {line_nr}"

            # removed <br> if that's the only thing in the line
            if line == "<br>\n":
                print(msg)
                f.write("\n")
            elif line == "<br>":
                print(msg)
            else:
                f.write(line)

    return None


def process_all_files(root_dir: Path, ext: tuple):
    """
    Loop all files and process.
    Filter by extensions.

    Args:
        root_dir(Path): directory to search
        ext(tuple): tuple of file extensions to include in the search
    Returns:
        None
    """

    for subdir, _, files in os.walk(root_dir):

        for file in files:

            if file.endswith(ext):

                remove_empty_line_break(os.path.join(subdir, file))

    return None


if __name__ == "__main__":

    root_dir = Path("lyrics")
    ext = (".md",)

    process_all_files(root_dir, ext)
