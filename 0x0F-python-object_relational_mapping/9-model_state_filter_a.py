#!/usr/bin/python3
"""This script displays the states containing the letter 'a'.
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    [print("{}: {}".format(state.id, state.name))
     for state in session.query(State).all()
     if 'a' in state.name]

    session.close()
