from pytube import YouTube

# Paste URL of the YouTube video you want to download
# video_url = "https://youtu.be/ftKiHCDVwfA"
video_url = "https://youtu.be/ZnQwO6V7pec"

print('\ndownload initiated...\n')
#download location
target_folder = r"C:\Users\Harish Paramathma"

# Create a YouTube object
yt = YouTube(video_url)

# Filter and get the first stream that contains both video and audio
video_audio_stream = yt.streams.filter(progressive=True, file_extension='mp4').first()

# Download the stream
video_audio_stream.download(output_path=target_folder)

print("\ndone. Success")

