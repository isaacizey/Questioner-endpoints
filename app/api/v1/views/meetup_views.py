""" meetup views"""
from flask import Blueprint, request, jsonify, make_response
from app.api.v1.models.meetups_model import MeetupModel
from app.api.v1.models.meetups_model import Meetups
from flask import Flask, request, jsonify

db = MeetupModel()

MEETUP = Blueprint('MEETUP', __name__)

@MEETUP.route('/meetups', methods=['POST'])
def create_user():
    data = request.get_json()


    print(data) 

    id = data['id']
    location = data['location']
    createdOn = data['createdOn']
    images = data['images']
    topics = data['topics']
    happeningOn = data['happeningOn']
    tags = data['tags']
    data = db.add_meetup(id, location, createdOn, images, topics, happeningOn, tags )
   
    return jsonify({'status' : 200,'message' : 'meetup created'})
