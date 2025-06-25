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
        feed = feedparser.parse(feed_url)
        for entry in feed.entries[:3]:
            headline = entry.title
            summary = entry.get("summary", "")
            news_items.append({
                "headline": headline,
                "summary": summary
            })

    return news_items[:5]
