import datetime

Meetups = [ {"meetup_id": 1,
            "location": "Safari Park", 
            "topics": "Tech teach us", 
            "happeningOn": "3/9/2019",
            "tags": "Ai, machine learning",
            "happeningOn": "3/9/2019",
            "happeningOn": "3/9/2019",
            "happeningOn": "3/9/2019"} ]
meetup_id = 0

class MeetupModel(object):
    '''models for meetups class'''

    def __init__(self):
        self.db = Meetups

    def add_meetup(self, id, location, createdOn, images, topics, tags ):
        ''' This method saves a meetup into a dictionary '''
        payload = {
            "meetup_id" : len(self.db) + 1,
            "location" : location,
            "createdOn" : createdOn,
            "images" : images,
            "topics" : topics,
            "happeningOn" : datetime.datetime.now(),
            "tags" : tags
        }
        self.db.append(payload)
        return self.db

    def get_single_meetup(self, meetup_id):
        """Method to get a specific meetup"""
        if len(Meetups) == 0:
            return False
        for meetup in Meetups:
            if meetup["meetup_id"] == meetup_id:
                return meetup
    def all_meetups(self):
        """This method to gets all meetups"""

        if len(Meetups) == 0:
            return False
        return Meetups
