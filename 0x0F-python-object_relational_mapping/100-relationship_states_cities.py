#!/usr/bin/python3
"""This script creeates the State “California” with the City “San Francisco” from the database.
"""
import sys
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]), 
                            pool_pre_ping=True)
    Base.metadata.create_all(engine)

    state = State(name='California')
    city = City(name='San Francisco', state_id=state.id)

    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(city)
    # session.commit()

    session.close()