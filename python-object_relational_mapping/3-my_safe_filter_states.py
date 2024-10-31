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

    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM states "
        "ORDER BY id ASC",
        (sys.argv[4],)
    )

    for state in cursor.fetchall():
        if str(state[1]) == sys.argv[4]:
            print("{}".format(state))

    cursor.close()
    db.close()
