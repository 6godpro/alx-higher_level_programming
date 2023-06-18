#!/usr/bin/python3
"""This script contains the definition of a City class.
"""
from sqlalchemy import Sequence, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Represents a City object.

    __tablename__ (string): The name of the table.
    id (int): The id of the City object.
    name (string): The name of the City object.
    state_id (int): The Foreign key column referencing the states
                    table.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
