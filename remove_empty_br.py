
"""
Remove redundant <br> in .md files.

Run with `python remove_empty_br.py`.

"""

import os

from pathlib import Path


def remove_empty_line_break(file_name):
    """
    Search for and remove redundant line breaks `<br>` and `<br>\n`.
    """

    lines = []

    msg = f"Found empty line break in {file_name}"

    # read in all lines of the file
    with open(file_name, "r") as f:
        lines = f.readlines()

    with open(file_name, "w") as f:

        # check redundant line breaks for each line
        for line in lines:

            if line == "<br>\n":
                print(msg)
                f.write("\n")
            elif line == "<br>":
                print(msg)
            else:
                f.write(line)


def process_all_files(root_dir, ext):
    """
    Loop all files and process.
    Filter by extensions.
    """

    for subdir, _, files in os.walk(root_dir):

        for file in files:

            if file.endswith(ext):

                remove_empty_line_break(os.path.join(subdir, file))


if __name__ == "__main__":

    root_dir = Path("lyrics")
    ext = (".md",)

    process_all_files(root_dir, ext)
