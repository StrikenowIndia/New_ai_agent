from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "StrikeNowIndia AI Agent Running"

def keep_alive():
    app.run(host='0.0.0.0', port=10000)
