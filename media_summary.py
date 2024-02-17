"""
Summarize media info.

Run with `python media_summary.py`
"""

import os
from pathlib import Path

import eyed3
import pandas as pd

from mutagen.mp3 import MP3


def get_media_summary(media_folders: Path, output_name: str):
    """
    Get media esp. Mp3 info.

    Args:
        media_folders(Path): file path including all folders to check
        output_name(str): Excel file name
    Returns:
        None
    """

    # load folder paths
    with open(media_folders, "r") as f:
        folder_list = f.readlines()

    # initiate result df
    media_summary = pd.DataFrame({
        "Album": [],
        "Title": [],
        "bitrate": [],
    })

    # loop folders
    for folder_dir in folder_list:
        # remove "\n", or cannot parse the path
        folder_dir = folder_dir.replace("\n", "")
        print(folder_dir)

        # loop files
        for subdir, _, files in os.walk(folder_dir):
            for file in files:

                if file.endswith(".mp3"):
                    file_w_path = os.path.join(subdir, file)

                    # get bitrate in kbps
                    f_media = MP3(file_w_path)
                    bitrate = int(f_media.info.bitrate / 1000)

                    # get album info
                    f_audio = eyed3.load(file_w_path)
                    album_info = f_audio.tag.album

                    # append to result
                    media_summary.loc[len(media_summary.index)] = [
                        album_info,
                        file,
                        bitrate,
                    ]

    media_summary.to_excel(output_name)

    return None


if __name__ == "__main__":

    get_media_summary(
        "media_folders.txt",
        "Media_Summary.xlsx",
    )
