# youtube_uploader.py

import os
import logging
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials

logging.basicConfig(filename="log.txt", level=logging.INFO)

def upload_video(file, title, description):
    scopes = ["https://www.googleapis.com/auth/youtube.upload"]
    creds = None

    try:
        # Check for token.json
        if not os.path.exists("token.json"):
            logging.error("❌ token.json file missing. Upload failed.")
            print("❌ ERROR: token.json missing. Please upload it manually.")
            return

        creds = Credentials.from_authorized_user_file("token.json", scopes)
        youtube = build("youtube", "v3", credentials=creds)

        request_body = {
            "snippet": {
                "title": title,
                "description": description,
                "tags": ["India", "News", "StrikeNowIndia"],
                "categoryId": "25"
            },
            "status": {
                "privacyStatus": "public"
            }
        }

        if not os.path.exists(file):
            logging.error(f"❌ Video file '{file}' not found.")
            print(f"❌ Video file '{file}' not found.")
            return

        media = MediaFileUpload(file)
        response = youtube.videos().insert(
            part="snippet,status",
            body=request_body,
            media_body=media
        ).execute()

        logging.info(f"✅ Uploaded: Video ID = {response.get('id')}")
        print("✅ Video uploaded to YouTube successfully.")

    except Exception as e:
        logging.error(f"❌ Error during upload: {str(e)}")
        print(f"❌ Upload error: {str(e)}")
