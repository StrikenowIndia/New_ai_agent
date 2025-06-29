from flask import Flask
import threading
import logging
from main import generate_video  # 🟢 directly import the function

app = Flask(__name__)

logging.basicConfig(
    filename='log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

@app.route('/')
def home():
    return '✅ YouTube AI News Agent is live!'

@app.route('/run')
def run_main():
    try:
        # Clear old logs
        open("log.txt", "w").close()

        # Run video generator in background thread
        thread = threading.Thread(target=generate_video)
        thread.start()

        return """
        ✅ Video generation started in background.<br><br>
        📝 <a href="/logs" target="_blank">View logs</a>
        """
    except Exception as e:
        logging.exception("❌ Exception while running generate_video")
        return "❌ Error occurred. Check log.txt for details."

@app.route('/logs')
def view_logs():
    try:
        with open("log.txt", "r") as f:
            content = f.read()
        return f"<pre>{content}</pre>"
    except Exception as e:
        return f"❌ Cannot read log file: {str(e)}"
