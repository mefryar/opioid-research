#!/usr/bin/env python
"""Define settings for Twitter scraper.

This module imports credentials necessary to authenticate with the Twitter
Streaming API from an untracked file. It also defines constants so that they
can be easily changed.

Hat tip: https://www.dataquest.io/blog/streaming-data-python/

"""

from datetime import datetime    # For timestamping csv files
import twitter_tokens

TWITTER_APP_KEY = twitter_tokens.TWITTER_APP_KEY
TWITTER_APP_SECRET = twitter_tokens.TWITTER_APP_SECRET
TWITTER_KEY = twitter_tokens.TWITTER_KEY
TWITTER_SECRET = twitter_tokens.TWITTER_SECRET

# Note these are case-insensitive
TRACK_TERMS = ['burprenorphine', 'carfentanil', 'codeine', 'fentanyl',
               'heroin', 'hydrocodone', 'methadone', 'morphine', 'naloxone',
               'naltrexone', 'narcan', 'narcotic', 'opana', 'opiate', 'opioid',
               'opium', 'overdose', 'oxycodone', 'oxycontin', 'percocet',
               'suboxone', 'vicodin', 'vivitrol']
CONNECTION_STRING = 'sqlite:///tweets.db'
DB_NAME = 'tweets'
TABLE_NAME = 'tweets'

NOW = datetime.utcnow().strftime("%Y-%m-%d_%H.%M.%S")
CSV_NAME = '/Users/mifryar/Documents/Dropbox (Personal)/TDI/opioid-research/' \
           'tweets_{}.csv'.format(NOW)
