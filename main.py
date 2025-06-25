from video_editor import create_video
from youtube_uploader import upload_to_youtube

def main():
    headline = "दिल्ली में भारी बारिश, ट्रैफिक प्रभावित"
    voice_file = "voice.mp3"
    
    print("🎥 Generating video...")
    create_video(voice_file, headline)
    
    print("📤 Uploading to YouTube...")
    upload_to_youtube(headline, "Breaking news from Delhi. @StrikeNowIndia")
    
    print("✅ Done!")

if __name__ == "__main__":
    keep_alive()  # Keeps web server alive
    main()
