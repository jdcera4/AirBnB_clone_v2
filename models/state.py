#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship, backref


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref=backref(
        "state", cascade="all, delete"))

    # @property
    # def cities(self):
    #     """the geter of cities"""
    #     return State.cities

    # @cities.setter
    # def cities(self):
    #     """gives a list with all the cities"""
    #     pass
