#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
from models.base_model import BaseModel


class test_Place(test_basemodel):
    '''Class to test the Place class Attributes'''
    @classmethod
    def setUpClass(cls):
        '''Create instance to test the attributes of a class'''
        cls.place = Place()

    @classmethod
    def tearDownClass(cls):
        '''Remove the istance after run tests'''
        del cls.place

    def test_inheritance_from_BaseModel(self):
        '''test if place class is a subclas of BaseModel'''
        self.assertTrue(issubclass(type(self.place), BaseModel))

    def test_attributes(self):
        '''test if de place class have the attributte and if is str'''
        # user_id
        self.assertTrue(hasattr(self.place, "user_id"))    # Att exists
        #self.assertIsInstance(self.place.user_id, str)     # Att is string
        #self.assertTrue(self.place.user_id == "")
        # city_id
        self.assertTrue(hasattr(self.place, "city_id"))
        #self.assertIsInstance(self.place.city_id, str)
        #self.assertTrue(self.place.city_id == "")
        # name
        self.assertTrue(hasattr(self.place, "name"))
        #self.assertIsInstance(self.place.name, str)
        #self.assertTrue(self.place.name == "")
        # description
        self.assertTrue(hasattr(self.place, "description"))
        #self.assertIsInstance(self.place.description, str)
        #self.assertTrue(self.place.description == "")
        # number_rooms
        self.assertTrue(hasattr(self.place, "number_rooms"))
        #self.assertIsInstance(self.place.number_rooms, int)
        #self.assertTrue(self.place.number_rooms == 0)
        # number_bathrooms
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        #self.assertIsInstance(self.place.number_bathrooms, int)
        #self.assertTrue(self.place.number_bathrooms == 0)
        # max_guest
        self.assertTrue(hasattr(self.place, "max_guest"))
        #self.assertIsInstance(self.place.max_guest, int)
        #self.assertTrue(self.place.max_guest == 0)
        # price_by_night
        self.assertTrue(hasattr(self.place, "price_by_night"))
        #self.assertIsInstance(self.place.price_by_night, int)
        #self.assertTrue(self.place.price_by_night == 0)
        # latitude
        self.assertTrue(hasattr(self.place, "latitude"))
        #self.assertIsInstance(self.place.latitude, float)
        #self.assertTrue(self.place.latitude == 0.0)
        # longitude
        self.assertTrue(hasattr(self.place, "longitude"))
        #self.assertIsInstance(self.place.longitude, float)
        #self.assertTrue(self.place.longitude == 0.0)
        # amenity_ids
        self.assertTrue(hasattr(self.place, "amenity_ids"))
        #self.assertIsInstance(self.place.amenity_ids, list)
       # self.assertTrue(self.place.amenity_ids == [])
