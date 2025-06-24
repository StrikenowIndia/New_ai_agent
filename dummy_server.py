# dummy_server.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "YouTube AI Agent is running"

def keep_alive():
    app.run(host='0.0.0.0', port=8080)
