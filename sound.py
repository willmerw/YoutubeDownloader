from pytube import YouTube
from sys import argv

link = "https://www.youtube.com/watch?v=Am4wYTiHHx8"
yt = YouTube(link)

print(f'Title: {yt.title}')

yd = yt.streams.get_audio_only()

yd.download("E:\Ljudosv")

