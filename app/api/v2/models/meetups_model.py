import datetime
from datetime import datetime as dt




Meetups = [ {"meetup_id": 1,
            "location": "Safari Park", 
            "topics": "Tech teach us", 
            "happeningOn": '2019-03-19',
            "tags": "Ai, machine learning",
            "happeningOn": "2019-03-19",
            "happeningOn": "2019-03-19",
            "happeningOn": "2019-03-19"} ]
meetup_id = 0
RSVP = [
    {
                   "meetup" : "meetup_id",
                   "topic" : "topics",
                   "status" : "status"
               }
]
class MeetupModel(object):
    '''models for meetups class'''

    def __init__(self):
        self.db = Meetups
       
    def add_meetup(self, id, location, happeningOn, images, topics, tags ):
        ''' This method saves a meetup into a dictionary '''
        payload = {
            "meetup_id" : len(self.db) + 1,
            "location" : location,
            "createdOn" : datetime.datetime.now().strftime('%Y-%m-%d'),
            "images" : images,
            "topics" : topics,
            "happeningOn" :happeningOn,
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
        """This method returns a list of all meetups"""

        if len(Meetups) == 0:
            return False
        return Meetups
   

    def get_upcomming_meetups(self):
        """ This methods returns a list of all the upcomming meetups """
        
        upcomming_meetups = []
        if len(Meetups) == 0:
            return False
        for meetup in Meetups:
            event_date = dt.strptime(meetup["happeningOn"], "%Y-%m-%d")
            if event_date > datetime.datetime.now():
                upcomming_meetups.append(meetup)
        return upcomming_meetups

        
    
            
class RSVPModel(object):
    '''models for RSVP class'''

    def __init__(self):
        self.db2 = RSVP

    def rsvp_meetup(self, meetup_id, topic, status):
        """ This method returns an RSVP for a given meetup """
    
        for meetup in Meetups:
            if meetup["meetup_id"] == meetup_id:
               return meetup
               data =  {
               "meetup" : meetup_id,
                "topic" : topic,
              "status" : status
             }
            self.db2.append(data)
            return self.db2




        

        
