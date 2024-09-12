import os
from rich import print
import yt_dlp
import asyncio

# Set the root path and change the current working directory
root_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(root_path)

# Create a folder named 'Facebook_download' if it doesn't exist
facebook_folder = os.path.join(root_path, 'Facebook_download')
if not os.path.exists(facebook_folder):
    os.makedirs(facebook_folder)

async def download_facebook_video(video_url):
    try:
        ydl_opts = {
            'outtmpl': os.path.join(facebook_folder, '%(title)s.%(ext)s'),  # Save the video in the 'Facebook_download' folder
            'quiet': False,                  
            'format': 'bestvideo+bestaudio/best',  
        }
        
        loop = asyncio.get_event_loop()

        def run_yt_dlp():
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(video_url, download=True)
                return info_dict

        info_dict = await loop.run_in_executor(None, run_yt_dlp)

        # Extract video details (if needed for any future use)
        video_title = info_dict.get('title', 'Unknown Title')
        video_channel = info_dict.get('uploader', 'Unknown Channel')
        video_description = info_dict.get('description', '')
        
        # Print the video information
        print({
            'channel_Name': video_channel,
            'title': video_title,
            'Description': video_description,
        })
        print('Video downloaded successfully...')
    
    except Exception as e:
        print(f"An error occurred: {e}")

async def main():
    video_url = input("Enter the Facebook video URL: ")
    await download_facebook_video(video_url)
    print('Download complete')

if __name__ == "__main__":
    asyncio.run(main())
