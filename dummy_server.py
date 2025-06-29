from flask import Flask
import subprocess
import logging

app = Flask(__name__)

# Set up logging to a file
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
        result = subprocess.run(['python', 'main.py'], capture_output=True, text=True)

        # Save output and error to log file
        logging.info("✅ main.py Output:\n" + result.stdout)
        logging.error("🔴 main.py Errors:\n" + result.stderr)

        return """
        ✅ main.py executed. Check log.txt for details.<br><br>
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
        
