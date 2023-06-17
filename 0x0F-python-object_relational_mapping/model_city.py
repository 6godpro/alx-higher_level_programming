#!/usr/bin/python3
"""This script contains the definition of a City class.
"""
from sqlalchemy import Sequence, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from model_state import State, Base


class City(Base):
    """Represents a City object
    """
    __tablename__ = 'cities'
    id = Column(Integer, Sequence("city_id_seq"), primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"))