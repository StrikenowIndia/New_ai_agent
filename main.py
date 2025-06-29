import datetime
import os
import logging
from flask import Flask, jsonify
from news_fetcher import get_trending_news
from news_collector import get_top_news
from script_writer import generate_script
from voiceover_generator import generate_voiceover
from video_editor import create_video
from youtube_uploader import upload_video

app = Flask(__name__)  # ✅ This is what Gunicorn needs

# Setup logging
logging.basicConfig(
    filename="log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run():
    try:
        logging.info("🛠️ Starting video generation...")

        today = datetime.datetime.now().strftime("%Y-%m-%d")
        news_data = get_top_news()

        if not news_data:
            logging.error("❌ No news data found!")
            return "No news data found", 500

        script = generate_script(news_data)
        audio_path = generate_voiceover(script)
        video_path = create_video(script, audio_path)

        if not video_path or not os.path.exists(video_path):
            logging.error("❌ Video creation failed. Skipping upload.")
            return "Video creation failed", 500

        video_title = f"आज की बड़ी खबरें - {today}"
        video_description = "जानिए आज की सभी बड़ी राष्ट्रीय और अंतरराष्ट्रीय खबरें एक ही वीडियो में।"
        upload_video(video_path, title=video_title, description=video_description)

        logging.info("🎬 Video generated and uploaded successfully!")
        return "Video generated and uploaded successfully!", 200
    except Exception as e:
        logging.error(f"❌ Error in run: {str(e)}")
        return f"Error: {str(e)}", 500

@app.route("/")
def home():
    return "🟢 Server is running!"

@app.route("/run", methods=["GET"])
def run_trigger():
    msg, code = run()
    return jsonify({"message": msg}), code

# Local test
if __name__ == "__main__":
    app.run(debug=True, port=5000)
