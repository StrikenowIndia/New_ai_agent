# dummy_server.py
from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return '✅ YouTube AI News Agent is live!'

@app.route('/run')
def run_main():
    try:
        result = subprocess.run(['python', 'main.py'], capture_output=True, text=True)
        return f"✅ main.py executed.\n\n🟢 Output:\n{result.stdout}\n\n🔴 Errors:\n{result.stderr}"
    except Exception as e:
        return f"❌ Error: {str(e)}"
