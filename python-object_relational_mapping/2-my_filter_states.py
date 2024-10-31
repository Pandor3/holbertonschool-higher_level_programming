#!/usr/bin/python3
"""
This module will be used to take an argument and display all values
in the states table of hbtn_0e_0_usa where name matches the argument
"""


import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        state_name_searched=sys.argv[4]
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC;")

    for state in cursor.fetchall():
        if state["name"] == state_name_searched:
            print(state)

    cursor.close()
    db.close()
