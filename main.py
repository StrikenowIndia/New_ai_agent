from video_editor import create_video
from youtube_uploader import upload_to_youtube
from dummy_server import keep_alive
import threading
import time

def main_loop():
    while True:
        headline = "आज की ताज़ा खबर"
        voice_file = "voice.mp3"  # पहले से जनरेट किया गया या TTS से ऑटो बना सकते हैं
        video_file = create_video(voice_file, headline)
        upload_to_youtube(video_file, headline)
        time.sleep(86400)  # रोज़ 1 बार

# Flask server अलग thread में
threading.Thread(target=main_loop).start()

# Flask server रन करो (Render को awake रखने के लिए)
keep_alive()
