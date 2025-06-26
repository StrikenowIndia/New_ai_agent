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

def main():
    logging.info("🛠️ Starting video generation...")

    # 1. Get today's date and fetch top news
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    news_data = get_top_news()  # [{'headline': ..., 'summary': ...}, ...]

    if not news_data:
        logging.error("❌ No news data found!")
        return

    # 2. Generate script from news
    script = generate_script(news_data)

    # 3. Generate voiceover from script
    audio_path = generate_voiceover(script)

    # 4. Generate video using visuals + audio
    video_path = create_video(script, audio_path)

    # 5. Upload video to YouTube
    video_title = f"आज की बड़ी खबरें - {today}"
    video_description = "जानिए आज की सभी बड़ी राष्ट्रीय और अंतरराष्ट्रीय खबरें एक ही वीडियो में।"
    upload_video(video_path, title=video_title, description=video_description)

    logging.info("🎬 Video generated and uploaded successfully!")

if __name__ == "__main__":
    open('log.txt', 'w').close()  # clear old logs
    main()
