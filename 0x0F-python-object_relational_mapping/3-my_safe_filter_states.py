#!/usr/bin/python3
"""lists all states from the database """
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2],
                         database=sys.argv[3])
    cur = db.cursor()
    q = sys.argv[4]
    query = "SELECT * FROM states WHERE name LIKE BINARY %s\
    ORDER BY id".format(q)
    cur.execute(query, (q,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
