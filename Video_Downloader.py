import pytube
import os

def download_video(video_url):
    youtube = pytube.YouTube(video_url)
    video = youtube.streams.get_highest_resolution()
    print("Video Name:",youtube.title)
    print("Downloading....")
    video.download(os.path.join(os.path.expanduser("~"), "Downloads"))
    print("Completed.")

# Replace with your video URL
download_video("https://youtu.be/r0_LhVDYX50?si=IvPLW0qwLfGbF5Ig")