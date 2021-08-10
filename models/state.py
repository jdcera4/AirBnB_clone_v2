#!/usr/bin/python3
""" State Module for HBNB project """
from models import city
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship, backref
from os import getenv
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref=backref(
            "state", cascade="all, delete"))
    else:
        @property
        def cities(self):
            """the geter of cities"""
            from models.city import City
            objs = models.storage.all(City)
            new_list = []
            for city in objs.values():
                if city.state_id == self.id:
                    new_list.append(city)
            return new_list