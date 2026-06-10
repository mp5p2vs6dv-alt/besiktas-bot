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

FEEDS = [
    "https://www.fanatik.com.tr/rss/besiktas",
    "https://www.ntvspornet/rss/besiktas"
]

def check_and_post():
    try:
        for feed_url in FEEDS:
            feed = feedparser.parse(feed_url)
            for article in feed.entries[:1]:
                if article.link not in posted:
                    tweet = article.title + "\n\n" + article.link + "\n\n#Besiktas #BJK"
                    client.create_tweet(text=tweet[:280])
                    posted.add(article.link)
                    print("Posted: " + article.title)
                    time.sleep(30)
    except Exception as e:
        print("Error: " + str(e))

while True:
    check_and_post()
    time.sleep(10800)