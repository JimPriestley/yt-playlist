# yt-playlist

A simple Python command-line tool to download all videos from a YouTube playlist in the best available quality (audio and video merged as MP4) to a folder named after the playlist in your user's Public directory.

This example code is for eduactional purposes. Please respect YouTube Terms of Service and all applicable Copyright laws.

## Features
- Downloads all videos from a YouTube playlist
- Saves videos in the best available quality (video+audio merged to MP4)
- Output folder is automatically named after the playlist and created in your `~/Public` directory
- Handles playlist URLs and provides a default for debugging

## Requirements
- Python 3.7 or higher
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- ffmpeg (for merging video and audio into MP4)

## Installation
1. Clone or download this repository.
2. (Recommended) Create a virtual environment:
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install required Python packages:
   ```sh
   pip install yt-dlp
   ```
4. Install ffmpeg (if not already installed):
   - **macOS:**
     ```sh
     brew install ffmpeg
     ```
   - **Ubuntu/Debian:**
     ```sh
     sudo apt-get install ffmpeg
     ```
   - **Windows:** Download from [ffmpeg.org](https://ffmpeg.org/download.html)

## Usage
Run the script from the command line, passing a YouTube playlist URL as an argument:

```sh
python yt-playlist.py "https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID"
```

If no URL is provided, a default playlist will be used for debugging.

All downloaded videos will be saved as MP4 files in a folder named after the playlist, located in your `~/Public` directory.

## Example
```
python yt-playlist.py "https://www.youtube.com/playlist?list=PLj6YeMhvp2S4aIxuGH0NaGXQZlVUBsH3E"
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.
Please respect YouTube's Terms of Service and copyright laws when downloading content.
