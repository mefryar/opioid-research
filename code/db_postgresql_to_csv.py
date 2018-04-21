#!/usr/bin/env python
"""Export PostgreSQL Database to CSV

This module exports a PostgreSQL Database to a CSV file.

psql command:
\copy tweets to '[CSV PATH]' csv header
"""

import psycopg2
import settings

conn = psycopg2.connect(settings.PSYCOPG2_CONNECTION)
cursor = conn.cursor()

f = open(settings.CSV_NAME, 'w')
cursor.copy_to(f, settings.TABLE_NAME, sep=',')
conn.commit()
conn.close()
