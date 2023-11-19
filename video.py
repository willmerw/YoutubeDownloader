from pytube import YouTube
from sys import argv

#Paste youtube link
link = ""
yt = YouTube(link)

print(f'Title: {yt.title}')

yd = yt.streams.get_by_resolution("720p")
#yd = yt.streams.get_highest_resolution()
#yd = yt.streams.get_lowest_resolution()

#Type location in download
yd.download()
