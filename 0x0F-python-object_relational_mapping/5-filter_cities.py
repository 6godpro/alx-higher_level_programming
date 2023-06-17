#!/usr/bin/python3
"""This script displays cities based on the name of state
   provided as argument.
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    try:
        db = MySQLdb.connect(host='localhost', user=argv[1],
                             passwd=argv[2], db=argv[3])
        state = argv[4]
    except Exception as e:
        if type(e) == IndexError:
            print("USAGE: prog_name user password db_name state_name")
        else:
            print(e.args[1])
        exit(1)

    cursor = db.cursor()
    cursor.execute("SELECT c.id, c.name, s.name \
                    FROM cities AS c \
                    INNER JOIN states AS s \
                    ON s.id = c.state_id \
                    ORDER BY c.id")
    print(', '.join([row[1] for row in cursor.fetchall()
          if row[2] == state]))
    cursor.close()
