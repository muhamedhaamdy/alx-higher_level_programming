#!/usr/bin/python3
"""lists all states from the database with IDs in ascending order"""


import MySQLdb
import sys
db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2],
                     database=sys.argv[3], port=3306, host = 'localhost')
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY state.id")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
db.close()
