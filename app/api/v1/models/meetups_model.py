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