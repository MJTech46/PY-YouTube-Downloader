from pytube import Playlist
import pytube
import os

def download_videos(playlist_url):
    playlist = Playlist(playlist_url)
    print("Playlist name:",playlist.title)
    print("number of videos:",len(playlist.video_urls))
    count=1
    for url in playlist.video_urls:
        youtube = pytube.YouTube(url)
        video = youtube.streams.get_highest_resolution()
        print(count,"/",len(playlist.video_urls),"\tDownloading....",pytube.YouTube(url).title)
        video.download(os.path.join(os.path.expanduser("~"), "Downloads", playlist.title) )
        print("\tCompleted.")
        count+=1

# Replace with your playlist URL
download_videos('https://youtube.com/playlist?list=')
