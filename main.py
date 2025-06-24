from news_generator import fetch_news
from voiceover import generate_voiceover
from video_editor import create_video
from youtube_uploader import upload_to_youtube

def run_agent():
    topic, headline = fetch_news()
    print(f"📰 Topic: {topic} | Headline: {headline}")

    voice_file = generate_voiceover(headline)
    video_path = create_video(voice_file, headline)

    upload_to_youtube(video_path, title=headline, description=f"{topic} - Daily News in Hindi")

if __name__ == "__main__":
    run_agent()
