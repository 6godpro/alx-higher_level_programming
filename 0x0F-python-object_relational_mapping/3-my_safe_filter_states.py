#!/usr/bin/python3
"""Lists all the states where name match a \
   search argument from the database hbtn_0e_0_usa.

   This is a modification of the previous script
   '2-my_filter_states.py'. This script is safe
   from SQL injections.

"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    try:
        db = MySQLdb.connect(host='localhost', user=argv[1],
                             passwd=argv[2], db=argv[3])
        pattern = argv[4]
    except Exception as e:
        if type(e) == IndexError:
            print("USAGE: prog_name user password db_name search_pattern")
        else:
            print(e.args[1])
        exit(1)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY `id`;")
    [print(row) for row in cursor.fetchall() if row[1] == pattern]

    cursor.close()
