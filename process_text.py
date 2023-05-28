
"""
Remove redundant <br> in .md files.

Run in terminal with `python process_text.py`.

"""

import os

from pathlib import Path

from source.text_processor import remove_empty_br, replace_special_characters


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
                
                remove_empty_br(file_w_path)

                replace_special_characters(file_w_path)

    return None


if __name__ == "__main__":

    root_dir = Path("lyrics")
    ext = (".md",)

    process_all_files(root_dir, ext)
