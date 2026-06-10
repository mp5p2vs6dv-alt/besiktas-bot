import feedparser
import tweepy
import time
import os

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
    feed = feedparser.parse("https://news.google.com/rss/search?q=Beşiktaş&hl=tr&gl=TR&ceid=TR:tr")
    for article in feed.entries[:5]:
        if article.link not in posted:
            tweet = f"⚫⚪🦅 {article.title}\n\n#Beşiktaş #BJK\n\n{article.link}"
            client.create_tweet(text=tweet[:280])
            posted.add(article.link)
            print(f"Paylaşıldı: {article.title}")
            time.sleep(10)

while True:
    check_and_post()
    print("1 saat bekleniyor...")
    time.sleep(3600)
