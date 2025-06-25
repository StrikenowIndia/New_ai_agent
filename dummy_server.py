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
        return f"""
        ✅ main.py executed.<br><br>
        🟢 Output:<br><pre>{result.stdout}</pre><br>
        🔴 Errors:<br><pre>{result.stderr}</pre>
        """
    except Exception as e:
        return f"❌ Error: {str(e)}"
