import unittest

import json
from app import create_app
from app.api.v1.models.meetups_model import MeetupModel
from app.api.v1.models.users_models import UserModels

register_url = 'http://localhost:5000/api/v1/auth/register'
login_url = 'http://localhost:5000/api/v1/auth/login'

APP = create_app()

test_data = [
    {
        "user_name" : "msee",
        "first_name" : "john",
        "last_name" : "james",
        "email" : "j.james@andela.com",
        "password" : "1234qwer"
    }
]
 

class TestUsers(unittest.TestCase):
    """This Class will test all users endpoints """

    def setUp(self):
        """Setup the test values"""
        APP.testing = True
        self.app = APP.test_client()


    


if __name__ == '__main__':
    unittest.main()
