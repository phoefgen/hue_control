#!/bin/python
'''Unit tests for the start module '''

import unittest
import app.start

class TestStart(unittest.TestCase):
    '''Runs all unit tests for the start.py module '''

    def test_start_returns_string(self):
        '''Tests that the hello method returns a string '''

        self.assertIsInstance(app.start.hello(), str)
        return


    def test_create_user(self):
        ''' Create user function test.
        expects: Bridge IP
        returns: Registered Username'''

        self.assertIsInstance(app.start.create_user('192.'))