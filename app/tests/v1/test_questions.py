"""File to test all Questions endpoints"""
import unittest
import json
from app import create_app
from app.api.v1.models.questions_models import QuestionsModel

APP = create_app()

all_meetups_url = 'http://localhost:5000/api/v1/meetups'
specific_meetup_url = 'http://localhost:5000/api/v1/meetups/1'
post_question_url = 'http://127.0.0.1:5000/api/v1/questions'
question_id = 1 

class TestQuestions(unittest.TestCase):
    """This Class will test all Questions endpoints """

    def setUp(self):
        """Setup the test values"""
        APP.testing = True
        self.app = APP.test_client()

    def test_all_questions(self):
        """ Methods that test all questions endpoints """
        data =  {
        "user" : 1,
        "meetup" : "be the best you there can be",
        "title" : "Rehumanizing humans",
        "body" : "Is this happening tomorow ?"
            }
        response = self.app.post(post_question_url, data=json.dumps(data), content_type="application/json")
        output = json.loads(response.data.decode("UTF-8"))

        self.assertEqual(output["status"], 201)
        self.assertEqual(output["message"], "Question created successfully!")
        self.assertEqual(response.status, "200 OK")
        self.assertTrue(response.content_type == "application/json")
    
   