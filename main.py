import datetime
import os
import logging
from news_fetcher import get_trending_news
from news_collector import get_top_news
from script_writer import generate_script
from voiceover_generator import generate_voiceover
from video_editor import create_video
from youtube_uploader import upload_video

# Setup logging
logging.basicConfig(
    filename="log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def generate_video():
    try:
        logging.info("🛠️ Starting video generation...")

        today = datetime.datetime.now().strftime("%Y-%m-%d")
        news_data = get_top_news()

        if not news_data:
            logging.error("❌ No news data found!")
            return

        script = generate_script(news_data)
        audio_path = generate_voiceover(script)
        video_path = create_video(script, audio_path)

        if not video_path or not os.path.exists(video_path):
            logging.error("❌ Video creation failed. Skipping upload.")
            return

        video_title = f"आज की बड़ी खबरें - {today}"
        video_description = "जानिए आज की सभी बड़ी राष्ट्रीय और अंतरराष्ट्रीय खबरें एक ही वीडियो में।"
        upload_video(video_path, title=video_title, description=video_description)

        logging.info("🎬 Video generated and uploaded successfully!")
    except Exception as e:
        logging.error(f"❌ Error in generate_video: {str(e)}")
