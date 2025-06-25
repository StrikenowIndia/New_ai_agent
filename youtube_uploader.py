def upload_video(file, title, description):
    scopes = ["https://www.googleapis.com/auth/youtube.upload"]
    creds = None

    # Load token.json only (no console auth in cron!)
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", scopes)
    else:
        print("❌ ERROR: token.json missing. Please upload it manually.")
        return

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
