#!/usr/bin/env python
"""Twitter scraper

This module scrapes tweets from the Twitter Streaming API and saves them to an
SQLite database.

Hat tip: https://www.dataquest.io/blog/streaming-data-python/

"""

import logging
import tweepy
import dataset
from sqlalchemy.exc import ProgrammingError
from requests.packages.urllib3.exceptions import ReadTimeoutError
from textblob import TextBlob
import settings

logging.basicConfig(
    filename=f"logs/{__name__}.log",
    level=logging.DEBUG,
    format="%(name)s - %(asctime)s - %(levelname)s - %(message)s",
    filemode='w')
logger = logging.getLogger()
logger.info('Starting log...')

db = dataset.connect(settings.CONNECTION_STRING)


class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        if hasattr(status, 'retweeted_status'):
            return

        else:
            try:
                text = status.extended_tweet['full_text']
            except AttributeError:
                text = status.text
            created_utc = status.created_at
            favs = status.favorite_count
            followers = status.user.followers_count
            handle = status.user.screen_name
            loc = status.user.location
            rts = status.retweet_count
            tweet_id_str = status.id_str
            user_id_str = status.user.id_str

            blob = TextBlob(text)
            polarity = blob.sentiment.polarity
            subjectivity = blob.sentiment.subjectivity

            table = db[settings.TABLE_NAME]
            try:
                table.insert(dict(
                    tweet_id=tweet_id_str,
                    user_id=user_id_str,
                    handle=handle,
                    user_location=loc,
                    followers=followers,
                    text=text,
                    created_utc=created_utc,
                    favorites=favs,
                    retweets=rts,
                    polarity=polarity,
                    subjectivity=subjectivity,
                ))
            except ProgrammingError as err:
                logging.warning(err)

    def on_error(self, status_code):
        if status_code == 420:  # rate limiting
            return False


if __name__ == '__main__':
    # Authenticate using tokens defined in settings.py
    auth = tweepy.OAuthHandler(settings.TWITTER_APP_KEY,
                               settings.TWITTER_APP_SECRET)
    auth.set_access_token(settings.TWITTER_KEY, settings.TWITTER_SECRET)
    api = tweepy.API(auth)

    while True:
        try:
            stream_listener = StreamListener()
            stream = tweepy.Stream(auth=api.auth, listener=stream_listener,
                                   tweet_mode='extended')
            stream.filter(track=settings.TRACK_TERMS, languages=['en'],
                          stall_warnings=True)
        except ReadTimeoutError as err:
            logging.warning(err)
            continue
