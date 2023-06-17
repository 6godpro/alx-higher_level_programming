#!/usr/bin/python3
"""This script displays all cities from the database 'hbtn_0e_4_usa'.
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    try:
        db = MySQLdb.connect(host='localhost', user=argv[1],
                             passwd=argv[2], db=argv[3])
    except Exception as e:
        if type(e) == IndexError:
            print("USAGE: /0-select_states.py user password db_name")
        else:
            print(e.args[1])
        exit(1)

    cursor = db.cursor()
    cursor.execute("SELECT c.id, c.name, s.name \
                    FROM cities AS c \
                    INNER JOIN states AS s \
                    ON s.id = c.state_id \
                    ORDER BY c.id")
    [print(row) for row in cursor.fetchall()]
    cursor.close()
