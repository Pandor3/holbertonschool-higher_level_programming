#!/usr/bin/python3
"""
This module will be used to list all cities from the database
named hbtn_0e_4_usa
"""


import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3]
    )

    cursor = db.cursor()

    cursor.execute(
            "SELECT * FROM states "
            "ORDER BY cities.id ASC ",
    )

    for state in cursor.fetchall():
        print("{}".format(state))

    cursor.close()
    db.close()
