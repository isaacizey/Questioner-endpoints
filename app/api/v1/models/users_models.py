from flask import request
Users = [
    {
        "user_name" : "msee",
        "first_name" : "john",
        "last_name" : "james",
        "email" : "j.james@andela.com",
        "password" : "1234qwer"
    }
    ]

class UserModels(object):

    def __init__(self):
        self.db = Users


    def user_login(self, email, password):

        """ This method imlements user registration endpoints """
        login_payload = {
            "email" : email,
            "password" : password
        }
    def user_registration(self,user_name,last_name, email,password,first_name  ):
        """ This method implement the users registration  models  """
        user_payload = {
            "user_name" : user_name,
            "first_name" : first_name,
            "last_name" : last_name,
            "email" : email,
            "password" : password
        }
        self.db.append(user_payload)
        return self.db

