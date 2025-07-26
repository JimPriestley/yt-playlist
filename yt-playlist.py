
import sys
import yt_dlp
import os
import re

def main():
    if len(sys.argv) == 2:
        playlist_url = sys.argv[1]
    else:
        # Default playlist URL for debugging
        playlist_url = "https://www.youtube.com/playlist?list=PLj6YeMhvp2S4aIxuGH0NaGXQZlVUBsH3E"
        print(f"No URL provided. Using default: {playlist_url}")
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'skip_download': True,
    }
    # Extract playlist info
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(playlist_url, download=False)
        if 'entries' not in info:
            print("No videos found in playlist.")
            sys.exit(1)
        # Get playlist title for folder name, fallback to playlist ID
        playlist_title = info.get('title') or info.get('id', 'playlist')
        # Sanitize folder name (remove problematic characters)
        playlist_title = re.sub(r'[^\w\- ]', '', playlist_title)
        # Get user's Public directory
        public_dir = os.path.expanduser('~/Public')
        output_dir = os.path.join(public_dir, playlist_title)
        os.makedirs(output_dir, exist_ok=True)
        for entry in info['entries']:
            title = entry.get('title', 'N/A')
            video_id = entry.get('id', 'N/A')
            print(f"Downloading: {title} (ID: {video_id})")
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            video_opts = {
                'quiet': True,
                'outtmpl': os.path.join(output_dir, '%(title)s.mp4'),
                'format': 'bestvideo+bestaudio/best',
                'merge_output_format': 'mp4'
            }
            with yt_dlp.YoutubeDL(video_opts) as video_ydl:
                try:
                    video_ydl.download([video_url])
                except Exception as e:
                    print(f"Failed to download {title}: {e}")

if __name__ == "__main__":
    main()

