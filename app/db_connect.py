import os 
import psycopg2 as psycopg


def connection():
    """ This method connects to the database """
    conn = psycopg.connect("dbname='moses' host='127.0.0.1' user='moses' password='12345678'")
    return conn

def get_connection():
    db = connection()
    return db 

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
    meetups_table = """CREATE TABLE IF NOT EXISTS MEETUPS (
         
        meetup_topic VARCHAR(50) NOT NULL,
        meetup_happening_on VARCHAR(50) NOT NULL, 
        meetup_location VARCHAR(50) NOT NULL
         ) """

    questions_table = """CREATE TABLE IF NOT EXISTS QUESTIONS (
        question_id INT NOT NULL, 
        meetup_id INT NOT NULL,
        question_body VARCHAR(50) NOT NULL,
        question_title VARCHAR(50) NOT NULL,
        user_id VARCHAR(50) NOT NULL,
        question_votes INT NOT NULL

    )"""

    user_table = """CREATE TABLE IF NOT EXISTS USERS (
        user_id SERIAL PRIMARY KEY, 
        username VARCHAR(50) NOT NULL,
        firstname VARCHAR(50) NOT NULL,
        lastname VARCHAR(50) NOT NULL, 
        email VARCHAR(50) NOT NULL,
        password VARCHAR(50) NOT NULL 
      )"""

    tables = [meetups_table, questions_table, user_table]
    return tables 

def post_data():
    """" Test adding data into the created table """
    sql = """INSERT INTO meetups(meetup_topic,meetup_happening_on,meetup_location)
             VALUES('{}','{}','{}');""".format("Meetup na","25th","Nairobi")
    return sql



    


if __name__ == '__main__':
    create_table()