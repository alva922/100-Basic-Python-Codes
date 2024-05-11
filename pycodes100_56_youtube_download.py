#https://newdigitals.org/2024/02/24/100-basic-python-codes/#youtube-downloader
# YouTube Downloader

2
!pip install pytube
Successfully installed pytube-15.0.0

from pytube import YouTube
 
link = input('https://youtu.be/GtvUxXyFoMw')
 
yt = YouTube(link)
yt.streams.first().download()
 
print('download', link)

#Example I/O

Input the link:
https://youtu.be/GtvUxXyFoMw
download https://youtu.be/GtvUxXyFoMw
#Output mp4 file (5.4 Mb)
How to become a software engineer  Important tips to become a software engineer
