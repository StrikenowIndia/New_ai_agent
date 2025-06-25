from flask import Flask

app = Flask(__name__)

@app.route('/run')
def run_main():
    subprocess.run(['python', 'main.py'], ...)
