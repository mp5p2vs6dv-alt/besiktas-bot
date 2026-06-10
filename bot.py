import feedparser
import tweepy
import time
import os
from datetime import datetime

API_KEY = os.environ.get("API_KEY")
API_SECRET = os.environ.get("API_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")

client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

posted = set()

def check_and_post():
    try:
        feed = feedparser.parse("https://news.google.com/rss/search?q=Beşiktaş&hl=tr&gl=TR&ceid=TR:tr")
        for article in feed.entries[:1]:
            if article.link not in posted:
                source = article.source.get('title', '') if hasattr(article, 'source') else ''
tweet = f"⚫⚪🦅 {article.title}\n\n📰 {source}\n\n#Beşiktaş #BJK"

                client.create_tweet(text=tweet[:280])
                posted.add(article.link)
                print(f"Paylaşıldı: {article.title}")
    except Exception as e:
        print(f"Hata: {e}")

while True:
    hour = datetime.utcnow().hour
    # Post at 6am, 12pm, 6pm Istanbul time (UTC+3)
    if hour in [3, 9, 15]:
        check_and_post()
    time.sleep(3600)
