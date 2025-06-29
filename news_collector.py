# news_collector.py

import feedparser

def get_top_news():
    rss_feeds = [
        "https://timesofindia.indiatimes.com/rssfeedstopstories.cms",
        "https://feeds.bbci.co.uk/news/world/rss.xml",
        "https://www.aljazeera.com/xml/rss/all.xml"
    ]

    news_items = []

    for feed_url in rss_feeds:
        try:
            feed = feedparser.parse(feed_url)
            for entry in feed.entries[:3]:
                headline = entry.title.strip()
                summary = entry.get("summary", "").strip()
                news_items.append({
                    "headline": headline,
                    "summary": summary
                })
        except Exception as e:
            print(f"❌ Error parsing {feed_url}: {e}")

    return news_items[:5] if len(news_items) >= 5 else news_items

# Debug run
if __name__ == "__main__":
    news = get_top_news()
    for i, item in enumerate(news, 1):
        print(f"{i}. {item['headline']}\n{item['summary']}\n")
        
