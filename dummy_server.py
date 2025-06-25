from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'YouTube AI News Agent is live!'
@app.route('/run')
def run_main():
    subprocess.run(['python', 'main.py'], ...)
