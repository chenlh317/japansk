"""
Docstring for video_to_mp3

Run with command:
    python video_to_mp3.py

Loop video files in a given directory and convert them to mp3 files.

- Can specify start and end times for conversion if needed, for specific video files.
- Can handle multiple video formats, including mp4, avi, mov, mkv, flv, rmvb, wmv, webm.
- Can specify input directory containing video files.
- Output highest possible bitrate mp3 files.
- Saves the converted mp3 files in the same directory.

"""

from moviepy import VideoFileClip
from pathlib import Path
from typing import Dict, Optional, Tuple


def convert_videos_to_mp3(
    input_directory: Path,
    start_end_time_dict: Dict[Path, Tuple[Optional[float], Optional[float]]] = None,
):
    """
    Convert video files in the specified directory to mp3 format.

    Parameters:
    - input_directory (Path): Path to the directory containing video files.
    - start_end_time_dict (Dict[Path, Tuple[Optional[float], Optional[float]]], optional):
        A dictionary mapping video file paths to tuples of (start_time, end_time) in seconds.
        If provided, only the specified segment of the video will be converted.

    Returns:
    - None
    """
    video_extensions: set = {
        ".mp4",
        ".avi",
        ".mov",
        ".mkv",
        ".flv",
        ".rmvb",
        ".wmv",
        ".webm",
    }

    input_directory = Path(input_directory)

    for video_file in input_directory.iterdir():
        if video_file.suffix.lower() in video_extensions:
            print(f"Processing file: {video_file.name}")

            start_time: Optional[float] = None
            end_time: Optional[float] = None

            if start_end_time_dict and (video_file in start_end_time_dict):
                start_time, end_time = start_end_time_dict[video_file]

            with VideoFileClip(str(video_file)) as video_clip:
                if start_time is not None or end_time is not None:
                    video_clip = video_clip.subclipped(
                        start_time=start_time,
                        end_time=end_time,
                    )

                audio_clip = video_clip.audio
                output_mp3_path = video_file.with_suffix(".mp3")
                audio_clip.write_audiofile(
                    str(output_mp3_path),
                    bitrate="320k",
                )
                audio_clip.close()

            print(f"Converted to mp3: {output_mp3_path.name}")

    return None


if __name__ == "__main__":

    input_dir = Path("./raw_media")  # Specify your input directory here

    start_end_times: Dict[Path, Tuple[Optional[float], Optional[float]]] = {
        # Path("./raw_media/いつも何度でも／木村 弓.mp4"): (30, 90),  # Example entry
    }

    convert_videos_to_mp3(input_dir, start_end_times)
