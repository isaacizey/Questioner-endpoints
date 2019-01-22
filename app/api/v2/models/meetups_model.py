import datetime
from datetime import datetime as dt

  conn = get_connection()
  db_cursor = conn.cursor()
  db_cursor.execute(post_data())
    
    conn.commit()

class MeetupModel(object):
    '''models for meetups class'''

    def __init__(self):
        self.db = Meetups
       
    def add_meetup(self, id, location, happeningOn, images, topics, tags ):

        ''' This method saves a meetup into a dictionary '''
        self.id = id
        self.location = location
        self.happeningOn = happeningOn
        self.images = images
        self.topics = topics
        self.tags = tags

       
        query = """
                INSERT INTO table_name ('id', 'location', 'happenningOn', 'images', 'topics', 
                'tags')VALUES('{}','{}','{}');""".format(self.id,self.location, self.happeningOn,
                 self.images, self.topics )
        
        return query

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




        

        
