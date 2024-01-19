from pytube import YouTube

def download_video(url, save_path):
    try:
        video = YouTube(url)
        stream = video.streams.get_highest_resolution()
        stream.download(save_path)
        print("Download successful!")
    except Exception as e:
        print(f"Error: {e}")

#enter video url in between the semicolon and run a code
video_url = "https://youtu.be/7wnove7K-ZQ?si=-pTui60m9SOsJVMJ"
save_path = "/path/video"

download_video(video_url, save_path)
