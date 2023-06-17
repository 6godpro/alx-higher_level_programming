#!/usr/bin/python3
"""Lists all the states from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    try:
        db = MySQLdb.connect(host='localhost', user=argv[1],
                             passwd=argv[2], db=argv[3])
    except Exception as e:
        if type(e) == IndexError:
            print("USAGE: /0-select_states.py user password db_name")
        print(e.args[1])
        exit(1)

    cursor = db.cursor()
    cursor.execute('SELECT * FROM states ORDER BY id asc;')

    [print(row) for row in cursor.fetchall()]

    cursor.close()
