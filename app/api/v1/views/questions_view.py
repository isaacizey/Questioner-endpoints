""" Views for questions """

from flask import Blueprint, make_response
from app.api.v1.models.questions_models import Questions
from app.api.v1.models import questions_models
from app.api.v1.models.questions_models import QuestionsModel
from app.api.v1 import version1
from flask import Flask, request, jsonify

from app.api.v1.models import meetups_model
db = QuestionsModel()
question_id = 1
votes = 0 


@version1.route("/questions", methods=["POST"])

def post_questions():
    try:
                """ Get questions on a spcific meetup """

            
                data = request.get_json()

                if not data:
                    return jsonify({
                        'message' : "Could not find any data, probably left some fields empty",
                        'status' : 401
                    })
                new_question = questions_models.QuestionsModel().add_question(data['meetup'], data['title'], 
                            data['body'])
                return jsonify({"status": 201, "message": "Question created successfully!", "data": new_question})
    
        
            

    except Exception as e:

        return jsonify({
                    'message': "Unknown error!",
                    'status': 401
                    })

@version1.route("/question/<question_id>", methods=["GET"])
def get_single_question(question_id):
    try:

        """ This get a single question """
        question = questions_models.QuestionsModel().single_question(question_id)
        if question:
            return jsonify ({
                'status': 200, 'data' : question
            })
        return jsonify({"status": 404, "message": "No meetup found!"})
    except Exception as e:

        return jsonify({
                    'message': "Unknown error!",
                    'status': 401
                    })





@version1.route("/questions/<question_id>/upvote", methods=["PATCH"])
def upvote_question(question_id):
    try:
        """ Views for upvoting a question """
        data = request.get_json()

        if len(Questions) == 0: 
            return jsonify({"status": 404, "message": "No questions found!"})
        my_question = get_single_question(question_id)
        if my_question:
            return jsonify ({
                'status': 201, 'message' : "vote added"
            })
            
        return jsonify({"status": 404, "message": "Can't find question"})
    
    except Exception as e:

        return jsonify({
                    'message': "Unknown error!",
                    'status': 401
                    })

@version1.route("/questions/<question_id>/downvote", methods=["PATCH"])
def downvote_question(question_id):

    try:
        """ Views for upvoting a question """
        data = request.get_json()

        if len(Questions) == 0: 
            return jsonify({"status": 404, "message": "No questions found!"})
        my_question = get_single_question(question_id)
        if my_question:
            return jsonify ({
                'status': 201, 'message' : "vote subtracted successfully!"
            })
        return jsonify({"status": 404, "message": "Specified question was not found!"})
    
    except Exception as e:

        return jsonify({
                    'message': "Unknown error!",
                    'status': 401
                    })




 

   