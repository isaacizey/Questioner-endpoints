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

        sql = "SELECT * FROM USERSTABLE"

        db_cursor.execute(sql)
        users_result = db_cursor.fetchall()
        users = []


        for user_value in users_result:
            user_value = {
                
                "location" : user_value[0],
                "happeningOn" : user_value[1],
                "topics" : user_value[2]

            }
            users.append(user_value)

        return users
       

            
    

   
    
    def user_registration(self, user_name, last_name, email, password, 
        first_name ):
        """ This method implement the users registration  models  """

        query = """ INSERT INTO USERS (username, firstname, lastname, email,
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
        conn.commit()
        return user_payload

       

       

    

