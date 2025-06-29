from flask import Flask, jsonify
import threading
import logging
from main import generate_video  # make sure generate_video() exists in main.py

app = Flask(__name__)

# Logging to file
logging.basicConfig(
    filename='log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

@app.route("/")
def home():
    return jsonify({"status": "✅ YouTube AI News Agent is live!"})

@app.route("/run", methods=["GET"])
def trigger_video():
    try:
        thread = threading.Thread(target=generate_video)
        thread.start()
        return jsonify({"status": "🎬 Video generation started in background"})
    except Exception as e:
        logging.exception("❌ Error triggering video generation")
        return jsonify({"error": str(e)})

@app.route("/logs", methods=["GET"])
def get_logs():
    try:
        with open("log.txt", "r") as f:
            content = f.read()
        return f"<pre>{content}</pre>"
    except Exception as e:
        return f"❌ Failed to read logs: {str(e)}"
