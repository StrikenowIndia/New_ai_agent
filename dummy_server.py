from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return 'YouTube AI News Agent is live!'

@app.route('/run')
def run_main():
    try:
        # Run main.py when this endpoint is triggered
        result = subprocess.run(['python', 'main.py'], capture_output=True, text=True)
        return f"main.py executed. Output:\n{result.stdout}\nErrors:\n{result.stderr}"
    except Exception as e:
        return f"Error: {str(e)}"
