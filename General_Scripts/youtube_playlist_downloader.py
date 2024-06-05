from pytube import Playlist, YouTube
import os
from tqdm import tqdm
# URL of the YouTube playlist
playlist_url = 'https://www.youtube.com/watch?v=MCIX5veJVic&list=PLUUFoSVr3vJe_qlVJr9ZKLBGzGrb9WrD2&pp=iAQB'
# 'Eduraka_Simplilearn_Playlist_ML_Python_stuff':'https://www.youtube.com/playlist?list=PLEiEAq2VkUULYYgj13YHUWmRePqiu8Ddy','codebasics':'https://www.youtube.com/playlist?list=PLEiEAq2VkUULYYgj13YHUWmRePqiu8Ddy',

playlist_list_url = {'UnitTest_Durgasir':'https://www.youtube.com/playlist?list=PLd3UqWTnYXOlb7QmXAYRGxDGf2xJ07V9N'}

# Create Playlist object
for playlist_url in playlist_list_url:
    playlist = Playlist(playlist_list_url[playlist_url])

    # Specify the output directory
    output_dir = rf'E:\{playlist_url}'

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    os.chdir(output_dir)
    files = os.listdir()
    count = 0
    # Iterate over videos in the playlist
    for video in tqdm(playlist.videos):
        count += 1
        if count <= len(files):
        #     # skipping the videos
            continue

        try:
            # Create a YouTube object for each video
            yt = YouTube(video.watch_url)

            # Get the video file name
            video_file_name = yt.streams.filter(progressive=True, file_extension='mp4').first().default_filename
            # print(video_file_name)
            if video_file_name in files:
                # print(f"{video_file_name} : Already downloaded, heading to download next.")
                continue
        
            # Download the video
            yt.streams.filter(progressive=True, file_extension='mp4').first().download(output_path=output_dir)

            # print(f"Downloaded: {video.title}")
        except Exception as e:
            print(f"Error downloading {video.title}: {str(e)}")
