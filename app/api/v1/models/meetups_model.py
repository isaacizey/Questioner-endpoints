

Meetups = [] 


class MeetupModel(object):
    '''models for meetups class'''

    def __init__(self):
        self.db = Meetups

    def add_meetup(self, id, location, createdOn, images, topics, happeningOn, tags ):
        ''' This method saves a meetup into a dictionary '''
        payload = {
            "id" : len(self.db) + 1,
            "location" : location,
            "createdOn" : createdOn,
            "images" : images,
            "topics" : topics,
            "happeningOn" : happeningOn,
            "tags" : tags
        }
        self.db.append(payload)
        return self.db

    def single_meetup(self, meetup_id):
        """ This method returns a meetup which has the secified id"""
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

    

