#!/usr/bin/python3
"""This script deletes all State objects in the database
   containing the letter 'a'.
"""
import sys
from model_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).all():
        if 'a' in state.name:
            session.delete(state)

    session.commit()
    session.close()
