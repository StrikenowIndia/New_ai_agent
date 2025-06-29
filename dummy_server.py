from flask import Flask
import subprocess
import logging
import threading
import main  # use your updated main.py without Flask

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
        def background_task():
            main.run()

        threading.Thread(target=background_task).start()
        return """
        ✅ Video generation started in background.<br><br>
        📝 <a href="/logs" target="_blank">View logs</a>
        """
    except Exception as e:
        logging.exception("❌ Exception while running main.py")
        return f"❌ Error occurred. Check log.txt for details."

@app.route('/logs')
def view_logs():
    try:
        with open("log.txt", "r") as f:
            content = f.read()
        return f"<pre>{content}</pre>"
    except Exception as e:
        return f"❌ Cannot read log file: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
