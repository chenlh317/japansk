"""
Download YouTube videos listed in a YAML file using yt-dlp.

Usage:
    1. Edit yaml_file and output in the __main__ block below.
    2. Run: python download_videos.py
"""

import subprocess
import yaml

from pathlib import Path


def clean_url(url: str) -> str:
    """Strip &list=... and everything after it from the URL."""
    idx: int = url.find("&list=")
    if idx != -1:
        url = url[:idx]
    return url


def download_videos(yaml_path: str, output_path: str) -> None:
    """
    Download all YouTube videos listed in a YAML file.

    Args:
        yaml_path: Path to the YAML file containing a 'videos' list of URLs.
        output_path: Directory where downloaded videos will be saved.
    """
    path: Path = Path(yaml_path)
    if not path.exists():
        print(f"Error: YAML file not found: {yaml_path}")
        return

    with open(path, "r", encoding="utf-8") as f:
        data: dict = yaml.safe_load(f)

    urls: list[str] = data.get("videos", [])
    if not urls:
        print("No videos found in YAML file.")
        return

    output_dir: Path = Path(output_path)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_template: str = str(output_dir / "%(title)s.%(ext)s")

    for url in urls:
        url = clean_url(url)
        print(f"\nDownloading: {url}")
        cmd: list[str] = [
            "yt-dlp",
            "-f", "bestvideo+bestaudio",
            "--merge-output-format", "mp4",
            "-o", output_template,
            url,
        ]
        subprocess.run(cmd)


if __name__ == "__main__":

    yaml_file: str = "videos.yaml"
    output: str = "./downloads"

    download_videos(yaml_file, output)
