#!/usr/bin/python3
"""This script displays the first state in the database.
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        state = session.query(State).filter_by(id=1).one()
        print("{}: {}".format(state.id, state.name))
    except Exception as e:
        print("Nothing")

    session.close()
