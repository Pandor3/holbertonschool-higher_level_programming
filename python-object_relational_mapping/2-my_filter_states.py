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

    cursor = db.cursor(MySQLdb.cursors.DictCursor)

    state_name_searched = sys.argv[4]
    query = (
        "SELECT * FROM states "
        "WHERE name = '{}' "
        "ORDER BY id ASC".format(state_name_searched.replace("'", "''"))
    )

    cursor.execute(query)

    for state in cursor.fetchall():
        if state["name"] == state_name_searched:
            print(state)

    cursor.close()
    db.close()
