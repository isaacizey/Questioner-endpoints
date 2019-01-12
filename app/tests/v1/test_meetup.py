"""File to test all meetup endpoints"""
import unittest
import json
from app import create_app
from app.api.v1.models.meetups_model import MeetupModel

APP = create_app()

all_meetups_url = 'http://localhost:5000/api/v1/meetups'
specific_meetup_url = 'http://localhost:5000/api/v1/meetups/1'

class TestMeetups(unittest.TestCase):
    """This Class will test all meetup endpoints """

    def setUp(self):
        """Setup the test values"""
        APP.testing = True
        self.app = APP.test_client()


    def test_all_meetups(self):
        """Method to test get all meetups endpoint"""
        data = {
            "meetup_id": 1,
            "location": "Safari Park", 
            "topics": "Tech teach us", 
            "happeningOn": "3/9/2019", 
            "tags": "Ai, machine learning"
            }
        response = self.app.post(all_meetups_url, data=json.dumps(data), content_type="application/json")
        output = json.loads(response.data.decode("UTF-8"))

        self.assertEqual(output["status"], 201)
        self.assertEqual(output["message"], "New meetup created successfully!")
        self.assertEqual(response.status, "200 OK")
        self.assertTrue(response.content_type == "application/json")

    

    


if __name__ == '__main__':
    unittest.main()
