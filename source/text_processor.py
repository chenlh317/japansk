
from pathlib import Path


def remove_empty_br(file_name: Path):
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


def replace_special_char(file_name: Path):
    """
    Replace non-half-width characters with half-width.

    Args:
        file_name(Path): file to process
    Returns:
        None
    """

    lines = []

    # read in all lines of the file
    with open(file_name, "r") as f:
        lines = f.readlines()

    # char to replace
    char_replace_dict = {
        "　": " ",
    }

    with open(file_name, "w") as f:

        # check redundant line breaks for each line
        for _, line in enumerate(lines):

            for k, v in char_replace_dict.items():

                line = line.replace(k, v)

            f.write(line)

    return None
