"""Class to include validations"""
import re
import datetime

class Validations():
    """This class contains validation for views"""
   

    def email_validate(self, email):
        """ Validates email """
        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email) is None:
            return False
        return True

    def numeric_validate(self, text):
        """ Ensures value is an integer """
        if isinstance(text, int):
            return True
        return False

    def string_validate(self, text):
        """ checks if value is a string """
        if isinstance(text, str):
            return True
        return False

    

    