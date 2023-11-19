from pytube import YouTube
from sys import argv

#Paste youtube link
link = ""
yt = YouTube(link)

print(f'Title: {yt.title}')

yd = yt.streams.get_audio_only()

#Type location in download
yd.download("")

