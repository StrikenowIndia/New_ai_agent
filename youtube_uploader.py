from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import os

def upload_to_youtube(video_path, title, description):
    scopes = ["https://www.googleapis.com/auth/youtube.upload"]
    flow = InstalledAppFlow.from_client_secrets_file("client_secrets.json", scopes)
    credentials = flow.run_console()

    youtube = build("youtube", "v3", credentials=credentials)

    request_body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": ["news", "india", "politics"],
            "categoryId": "25"  # News & Politics
        },
        "status": {
            "privacyStatus": "public"
        }
    }

    media = MediaFileUpload(video_path)
    youtube.videos().insert(part="snippet,status", body=request_body, media_body=media).execute()
