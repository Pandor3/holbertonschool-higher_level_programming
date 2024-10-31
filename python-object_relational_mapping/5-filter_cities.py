#!/usr/bin/python3
"""
This module will take the name of a state as an argument and list
all cities of that state using the hbtn_0e_4_usa database
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

    cursor = db.cursor
    cursor.execute("SELECT cities.id, cities.name, states.name \
            FROM cities JOIN states ON cities.state_id = states.id \
            WHERE states.name = %s \
            ORDER BY cities.id ASC;", (sys.argv[4],))

    for row in cursor.fetchall():
        print("{}, ".join.format(row[0]))

    cursor.close()
    db.close()
