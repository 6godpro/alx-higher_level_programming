#!/usr/bin/python3
"""Lists all City objects from the database hbtn_0e_101_usa,
   in the format <city id>: <city name> -> <state name>

   Usage: ./prog_name username password database name
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for city in session.query(City).join(State) \
            .filter(State.id == City.state_id).all():
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
