from flask import Blueprint, make_response, request, jsonify
from ..models import users_models
from .. import version1 

@version1.route("/login", methods=["POST", "GET"]) 



def user_login():
    try:

        """ Method for user login """
        data = request.get_json()

        
        if not data:
            return jsonify({
                'message': "Please fill in all data!",
                'status': 401
                })
        elif data["email"] == "email" and data["password"] == "password":
            return jsonify({"status": 201, "message": "Authenticstion successful !"})

        elif data["email"] == "" or data["password"] == "":
            return jsonify({
                'message': "Please fill in all fields!",
                'status': 401
                })
        else:
            
            return jsonify({
                'message': "Unknown error!",
                'status': 401
                })
    except :
        pass
