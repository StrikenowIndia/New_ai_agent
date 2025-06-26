# news_fetcher.py

import feedparser
import logging

logging.basicConfig(filename='log.txt', level=logging.INFO)

def get_trending_news():
    rss_feeds = [
        "https://timesofindia.indiatimes.com/rssfeedstopstories.cms",
        "https://feeds.bbci.co.uk/news/world/rss.xml",
        "https://www.aljazeera.com/xml/rss/all.xml"
    ]

    all_headlines = []

    for url in rss_feeds:
        feed = feedparser.parse(url)
        logging.info(f"📥 Fetched feed: {url} with {len(feed.entries)} entries")
        for entry in feed.entries[:3]:  # Top 3 from each source
            headline = entry.title
            summary = entry.get("summary", "")
            all_headlines.append({
                "headline": headline.strip(),
                "summary": summary.strip()
            })

    logging.info(f"📰 Total news collected: {len(all_headlines)}")
    return all_headlines[:5]  # Top 5 total

if __name__ == "__main__":
    news = get_trending_news()
    for i, item in enumerate(news, start=1):
        print(f"{i}. {item['headline']} - {item['summary'][:100]}...")
