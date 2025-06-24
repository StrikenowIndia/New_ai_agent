# main.py
import time
from video_editor import create_video
from youtube_uploader import upload_to_youtube
from dummy_server import keep_alive  # New line

def main():
    print("🚀 YouTube AI News Agent Starting...")
    create_video()
    upload_to_youtube()
    print("🏁 Process Complete.")
    keep_alive()  # Keep process alive for Render web service

if __name__ == '__main__':
    main()
