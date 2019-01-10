   
"""model for view for meetups"""
import datetime

from flask import jsonify,request
from flask_restful import Resource

meetups = []


class MeetupsModel():
    """Class with methods to perform CRUD operations on the DB"""

    def __init__(self):
        self.db = meetups
        if len(meetups) == 0:
            self.id = 1
        else:
            self.id = meetups[-1]['id'] + 1
        self.id = len(meetups) + 1

    def save(self):
        data = {
            'id': self.id,
            'createdOn': datetime.datetime.utcnow(),
            'location': request.json.get('location'),
            'Topic': request.json.get('topic'),
            'happeningOn': request.json.get('happeningOn'),
            'tags': request.json.get('tags')
        }

        self.db.append(data)
        return self.id

    def get_all(self):
        return self.db