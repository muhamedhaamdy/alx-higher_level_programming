#!/usr/bin/python3
""" lists all cities from the database"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2],
                         database=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name\
                 FROM cities, states\
                 WHERE states.name = %s\
                 ORDER BY cities.id;",(sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
