"""
Slices an audio file and exports the sliced segment.

Run by `python slice_mp3.py`

"""

from pathlib import Path

from pydub import AudioSegment


def slice_mp3_audio(
    song_path: Path,
    start_second: int,
    end_second: int,
) -> None:
    """
    Slices an audio file and exports the sliced segment.

    Args:
        song_path (Path): The path to the audio file.
        start_second (int): The start time in seconds.
        end_second (int): The end time in seconds.
    Returns:
        None
    """

    # Convert seconds to milliseconds
    k: int = 1000

    # read in, slice, and export the audio file
    song = AudioSegment.from_mp3(song_path)
    new_song = song[start_second * k: end_second * k]
    new_song.export(
        f"{song_path.stem}_{start_second}_{end_second}.mp3",
        format="mp3",
    )

    return None


if __name__ == "__main__":
    slice_mp3_audio(
        song_path=Path("hiromi.mp3"),
        start_second=586,
        end_second=701,
    )
