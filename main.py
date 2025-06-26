with open("debug.txt", "w") as f:
    f.write("✅ main.py started\n")

try:
    news_data = get_top_news()
    f.write(f"News fetched: {news_data}\n")
except Exception as e:
    f.write(f"News fetch error: {e}\n")
import datetime
import logging
import os
from news_fetcher import get_trending_news
from news_collector import get_top_news
from script_writer import generate_script
from voiceover_generator import generate_voiceover
from video_editor import create_video
from youtube_uploader import upload_video

# Setup logging
logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("🛠️ Starting video generation...")

    try:
        today = datetime.datetime.now().strftime("%Y-%m-%d")

        # 1. Get news
        news_data = get_top_news()
        if not news_data:
            logging.error("❌ No news data found!")
            return
        logging.info("✅ News fetched successfully.")

        # 2. Generate script
        try:
            script = generate_script(news_data)
            logging.info("✅ Script generated successfully.")
        except Exception as e:
            logging.error(f"❌ Error generating script: {e}")
            return

        # 3. Generate voiceover
        try:
            audio_path = generate_voiceover(script)
            logging.info("✅ Voiceover generated: %s", audio_path)
        except Exception as e:
            logging.error(f"❌ Error generating voiceover: {e}")
            return

        # 4. Create video
        try:
            video_path = create_video(script, audio_path)
            logging.info("✅ Video created: %s", video_path)
        except Exception as e:
            logging.error(f"❌ Error creating video: {e}")
            return

        # 5. Upload video
        try:
            video_title = f"आज की बड़ी खबरें - {today}"
            video_description = "जानिए आज की सभी बड़ी राष्ट्रीय और अंतरराष्ट्रीय खबरें एक ही वीडियो में।"
            upload_video(video_path, title=video_title, description=video_description)
            logging.info("✅ Video uploaded to YouTube successfully.")
        except Exception as e:
            logging.error(f"❌ Error uploading video: {e}")
            return

    except Exception as e:
        logging.critical(f"💥 Unhandled exception in main: {e}")

if __name__ == "__main__":
    main()
