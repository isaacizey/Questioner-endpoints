from flask import Blueprint, make_response, request, jsonify
from ..models import users_models
from .. import version2 
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import datetime
from functools import wraps 

from  app.api.v2.utils import validations

validate = validations.Validations()
SECRET_KEY = "thisismyawesomekey"



def requires_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401

        try: 
            data = jwt.decode(token, SECRET_KEY)
            current_user = User.query.filter_by(
                public_id=data['public_id']).first()
        except:
            return jsonify({'message' : 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated

@version2.route("/auth/login", methods=["POST", "GET"]) 

def user_login():
    #try:

        """ This method implements login views """
    
        auth = request.authorization

        if not auth or not auth.username or not auth.password:
            return make_response('Could not verify 1', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

        user = {'username' : 'isaac', 'password' :'password'}
        

        if not user:
            return make_response('Could not verify 2', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

        if user["password"] == auth.password:
            token = jwt.encode({'username':user["username"] , 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, SECRET_KEY)

            return jsonify({'token' : token.decode('UTF-8')})

        return make_response('Could not verify 3', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})
    

@version2.route("auth/register", methods = ["POST"])
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


    

@version2.errorhandler(404)
def UnknownRequest(e):
    return jsonify({
                'message': "Unknown error!",
                'status': 404
                })
