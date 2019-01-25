import os 
import psycopg2 as psycopg


def get_connection():
    conn = psycopg.connect(""" dbname='questionerdb' host='127.0.0.1' 
            user='postgres' password='12345678'""")
    
    return conn 

def create_table():
    conn = get_connection()
    db_cursor = conn.cursor()
    tables = my_tables()
    for table in tables: 
        db_cursor.execute(table)
    conn.commit()

def enter_data():
    conn = get_connection()
    db_cursor = conn.cursor()
    db_cursor.execute(post_data())
    
    conn.commit()





def my_tables ():


    """ Table creation queries are implemented here """

    """ creates meetups table """
    meetups_table = """CREATE TABLE IF NOT EXISTS MEETUPSTABLE (
        meetup_id SERIAL PRIMARY KEY,
        meetup_topic VARCHAR(50) NOT NULL,
        meetup_happening_on VARCHAR(50) NOT NULL, 
        meetup_location VARCHAR(50) NOT NULL,
        meetup_tags VARCHAR(50) NOT NULL
         ) """

    questions_table = """CREATE TABLE IF NOT EXISTS QUESTIONS (
        question_id SERIAL NOT NULL, 
        meetup_id INT NOT NULL,
        question_body VARCHAR(50) NOT NULL,
        question_title VARCHAR(50) NOT NULL,
        user_id VARCHAR(50) NOT NULL,
        question_votes INT NOT NULL

    )"""

    user_table = """CREATE TABLE IF NOT EXISTS USERS (
        user_id SERIAL PRIMARY KEY, 
        username VARCHAR(150) NOT NULL,
        firstname VARCHAR(150) NOT NULL,
        lastname VARCHAR(150) NOT NULL, 
        email VARCHAR(150) NOT NULL,
        password VARCHAR(150) NOT NULL 
      )""" 

    rsvp_table = """ CREATE TABLE IF NOT EXISTS RSVPSTABLE(
        rsvp_id SERIAL PRIMARY KEY, 
        id INTEGER NOT NULL,
        topic VARCHAR(20) NOT NULL,
        status VARCHAR(50) NOT NULL
    ) """

    comment_table = """ CREATE TABLE IF NOT EXISTS COMMENTS(
        comment_id SERIAL PRIMARY KEY,
        question VARCHAR(100) NOT NULL, 
        body VARCHAR(100) NOT NULL,
        title VARCHAR(100) NOT NULL,
        comment VARCHAR(100) NOT NULL

    )
    
    """

    tables = [meetups_table, questions_table, user_table, rsvp_table, comment_table]
    return tables 

def post_data():
    """" Test adding data into the created table """
    sql = """INSERT INTO meetups(meetup_topic,meetup_happening_on,meetup_location)
             VALUES('{}','{}','{}');""".format("Meetup na","25th","Nairobi")
    return sql



    


if __name__ == '__main__':
    create_table()