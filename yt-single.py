
import sys
import yt_dlp
import os
import re

def main():
    if len(sys.argv) == 2:
        video_url = sys.argv[1]
    else:
        # Default video URL for debugging
        video_url = "https://www.youtube.com/watch?v=reJpOCniWs8"
        print(f"No URL provided. Using default: {video_url}")

    # Extract video info to get the title
    ydl_opts_info = {
        'quiet': False,
        'skip_download': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts_info) as ydl:
        try:
            info = ydl.extract_info(video_url, download=False)
        except Exception as e:
            print(f"Failed to extract video info: {e}")
            sys.exit(1)
        title = info.get('title', 'video')
        # Sanitize file name
        title = re.sub(r'[^\w\- ]', '', title)

    # Set output path in ~/Public
    public_dir = os.path.expanduser('~/Public')
    os.makedirs(public_dir, exist_ok=True)
    output_path = os.path.join(public_dir, f"{title}.mp4")

    video_opts = {
        'quiet': False,
        'outtmpl': output_path,
        'noplaylist': True,
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4'
    }
    print(f"Downloading: {title}\nOutput: {output_path}")
    with yt_dlp.YoutubeDL(video_opts) as video_ydl:
        try:
            video_ydl.download([video_url])
        except Exception as e:
            print(f"Failed to download {title}: {e}")

if __name__ == "__main__":
    main()

