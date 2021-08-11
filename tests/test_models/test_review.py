#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
from models.base_model import BaseModel


class test_review(test_basemodel):
    '''Class to test the Review class Attributes'''
    @classmethod
    def setUpClass(cls):
        '''Create instance to test the attributes of a class'''
        cls.review = Review()

    @classmethod
    def tearDownClass(cls):
        '''Remove the istance after run tests'''
        del cls.review

    def test_inheritance_from_BaseModel(self):
        '''test if review class is a subclas of BaseModel'''
        self.assertTrue(issubclass(type(self.review), BaseModel))

    def test_attributes(self):
        '''test if de place class have the attributte and if is str'''
        # place_id
        self.assertTrue(hasattr(self.review, "place_id"))    # Att exists
        #self.assertIsInstance(self.review.place_id, str)     # Att is string
        #self.assertTrue(self.review.place_id == "")
        # user_id
        self.assertTrue(hasattr(self.review, "user_id"))
        #self.assertIsInstance(self.review.user_id, str)
        #self.assertTrue(self.review.user_id == "")
        # text
        self.assertTrue(hasattr(self.review, "text"))
        #self.assertIsInstance(self.review.text, str)
        #self.assertTrue(self.review.text == "")