#!/usr/bin/python3
import MySQLdb
import sys
"""lists all states from the database """
"""that starts with letter N in ascending order"""


if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2],
                         database=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
