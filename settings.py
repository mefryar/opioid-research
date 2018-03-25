#!/usr/bin/env python
"""Define settings for Twitter scraper.

This module imports credentials necessary to authenticate with the Twitter
Streaming API from an untracked file. It also defines constants so that they
can be easily changed.

Hat tip: https://www.dataquest.io/blog/streaming-data-python/

"""

import twitter_tokens

TWITTER_APP_KEY = twitter_tokens.TWITTER_APP_KEY
TWITTER_APP_SECRET = twitter_tokens.TWITTER_APP_SECRET
TWITTER_KEY = twitter_tokens.TWITTER_KEY
TWITTER_SECRET = twitter_tokens.TWITTER_SECRET

TRACK_TERMS = ['opioid', 'opiate', 'heroin', 'fentanyl', 'methadone']
CONNECTION_STRING = 'sqlite:///tweets.db'
CSV_NAME = 'tweets.csv'
TABLE_NAME = 'tweets'
