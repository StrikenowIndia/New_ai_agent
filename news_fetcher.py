# news_fetcher.py

import feedparser

def get_trending_news():
    rss_feeds = [
        "https://timesofindia.indiatimes.com/rssfeedstopstories.cms",
        "https://feeds.bbci.co.uk/news/world/rss.xml",
        "https://www.aljazeera.com/xml/rss/all.xml"
    ]

    all_headlines = []

    for url in rss_feeds:
        feed = feedparser.parse(url)
        for entry in feed.entries[:3]:  # Top 3 from each source
            title = entry.title
            summary = entry.get("summary", "")
            all_headlines.append(f"{title} - {summary}")

    return all_headlines[:5]  # Only return top 5 headlines

if __name__ == "__main__":
    news = get_trending_news()
    for i, item in enumerate(news):
        print(f"{i+1}. {item}")
