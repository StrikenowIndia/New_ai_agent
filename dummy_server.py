# dummy_server.py
from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "Running..."

def keep_alive():
    def run():
        app.run(host='0.0.0.0', port=10000)
    t = threading.Thread(target=run)
    t.start()
