def main():
    print("📺 Starting video creation...")

    today = datetime.datetime.now().strftime("%Y-%m-%d")
    news_data = get_top_news()

    if not news_data:
        print("❌ No news found.")
        return

    script = generate_script(news_data)
    audio_path = generate_voiceover(script)
    video_path = create_video(script, audio_path)

    video_title = f"आज की बड़ी खबरें - {today}"
    video_description = "राष्ट्रीय और अंतरराष्ट्रीय सभी बड़ी खबरें देखें इस वीडियो में।"
    upload_video(video_path, title=video_title, description=video_description)

    print("✅ Upload complete.")
