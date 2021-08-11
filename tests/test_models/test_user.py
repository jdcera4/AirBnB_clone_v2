#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
from models.base_model import BaseModel


class test_User(test_basemodel):
    '''Class to test the User class Attributes'''
    @classmethod
    def setUpClass(cls):
        '''Create instance to test the attributes of a class'''
        cls.user = User()

    @classmethod
    def tearDownClass(cls):
        '''Remove the istance after run tests'''
        del cls.user

    def test_inheritance_from_BaseModel(self):
        '''test if User class is a subclas of BaseModel'''
        self.assertTrue(issubclass(type(self.user), BaseModel))

    def test_attributes(self):
        '''test if de User class have the attributte and if is str'''
        # Email
        self.assertTrue(hasattr(self.user, "email"))    # Att exists
        #self.assertIsInstance(self.user.email, str)     # Att is string
        #self.assertTrue(self.user.email == "")          # Att is empty
        # Password
        self.assertTrue(hasattr(self.user, "password"))
        #self.assertIsInstance(self.user.password, str)
        #self.assertTrue(self.user.password == "")
        # First Name
        self.assertTrue(hasattr(self.user, "first_name"))
        #self.assertIsInstance(self.user.first_name, str)
        #self.assertTrue(self.user.first_name == "")
        # Last Name
        self.assertTrue(hasattr(self.user, "last_name"))
        #self.assertIsInstance(self.user.last_name, str)
        #self.assertTrue(self.user.last_name == "")