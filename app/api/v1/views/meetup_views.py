""" meetup views"""
from flask import Blueprint, make_response
from app.api.v1.models.meetups_model import MeetupModel
from app.api.v1 import version1
from app.api.v1.models.meetups_model import Meetups
from flask import Flask, request, jsonify

from app.api.v1.models import meetups_model

db = MeetupModel()



@version1.route("/meetups", methods=["POST"])
def create_meetup():
    try:
        """ Post meetups """
        data = request.get_json()

        if not data:
            return jsonify({
                'message': "Please fill in all fields!",
                'status': 401
                })
        new_meetup = meetups_model.MeetupModel().add_meetup(data['location'], data['tags'], data['topics'], 
                    data['happeningOn'],data['happeningOn'],data['happeningOn'])
        return jsonify({"status": 201, "message": "New meetup created successfully!", "data": new_meetup})
    except Exception as e:

        return jsonify({
                    'message': "Unknown error!",
                    'status': 401
                    })


@version1.route("/meetups", methods=["GET"])
def all_meetups():
    try:
        """ Returns all meetups"""
        meetups = meetups_model.Meetups

        if meetups: 
            return jsonify({"status": 200, "data" : meetups})
        return jsonify({"status" : 404,"message" : "Sorry, we could not find any meetups" })
    except Exception as e:

        return jsonify({
                    'message': "Unknown error!",
                    'status': 404
                    })


@version1.route("/meetups/<int:meetup_id>", methods=["GET"])
def get_single_meetup(meetup_id):
    try:
        """ Gets specific meetup """
        meetup = meetups_model.MeetupModel().get_single_meetup(meetup_id)

        if meetup:
            return jsonify({"status": 200, "data": meetup})
        return jsonify({"status": 404, "message": "No meetup found!"})
    except Exception as e:

        return jsonify({
                    'message': "Unknown error!",
                    'status': 404
                    })

@version1.route("/meetups/upcoming", methods = ["GET"])
def get_upcomming_meetups():
    try:
        """ This returns a list of all the upcomming meetups """

        upcomming_meetups = meetups_model.MeetupModel().get_upcomming_meetups()
        if upcomming_meetups : 
            return jsonify({"status": 200, "data": upcomming_meetups})
        return jsonify({"status": 404, "message": "No upcomming found!"})
    except Exception as e:

        return jsonify({
                    'message': "Unknown error!",
                    'status': 404
                    })


@version1.route("/meetups/<int:meetup_id>/rsvps", methods = ["POST"])
def post_rsvp(meetup_id):
    """This method creates rsvp for a meetup"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({
                'message': "Please fill in all fields!",
                'status': 404
                })
        
        try:


            rsvp = meetups_model.MeetupModel().rsvp_meetup(data["meetup_id"], data["topic"], data["status"])
            return jsonify({"status":201, "message":"RSVP created successfuly!", "data" : rsvp })

        except :
            return jsonify({'message': "Please fill in all fields!",'status': 404})
    except Exception as e:

        return jsonify({
                    'message': "Unknown error!",
                    'status': 404
                    })
        
    
    



