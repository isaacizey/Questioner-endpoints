"""File to test all meetup endpoints"""
import unittest
import json
from app import create_app
from app.api.v1.models.meetups_model import MeetupModel

APP = create_app()

all_meetups_url = 'http://localhost:5000/api/v1/meetups'
specific_meetup_url = 'http://localhost:5000/api/v1/meetups/1'
new_meet_url = 'http://localhost:5000/api/v1/meetups'
upcomming_meetups_url = 'http://localhost:5000/api/v1/meetups/upcoming'
meetup_id = 1 
test_data = {
           
            "location": "Safari Park", 
            "topics": "Tech teach us", 
            "happeningOn": "3/9/2019",
            "tags": "Ai, machine learning"
            }

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

        self.assertEqual(output["status"], 404)
        self.assertEqual(output["message"], "Unknown error!")
        self.assertEqual(response.status, "200 OK")
        self.assertTrue(response.content_type == "application/json")

    def test_specific_meetup(self):
            """Method to test get specific meetup endpoint"""
            
            self.app.post(all_meetups_url, data=json.dumps(test_data), content_type="application/json")
            results = self.app.get(specific_meetup_url)
            result1 = json.loads(results.data.decode("UTF-8"))

            self.assertEqual(result1["status"], 200)
            self.assertEqual(results.status_code, 200)
            self.assertEqual(results.status, "200 OK")
            self.assertTrue(results.content_type == "application/json")
    
    def test_creating_meetup(self):
        """ This method tests adding a new meetup record """

        response = self.app.post(new_meet_url, data=json.dumps(test_data), content_type="application/json")
        result = json.loads(response.data.decode("UTF-8"))

        self.assertEqual(result["message"], "Unknown error!")
        self.assertEqual(result["status"], 404)
        self.assertEqual(response.status, "200 OK")
        self.assertTrue(response.content_type == "application/json")

    
    def test_upcomming_meetups(self):
        """ This method test all the upcomming meetups """    

        response = self.app.get(upcomming_meetups_url, data=json.dumps(test_data), content_type="application/json")
        result = json.loads(response.data.decode("UTF-8"))

        
        self.assertEqual(result["status"], 200)
        self.assertEqual(response.status, "200 OK")
        self.assertTrue(response.content_type == "application/json")

def test_specific_meetup(self):
            """Method to test get specific meetup endpoint"""
            
            self.app.post(all_meetups_url, data=json.dumps(test_data), content_type="application/json")
            results = self.app.get(specific_meetup_url)
            result1 = json.loads(results.data.decode("UTF-8"))

            self.assertEqual(result1["status"], 200)
            self.assertEqual(results.status_code, 200)
            self.assertEqual(results.status, "200 OK")
            self.assertTrue(results.content_type == "application/json")
    
def test_creating_meetup(self):
    
    """ This method tests adding a new meetup record """

    response = self.app.post(new_meet_url, data=json.dumps(test_data), content_type="application/json")
    result = json.loads(response.data.decode("UTF-8"))

    self.assertEqual(result["message"], "New meetup created successfully!")
    self.assertEqual(result["status"], 201)
    self.assertEqual(response.status, "200 OK")
    self.assertTrue(response.content_type == "application/json")


def test_upcomming_meetups(self):
    """ This method test all the upcomming meetups """    

    response = self.app.get(upcomming_meetups_url, data=json.dumps(test_data), content_type="application/json")
    result = json.loads(response.data.decode("UTF-8"))

    
    self.assertEqual(result["status"], 200)
    self.assertEqual(response.status, "200 OK")
    self.assertTrue(response.content_type == "application/json")



    

    

    


if __name__ == '__main__':
    unittest.main()

