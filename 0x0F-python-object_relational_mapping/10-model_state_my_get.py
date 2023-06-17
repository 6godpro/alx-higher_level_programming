#!/usr/bin/python3
"""This script displays the id of the State object
   corresponding with the state passed as argument.
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine) 
    session = Session()

    state = session.query(State).filter_by(name=sys.argv[4])
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")

    session.close()