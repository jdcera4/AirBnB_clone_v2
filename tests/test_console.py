#!/usr/bin/python3
''' Test suite for the console'''

import os
import sys
import models
import unittest
from io import StringIO
from console import HBNBCommand
from unittest.mock import create_autospec
import os

class test_console(unittest.TestCase):
    """ Test the console module """

    def setUp(self):
        '''setup for'''
        self.backup = sys.stdout
        self.capt_out = StringIO()
        sys.stdout = self.capt_out

    def tearDown(self):
        ''''''
        sys.stdout = self.backup

    def create(self):
        """ create instance of HBNBCommand class """
        return HBNBCommand()

    def test_EOF(self):
        """ Test EOF exist """
        cosnole = self.create()
        self.assertTrue(console.onecmd("EOF"))

    def test_quit(self):
        """ test quit exists """
        cosnole = self.create()
        self.assertTrue(console.onecmd("quit"))

    def test_all(self):
        """ Test all exist """
        cosnole = self.create()
        console.onecmd("all")
        self.assertTrue(isinstance(self.capt_out.getvalue(), str))
