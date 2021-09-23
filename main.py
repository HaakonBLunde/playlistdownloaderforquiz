import os
from pytube import YouTube
from pytube import Playlist
from moviepy.editor import *
import pathlib
import time
from datetime import date
'''
link = input("Enter the link of YouTube video you want to download:  ")
yt = YouTube(link)

#Showing details
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)
#Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

#Starting download
print("Downloading...")
file = ys.download()
fileName = yt.title + '.mp3'
'''
#last ned spillelista
p = Playlist(input("Enter the link of the playlist you want to fuck around with: "))
print("songs in playlist: %s" % len(p.video_urls))

files = list()
fileNames = list()
for video in p.videos:
    files.append(video.streams.first().download())
    fileNames.append(video.title + ".mp3")
    print("downloaded song")

#print(files)
#print(fileNames)
cleanFileNames = list()

for filename in fileNames:
    cleanFileNames.append(filename.translate({ord(i): None for i in '/\\'}))

#print(cleanFileNames)


#lage nytt directory for denne ukas quiz
who_has_quiz = input("Hvem holder quizen den aktuelle uka? Skriv bare bokstaver: ")
currentPath = pathlib.Path(__file__).parent.resolve()
fileDir = os.path.join(currentPath, who_has_quiz)
pathlib.Path(fileDir).mkdir(parents=True, exist_ok=True)


#konverter til mp3

for i in range(len(files)):
    video = VideoFileClip(files[i])
    video.audio.write_audiofile(os.path.join(fileDir, cleanFileNames[i]))
    video.close()





for file in files:
    os.remove(file)
print("Download completed!!")
