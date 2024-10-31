!#/usr/bin/python3
'''
This module will be used to lists all states from the database hbtn_0e_0_usa
'''

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", 
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC;")
    '''
    Execute this SQL command
    '''
    
    for state in cursor.fetchall():
        print(state)

    cursor.close()
    db.close()
