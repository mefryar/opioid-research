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
        if hasattr(status, 'retweeted_status') or (status.lang != 'en'):
            return

        else:
            try:
                text = status.extended_tweet['full_text']
            except AttributeError:
                text = status.text
            created = status.created_at
            handle = status.user.screen_name
            loc = status.user.location
            tweet_id = status.id_str
            user_id = status.user.id

            blob = TextBlob(text)
            polarity = blob.sentiment.polarity
            subjectivity = blob.sentiment.subjectivity

            table = db[settings.TABLE_NAME]
            try:
                table.insert(dict(
                    tweet_id=tweet_id,
                    user_id=user_id,
                    handle=handle,
                    user_location=loc,
                    text=text,
                    created=created,
                    polarity=polarity,
                    subjectivity=subjectivity,
                ))
            except ProgrammingError as err:
                logging.warning(err)

    def on_error(self, status_code):
        if status_code == 420:  # rate limiting
            return False


# Authenticate using tokens defined in settings.py
auth = tweepy.OAuthHandler(settings.TWITTER_APP_KEY,
                           settings.TWITTER_APP_SECRET)
auth.set_access_token(settings.TWITTER_KEY, settings.TWITTER_SECRET)
api = tweepy.API(auth)

stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener,
                       tweet_mode='extended')
stream.filter(track=settings.TRACK_TERMS)
