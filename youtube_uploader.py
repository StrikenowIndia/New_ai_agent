import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def upload_video(file, title, description):
    scopes = ["https://www.googleapis.com/auth/youtube.upload"]
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", scopes)
    else:
        flow = InstalledAppFlow.from_client_secrets_file("client_secrets.json", scopes)
        creds = flow.run_console()
        with open("token.json", "w") as token:
            token.write(creds.to_json())

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

    media = MediaFileUpload(file)
    youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=media
    ).execute()
    print("✅ Video uploaded to YouTube successfully.")
