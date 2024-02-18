#!/usr/bin/python3
import MySQLdb
import sys
db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2], database=sys.argv[3])
cur = db.cursor()
cur.execute("SELECT * FORM states ORDER BY states.id")
rows = cur.fetchone()
