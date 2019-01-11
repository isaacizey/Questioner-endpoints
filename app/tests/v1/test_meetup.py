"""this module tests the meetups endpoint """

import json
import unittest
from app import app 

class TestMeetupEndpoint(unittest.TestCase):
    """this class handles testing for the meetups endpoint"""

    def setUp(self):
        """code executed befor each test"""
        app.testing = True
        self.app =  app.test_client()

