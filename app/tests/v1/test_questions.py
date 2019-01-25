"""File to test all Questions endpoints"""
import unittest
import json
from app import create_app
from app.api.v1.models.questions_models import QuestionsModel

APP = create_app()

all_meetups_url = 'http://localhost:5000/api/v1/meetups'
specific_meetup_url = 'http://localhost:5000/api/v1/meetups/1'
post_question_url = 'http://127.0.0.1:5000/api/v1/questions'
downvote_question_uri = 'http://127.0.0.1:5000/api/v1/questions/1/downvote'
upvote_question_uri = 'http://127.0.0.1:5000/api/v1/questions/1/upvote'

question_id = 1 
test_data =  {
        "user" : 1,
        "question_id" : 1,
        "meetup" : "be the best you there can be",
        "title" : "Rehumanizing humans",
        "body" : "Is this happening tomorow ?",
        "votes" : 0 
            }

class TestQuestions(unittest.TestCase):
    """This Class will test all Questions endpoints """

    def setUp(self):
        """Setup the test values"""
        APP.testing = True
        self.app = APP.test_client()

    def test_all_questions(self):
        """ Methods that test all questions endpoints """
        
        response = self.app.post(post_question_url, data=json.dumps(test_data), content_type="application/json")
        output = json.loads(response.data.decode("UTF-8"))

        self.assertEqual(output["status"], 404)
        self.assertEqual(output["message"], "Unknown error!")
        self.assertEqual(response.status, "200 OK")
        self.assertTrue(response.content_type == "application/json")

    def test_create_new_question(self):
     
        """ This method tests adding a new question """

        response = self.app.post(post_question_url, data=json.dumps(test_data), content_type="application/json")
        result = json.loads(response.data.decode("UTF-8"))

        self.assertEqual(result["message"], "Unknown error!")
        self.assertEqual(result["status"], 404)
        self.assertEqual(response.status, "200 OK")
        self.assertTrue(response.content_type == "application/json")

    def test_upvote_question(self):
        """ this tests the upvote question endpoint """
        response = self.app.patch(upvote_question_uri, data=json.dumps(test_data), content_type="application/json")
        result = json.loads(response.data.decode("UTF-8"))

        self.assertEqual(result["message"], "Can't find question")
        self.assertEqual(result["status"], 404)
        self.assertEqual(response.status, "200 OK")
        self.assertTrue(response.content_type == "application/json")

    def test_downvote_question(self):
        """ this tests the upvote question endpoint """
        
        response = self.app.patch(downvote_question_uri,data=json.dumps(test_data), content_type="application/json")
        result = json.loads(response.data.decode("UTF-8"))

        self.assertEqual(result["message"], "Unknown error!")
        self.assertEqual(result["status"], 404)
        self.assertEqual(response.status, "200 OK")
        self.assertTrue(response.content_type == "application/json")

    
 
    
        



    
   