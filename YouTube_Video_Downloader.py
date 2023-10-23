
from pytube import YouTube

import os


def download_video(url, output_path):
    try:
        yt = YouTube(url)
        video_stream = yt.streams.filter(res="2160p").first()

        if video_stream:
            video_stream.download(output_path=output_path)
            return video_stream.default_filename
        else:
            yt.streams.get_highest_resolution().download(output_path=output_path)
            print(f"File saved at: {output_path}")
            print("Download completed successfully!")
            
            exit(0)

    except Exception as e:
        print(f"An error occurred during video download: {str(e)}")
        return None


def download_audio(url, output_path):
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()

        if audio_stream:
            audio_stream.download(output_path=output_path)
            return audio_stream.default_filename
        else:
            print("No suitable audio stream available for this video.")
            return None

    except Exception as e:
        print(f"An error occurred during audio download: {str(e)}")
        return None


url = input("Enter the url of the video: ")
path = 'D:\Python\Side_Projects'
c = input("Enter A for audio and V for both audio and video: ")
if (c == 'A' or c == 'a'):
    audio_path = download_audio(url, path)
    print("Download completed successfully!")
    print(f"File saved at: {path}\{audio_path}")
    exit(0)
audio_path = download_audio(url, path)
video_path = download_video(url, path)
os.rename(audio_path, "audio.mp4")
os.rename(video_path, "video.webm")
output_name = "output.mp4"
os.system(
    f"ffmpeg -i video.webm -i audio.mp4 -c:v copy -c:a aac -map 0:v -map 1:a {output_name}")

os.remove("audio.mp4")
os.remove("video.webm")
print("Download completed successfully!")
print(f"File saved at: {path}\{output_name}")
