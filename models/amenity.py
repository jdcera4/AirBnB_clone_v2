#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String
from sqlalchemy.orm import relationship, backref


class Amenity(BaseModel):
    """the class of amenity"""
    name = ""
    # from models.place import place_amenity
    # __tablename__ = 'amenities'
    # name = Column(String(128), nullable=False)
    # place_amenities = relationship(
    #     "Place", secondary=place_amenity, back_populates="amenities")
