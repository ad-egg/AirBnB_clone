#!/usr/bin/python3
"""Unittests for city"""
import datetime
import os
from pep8 import StyleGuide
import unittest
from models.base_model import BaseModel
from models.city import City


class TestClasscity(unittest.TestCase):
    """test the city class"""
    def setUp(self):
        """if file.json exists, copy contents to temp file"""
        if os.path.isfile('./file.json') is True:
            with open("file.json") as r:
                instances = r.read()
            with open("temp.json", 'w+') as w:
                w.write(instances)

    def tearDown(self):
        """
        if temp file exists, copy contents back to file.json and
        remove temp file
        """
        if os.path.isfile('./temp.json') is True:
            with open("temp.json") as r:
                instances = r.read()
            with open("file.json", 'w') as w:
                w.write(instances)
            os.remove("temp.json")
        elif os.path.isfile('./file.json') is True:
            os.remove("file.json")

    def test_style(self):
        """tests for correct pep8 style"""
        style = StyleGuide(quiet=True).check_files(["models/city.py"])
        self.assertEqual(style.total_errors, 0, "fix pep8")

    def test_subclass(self):
        """tests if subclass of BaseModel"""
        city = City()
        self.assertTrue(issubclass(city.__class__, BaseModel), True)

    def test_docstrings(self):
        """tests if docstrings exist"""
        city = City()
        self.assertTrue(len(city.__doc__) > 0)
        for method in dir(city):
            self.assertTrue(len(method.__doc__) > 0)

    def test_attribute_types(self):
        """test if attrs are correct type"""
        city = City()
        self.assertEqual(type(city.name), str)
        self.assertEqual(type(city.state_id), str)


if __name__ == '__main__':
    unittest.main()
