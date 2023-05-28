"""
Text processors.
"""

from pathlib import Path


def replace_special_char(line: str) -> str:
    """
    Replace full-width characters with half-width,
    as well as other special characters.

    Args:
        line(str): line to process
    Returns:
        str
    """

    # char to replace
    char_replace_dict = {
        "　": " ",
        "（": "(",
        "）": ")",
    }

    for k, v in char_replace_dict.items():

        line = line.replace(k, v)

    return line


def remove_empty_br(
    file_w_path: Path,
    line_nr: int,
    line: str,
) -> str:
    """
    Search for and remove redundant line break
    marks `<br>` and `<br>\n`.

    Args:
        file_w_path(Path): file to process
        line_nr(int):
        line(str): line to process
    Returns:
        str
    """

    msg = f"Removed empty line break marks in {file_w_path}: Line {line_nr}"

    # remove <br> if that's the only thing in the line
    if line in ("<br>\n", "<br>"):
        print(msg)
        line = line.replace("<br>", "")
        return line
    else:
        return line
