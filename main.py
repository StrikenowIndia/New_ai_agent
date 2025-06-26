1| import datetime
2| import os
3| import logging
4| from news_fetcher import get_trending_news
5| from news_collector import get_top_news
6| from script_writer import generate_script
7| from voiceover_generator import generate_voiceover
8| from video_editor import create_video
9| from youtube_uploader import upload_video
10|
11| # Setup logging
12| logging.basicConfig(
13|     filename="log.txt",
14|     level=logging.INFO,
15|     format="%(asctime)s - %(levelname)s - %(message)s"
16| )
17|
18| def main():
19|     logging.info("🛠️ Starting video generation...")
20|
21|     # 1. Get today's date and fetch top news
22|     today = datetime.datetime.now().strftime("%Y-%m-%d")
23|     news_data = get_top_news()  # [{'headline': ..., 'summary': ...}, ...]
24|
25|     if not news_data:
26|         logging.error("❌ No news data found!")
27|         return
28|
29|     # 2. Generate script from news
30|     script = generate_script(news_data)
31|
32|     # 3. Generate voiceover from script
33|     audio_path = generate_voiceover(script)
34|
35|     # 4. Generate video using visuals + audio
36|     video_path = create_video(script, audio_path)
37|
38|     # 5. Upload video to YouTube
39|     video_title = f"आज की बड़ी खबरें - {today}"
40|     video_description = "जानिए आज की सभी बड़ी राष्ट्रीय और अंतरराष्ट्रीय खबरें एक ही वीडियो में।"
41|     upload_video(video_path, title=video_title, description=video_description)
42|
43|     logging.info("🎬 Video generated and uploaded successfully!")
44|
45| if __name__ == "__main__":
46|     open('log.txt', 'w').close()  # clear old logs
47|     main()
