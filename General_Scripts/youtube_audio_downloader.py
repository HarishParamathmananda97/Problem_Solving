from pytube import YouTube

# Paste URL of the YouTube video you want to download
audio_url = "https://www.youtube.com/watch?v=fenbT_OxipM&pp=ygUXYXVkaW9ib2sgdGFtaWwgcGxheWxpc3Q%3D"

# Create a YouTube object
yt = YouTube(audio_url)

# Filter and get the first audio stream
audio_stream = yt.streams.filter(only_audio=True).first()

# Download the audio
audio_stream.download()
