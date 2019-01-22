Questions = [
     {
            "body ": "Is this happening tomorow ?",
            "question_id": 1,
            "meetup_id": 1,
            "title": "Rehumanizing humans",
            "user": 1,
            "votes": 0
        }
]
user = 1
votes = 1
class QuestionsModel():

    """ This class contains models for questions """
    def __init__(self):
        self.db = Questions

    def single_question(self, question_id):
        if len(Questions) == 0:
            return False
        for question in Questions:
            if question["question_id"] == question_id:
                return question
            return False   

    def add_question(self, meetup_id, title,body_text):
        
        """ Questioner endpoints for questions """
        output =  {
                "user" : user,
                "question_id" : len(self.db) + 1,
                "meetup_id" : meetup_id,
                "title" : title,
                "body_text" : body_text
        }
            
        self.db.append(output)
        return self.db

        

    def upvote_question(self, question_id):

        """ This model upvotes a question """
        if len(Questions) == 0:
            return False
        my_question = self.single_question(question_id)
        if my_question:
            my_question["votes"] += 1
            return my_question
        return False

    def downvote_question(self, question_id):

        """ This model downvotes a question """
        if len(Questions) == 0:
            return False
        my_question = self.single_question(question_id)
        if my_question:
            my_question["votes"] -= 1
            return my_question
        return False
    

    


