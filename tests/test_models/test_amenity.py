#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from models.base_model import BaseModel


class test_Amenity(test_basemodel):
    '''Class to test the Amenity class Attributes'''
    @classmethod
    def setUpClass(cls):
        '''Create instance to test the attributes of a class'''
        cls.amenity = Amenity()

    @classmethod
    def tearDownClass(cls):
        '''Remove the istance after run tests'''
        del cls.amenity

    def test_inheritance_from_BaseModel(self):
        '''test if User class is a subclas of BaseModel'''
        self.assertTrue(issubclass(type(self.amenity), BaseModel))

    def test_attributes(self):
        '''test if de Amenity class have the attributte and if is str'''
        # Email
        self.assertTrue(hasattr(self.amenity, "name"))    # Att exists
        #self.assertIsInstance(self.amenity.name, str)     # Att is string
        #self.assertTrue(self.amenity.name == "")          # Att is empty
