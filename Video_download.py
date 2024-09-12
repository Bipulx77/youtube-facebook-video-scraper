import os
import yt_dlp
from rich import print
import asyncio

# Set the root path and change the current working directory
root_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(root_path)

# Create a folder named 'YouTube_Video' if it doesn't exist
youtube_folder = os.path.join(root_path, 'YouTube_Video')
if not os.path.exists(youtube_folder):
    os.makedirs(youtube_folder)

async def download_youtube_video(video_url):
    ydl_opts = {
        'outtmpl': os.path.join(youtube_folder, '%(title)s.%(ext)s'),  # Save the video in the 'YouTube_Video' folder
        'quiet': False,                
        'format': 'bestvideo[height<=1080]+bestaudio/best[height<=720]',  
    }
    
    loop = asyncio.get_event_loop()

    def run_yt_dlp():
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=True)
            return info_dict

    info_dict = await loop.run_in_executor(None, run_yt_dlp)

    # Extract and print video details
    title = info_dict.get('title', None)
    channel_Name = info_dict.get('uploader', None)
    description = info_dict.get('description', None)
    
    print({
        'channel_Name': channel_Name,
        'title': title,
        'Description': description,
    })
    print('Video Downloaded...')

async def main():
    video_url = input("Enter the YouTube video URL: ")
    await download_youtube_video(video_url)
    print('Download complete')

if __name__ == "__main__":
    asyncio.run(main())
