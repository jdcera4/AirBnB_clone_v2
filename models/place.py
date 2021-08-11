#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy.sql.schema import Column, ForeignKey, Table
from sqlalchemy.sql.sqltypes import Float, Integer, String
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy.orm import relationship, backref
import models

metadata = Base.metadata
place_amenity = Table("place_amenity", metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref=backref(
            "place", cascade="all, delete"))
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            """the geter of cities"""
            from models.review import Review
            objs = models.storage.all(Review)
            new_list = []
            for review in objs.values():
                if review.place_id == self.id:
                    new_list.append(review)
            return new_list

        @property
        def amenities(self):
            """ the getter of amenities """
            amenity_obj = []
            for amenity_id in self.amenity_ids:
                key = 'Amenety.' + amenity_id
                if key in FileStorage.__objects[key]:
                    amenity_obj.append(FileStorage.__objects[key])
            return amenity_obj

        @amenities.setter
        def amenities(self, obj):
            """ Setter of amenities """
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
