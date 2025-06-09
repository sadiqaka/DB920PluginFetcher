import feedparser
from config import RSS_FEEDS, YOUTUBE_FEEDS

def fetch_all_feeds():
    all_items = []
    for url in RSS_FEEDS + YOUTUBE_FEEDS:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            item = {
                "title": entry.title,
                "link": entry.link,
                "summary": getattr(entry, "summary", ""),
                "published": getattr(entry, "published", "")
            }
            all_items.append(item)
    return all_items
