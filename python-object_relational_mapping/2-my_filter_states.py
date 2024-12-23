#!/usr/bin/python3
"""
This module takes an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
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
        "WHERE BINARY name = '{}' "
        "ORDER BY id ASC".format(sys.argv[4]))

    for state in cursor.fetchall():
        print("{}".format(state))

    cursor.close()
    db.close()
