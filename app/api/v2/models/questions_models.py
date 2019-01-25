import datetime
from datetime import datetime as dt
import app.db_connect as connection
import psycopg2 as psycopg
from flask import jsonify

db_conn = connection.get_connection()
db_cursor = db_conn.cursor()

class QuestionsModel():

    """ This class contains models for questions """
    def __init__(self):
        """ This method gets a specific question"""

    def single_question(self, question_id):
        questions = self.all_questions()
        if len(questions) == 0:
            return False
        for question in questions:
            if question["question_id"] == question_id:
                return question
    
    @staticmethod
    def all_questions():
        """ This method returns all questions in the database """
        sql = "SELECT * FROM QUESTIONS"

        db_cursor.execute(sql)
        question_results = db_cursor.fetchall()
        questions = []

        for question in questions:
            question_results = {
                "question_id" : question_results[0],
                "meetup_id" : question_results[1],
                "question_body" : question_results[2],
                "question_title" : question_results[3],
                "user_id" : question_results[4],
                "votes" : question_results[5]
            }
            questions.append(question_results)
        return questions

            

    def add_question(self, user, meetup_id, title,body_text,votes):
        
        """ Questioner endpoints for questions """
        query = """ INSERT INTO  QUESTIONS (user_id, meetup_id, 
        question_title, question_body, question_votes ) VALUES 
        ('{}','{}','{}','{}','{}');""".format(user,meetup_id, 
        title, body_text, votes)

        db_cursor.execute(query)
        db_conn.commit()

        output =  {
                "user" : user,
                "meetup_id" : meetup_id,
                "title" : title,
                "body_text" : body_text
        }
            
    
        return output
    
        

    def upvote_question(self, question_id):

        new_votes = 0
        my_question = self.single_question(question_id)
        if my_question:
            my_question["votes"] += 1
            new_votes =  my_question["votes"] 
            sql = "UPDATE QUESTIONS SET VOTES = new_votes WHERE question_id = question_id" 
            db_cursor.execute(sql)
            db_conn.commit()

            return my_question
        return False
    def downvote_question(self, question_id):

        """ This model downvotes a question """
        new_votes = 0
        my_question = self.single_question(question_id)
        if my_question:
            my_question["votes"] -= 1
            new_votes =  my_question["votes"] 
            sql = "UPDATE QUESTIONS SET VOTES = new_votes WHERE question_id = question_id" 
            db_cursor.execute(sql)
            db_conn.commit()

            return my_question
        return False
    
    def add_comment(self, question, title, body, comment):
        """ This method add comments to the comments database """
        query = """ INSERT INTO COMMENTS (question, title, body, comment) 
        VALUES ('{}','{}','{}','{}');""".format(question, title, body, comment)
 
        
        db_cursor.execute(query)
        db_conn.commit()

        output = {
            "question" : question,
            "title" : title,
            "body" : body,
            "comment" : comment
        }

        return output
    

    


