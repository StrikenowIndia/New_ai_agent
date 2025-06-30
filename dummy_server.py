from flask import Flask
import subprocess
import logging

app = Flask(__name__)

# Logging setup
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
        open("log.txt", "w").close()  # clear logs

        with open("log.txt", "a") as f:
            subprocess.run(['python', 'main.py'], stdout=f, stderr=f)

        return """
        ✅ main.py executed. Check log.txt for details.<br><br>
        📝 <a href="/logs" target="_blank">View logs</a>
        """
    except Exception as e:
        logging.exception("❌ Exception while running main.py")
        return "❌ Error occurred. Check log.txt for details."

@app.route('/logs')
def view_logs():
    try:
        with open("log.txt", "r") as f:
            return f"<pre>{f.read()}</pre>"
    except Exception as e:
        return f"❌ Cannot read log file: {str(e)}"
