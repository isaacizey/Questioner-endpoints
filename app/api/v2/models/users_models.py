from flask import request, make_response
import jwt
import psycopg2 as psycopg
import app.db_connect as connection
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

conn = connection.get_connection()
db_cursor = conn.cursor()


class UserModels(object):

    def __init__(self):
       """ Initialization of the UserModels class """


    def user_login(self, user_name, password):

        """ This method imlements user registration endpoints """
        auth = request.authorization
        if not auth or not auth.user_name or not auth.password:
            return make_response('Could not verify', 401, 
            {'WWW-Authenticate' : 'Basic realm="Login required!"'})

        user = User.query.filter_by(name=auth.username).first()

        if not user:
            return make_response('Could not verify', 401, 
            {'WWW-Authenticate' : 'Basic realm="Login required!"'})

        if check_password_hash(user.password, auth.password):
            
            token = jwt.encode({'user_name': user_name, 
            'exp' : datetime.datetime.utcnow() + 
            datetime.timedelta(minutes=60)}, SECRET_KEY,  algorithm='HS256')
            return jsonify({'token' : token.decode('UTF-8')})
        return make_response('Could not verify', 401, 
        {'WWW-Authenticate' : 'Basic realm="Login required!"'})

            
    

   
    
    def user_registration(self, user_name, last_name, email, password, 
        first_name ):
        """ This method implement the users registration  models  """

        query = """ INSERT INTO USERS (user_name, first_name, last_name, email,
        password)VALUES('{}','{}','{}','{}','{}'); """ .format(user_name, 
        last_name, email, generate_password_hash(password), first_name)
        user_payload = {
            'user_name' : user_name,
            'first_name' : first_name,
            'last_name' : last_name,
            'email' : email,
            'password' : generate_password_hash(password)
        }

        db_cursor.execute(query)
        return user_payload

       


       

    

