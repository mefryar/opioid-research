#!/usr/bin/env python
"""Export SQLite3 Database to CSV

This module exports an SQLite Database to a CSV file.

"""

import csv
import sqlite3
import settings

conn = sqlite3.connect(settings.DB_NAME)
cursor = conn.cursor()
cursor.execute('SELECT * FROM {}'.format(settings.TABLE_NAME))

with open(settings.CSV_NAME, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(i[0] for i in cursor.description)  # write headers
    csv_writer.writerows(cursor)
