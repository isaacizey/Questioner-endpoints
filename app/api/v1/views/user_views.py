from flask import Blueprint, make_response, request, jsonify
from ..models import users_models
from .. import version1 
from  app.api.v1.utils import validations

validate = validations.Validations()

@version1.route("/auth/login", methods=["POST", "GET"]) 

def user_login():
    try:

        """ This method implements login views """

        data = request.get_json()

            
        if not data:
            return jsonify({
                    'message': "Please fill in all data!",
                    'status': 404
                    })
        elif data["email"] == "email" and data["password"] == "password":
            return jsonify({"status": 201, "message": "Authenticstion successful !"})

        elif data["email"] == "" or data["password"] == "":
            return jsonify({
                    'message': "Please fill in all fields!",
                    'status': 404
                    })
        else:
                
            return jsonify({
                    'message': "Unknown error!",
                    'status': 404
                    })
    except Exception as e:
        return jsonify({
                'message': "Unknown error!",
                'status': 404
                })

@version1.route("auth/register", methods = ["POST"])
def user_register():

    try:
        data =  request.get_json()

        if not data:
                return jsonify({
                    'message': "All fields are required!",
                    'status': 404
                    })
        
        if validate.email_validate(data["email"]) == False:
            jsonify({"message": "That email is invalid"})
        elif validate.string_validate(data["user_name"]) == False:
            jsonify({'message': 'Username must be a string'})
        
        elif validate.string_validate(data["first_name"]) == False:
            jsonify({'message': 'First name must be a string'})

        elif validate.string_validate(data["last_name"]) == False:
            jsonify({'message': 'Last Name must be a string'})
        
        

        return jsonify({"status": 201, "message": "New meetup created successfully!", "data": new_user})

        
    
    except Exception as e:
        return jsonify({
                'message': "Unknown error!",
                'status': 404
                })


    

@version1.errorhandler(404)
def UnknownRequest(e):
    return jsonify({
                'message': "Unknown error!",
                'status': 404
                })
