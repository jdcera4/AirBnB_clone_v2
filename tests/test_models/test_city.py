#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models.base_model import BaseModel


class test_City(test_basemodel):
    '''Class to test the Amenity class Attributes'''
    @classmethod
    def setUpClass(cls):
        '''Create instance to test the attributes of a class'''
        cls.city = City()

    @classmethod
    def tearDownClass(cls):
        '''Remove the istance after run tests'''
        del cls.city

    def test_inheritance_from_BaseModel(self):
        '''test if User class is a subclas of BaseModel'''
        self.assertTrue(issubclass(type(self.city), BaseModel))

    def test_attributes(self):
        '''test if de City class have the attributte and if is str'''
        # name
        self.assertTrue(hasattr(self.city, "name"))    # Att exists
        #self.assertIsInstance(self.city.name, str)     # Att is string
        #self.assertTrue(self.city.name == "")          # Att is empty
        # state_id
        self.assertTrue(hasattr(self.city, "state_id"))    # Att exists
        #self.assertIsInstance(self.city.state_id, str)     # Att is string
        #self.assertTrue(self.city.state_id == "")          # Att is empty
