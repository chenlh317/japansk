
"""
Batch text processor for .md files. E.g.

- Replace special characters.
- Remove redundant line break marks.

Run in terminal with `python process_text.py`.

"""

import os

from pathlib import Path

from source.text_processor import remove_empty_br, replace_special_char


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

                file_w_path = os.path.join(subdir, file)

                lines = []

                # read in all lines of the file
                with open(file_w_path, "r") as f:
                    
                    lines = f.readlines()

                with open(file_w_path, "w") as f:

                    for line_nr, line in enumerate(lines):

                        line = replace_special_char(line)

                        line = remove_empty_br(file_w_path, line_nr, line)

                        f.write(line)
    return None


if __name__ == "__main__":

    root_dir = Path("lyrics")
    ext = (".md",)

    process_all_files(root_dir, ext)
