#!/usr/bin/python3
"""
This module will be used to learn about how to avoid SQL injections
"""


import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor(MySQLdb.cursors.DictCursor)

    cursor.execute(
        "SELECT * FROM states "
        "WHERE BINARY name = '{}' "
        "ORDER BY id ASC".format(sys.argv[4]))

    for state in cursor.fetchall():
        print("{}".format(state))

    cursor.close()
    db.close()
