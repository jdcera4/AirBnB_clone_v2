#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
from models.base_model import BaseModel


class test_state(test_basemodel):
    """ Class to test the state atributtes """
    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.state = State()
        cls.state.name = "CA"

    @classmethod
    def teardownClass(cls):
        """at the end of the test this will tear it down"""
        del cls.state

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_attributes_State(self):
        """chekcing if State have attributes"""
        # self.assertTrue('id' in self.state.__dict__)
        # self.assertTrue('created_at' in self.state.__dict__)
        # self.assertTrue('updated_at' in self.state.__dict__)
        self.assertTrue('name' in self.state.__dict__)

    def test_is_subclass_State(self):
        """test if State is subclass of BaseModel"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_attribute_types_State(self):
        """test attribute type for State"""
        self.assertTrue(hasattr(self.state, "name"))
        #self.assertEqual(type(self.state.name), str)
        #self.assertTrue(self.state.name == "CA")
    # def test_save_State(self):
    #     """test if the save works"""
    #     self.state.save()
    #     self.assertNotEqual(self.state.created_at, self.state.updated_at)

    # def test_to_dict_State(self):
    #     """test if dictionary works"""
    #     self.assertEqual('to_dict' in dir(self.state), True)
