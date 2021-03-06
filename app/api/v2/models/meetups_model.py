import datetime
from datetime import datetime as dt
import app.db_connect as connection
import psycopg2 as psycopg
from flask import jsonify

db_conn = connection.get_connection()

db_cursor = db_conn.cursor()


    
   

class MeetupModel(object):
    '''models for meetups class'''

    def __init__(self):
        """ Initialize class """

    
        
       
    def add_meetup(self, location, happeningOn, topic, tags ):

        ''' This method saves a meetup into a dictionary '''

        query = """
                INSERT INTO MEETUPSTABLE (meetup_location, meetup_happening_on, 
                meetup_topic, meetup_tags)VALUES('{}','{}','{}','{}');
                """.format(location, 
                happeningOn,topic, tags)

        db_cursor.execute(query)
        db_conn.commit()
        payload = {
           
            "location" : location,
            "topics" : topic,
            "happeningOn" :happeningOn,
            "tags" : tags
        }
    
        return payload
     

    def get_single_meetup(self, meetup_id):
        """Method to get a specific meetup"""

        meetups = self.all_meetups()
        for meetup in meetups:
            if len(meetups) == 0:
                return False
            if meetup["id"] == meetup_id:
                return meetup

    @staticmethod
    def all_meetups():
        """This method returns a list of all meetups"""

        
        sql = "SELECT * FROM MEETUPSTABLE"

        db_cursor.execute(sql)
        meetups_result = db_cursor.fetchall()
        meetups = []

        for meetup_value in meetups_result:
            meetup_value = {
                
                "id" : meetup_value[0],
                "location" : meetup_value[1],
                "happeningOn" : meetup_value[2],
                "tags" : meetup_value[3],
                "topics" : meetup_value[4],

            }
            meetups.append(meetup_value)

        return meetups


    def get_upcomming_meetups(self):
        """ This methods returns a list of all the upcomming meetups """
        upcomming_meetups = []
        meetups = self.all_meetups()
        if len(meetups) == 0:
            return False
        for meetup in meetups:
            event_date = dt.strptime(meetup["happeningOn"], "%Y-%m-%d")
            if event_date > datetime.datetime.now():
                upcomming_meetups.append(meetup)
        return upcomming_meetups
        
class RSVPModel(object):
    '''models for RSVP class'''

    def __init__(self):
        #self.db2 = RSVP
        """this is the init method """

    def rsvp_meetup(self, meetup_id, topic, status):
        """ This method returns an RSVP for a given meetup """
       
        meetups = MeetupModel.all_meetups()
        for meetup in meetups:
            if meetup["id"] == meetup_id:
                sql = """INSERT INTO RSVPSTABLE(id, topic, status)VALUES('{}',
                '{}', '{}');""".format(meetup_id, topic, status)
                data =  {
                "meetup" : meetup_id,
                "topic" : topic,
                "status" : status
                }
            db_cursor.execute(sql)
            db_conn.commit()
            
                
            return data
            

    