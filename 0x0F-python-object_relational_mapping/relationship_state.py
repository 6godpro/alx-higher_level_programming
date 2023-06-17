#!/usr/bin/python
"""This module contains the class definition of a State."""
from relationship_city import Base, City
from sqlalchemy import Sequence, Column, Integer, String
from sqlalchemy.orm import relationship


class State(Base):
    """Represents a state object."""

    __tablename__ = 'states'

    id = Column(Integer, Sequence('state_id_seq'), primary_key=True)
    name = Column(String(128), nullable=False)

