#!/bin/bash

# Activate virtualenv if needed (optional)
# source venv/bin/activate

# Start Flask app using gunicorn with 15-minute timeout
gunicorn dummy_server:app --timeout 900 -b 0.0.0.0:10000
