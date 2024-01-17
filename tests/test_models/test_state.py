#!/usr/bin/python3
"""
Class that defines test_state
"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """
    Class that defines test_state.
    """
    def test_name3(self):
        """
        check state name inserted into the db.
        """
        new = self.value()
        self.assertEqual(type(new.name), str)
