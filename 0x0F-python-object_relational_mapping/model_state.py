#!/usr/bin/python3
"""This module contains the class definition of a State."""
from sqlalchemy import Sequence, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a State object.

    __tablename__ (string): The name of the table to link to.
    id (int): The id of the State object.
    name (string): The name of the State object.
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
