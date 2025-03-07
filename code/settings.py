#!/usr/bin/env python
"""Define settings for Twitter scraper.

This module imports credentials necessary to authenticate with the Twitter
Streaming API from an untracked file. It also defines constants so that they
can be easily changed.

Hat tip: https://www.dataquest.io/blog/streaming-data-python/

"""

from datetime import datetime    # For timestamping csv files
import secrets

TWITTER_API_KEY = secrets.TWITTER_API_KEY
API_SECRET = secrets.API_SECRET
ACCESS_TOKEN = secrets.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = secrets.ACCESS_TOKEN_SECRET
PLOTLY_API_KEY = secrets.PLOTLY_API_KEY

# Note these are case-insensitive
TRACK_TERMS = ['burprenorphine', 'carfentanil', 'codeine', 'fentanyl',
               'heroin', 'injection site', 'hydrocodone', 'methadone',
               'morphine', 'naloxone', 'naltrexone', 'narcan', 'narcotic',
               'needle exchange', 'opana', 'opiate', 'opioid', 'opium',
               'overdose', 'oxycodone', 'oxycontin', 'percocet', 'suboxone',
               'safe injection', 'supervised injection', 'vicodin', 'vivitrol']
CONNECTION_STRING = 'postgresql://admin:{}' \
                    '@localhost:5432/tweets'.format(secrets.ADMIN_PASSWORD)
DB_NAME = 'tweets'
TABLE_NAME = 'tweets'
PSYCOPG2_CONNECTION = 'dbname={} user=admin ' \
                      'password={}'.format(DB_NAME, secrets.ADMIN_PASSWORD)

NOW = datetime.utcnow().strftime("%Y-%m-%d_%H.%M.%S")
CSV_NAME = '/Users/mefryar/Dropbox (Personal)/opioid-research/'\
           'opioid-db-backups/tweets_{}.csv'.format(NOW)

DATA_PATH = '/Users/mefryar/Dropbox (Personal)/opioid-research/data/'
