""" meetup views"""
from flask import Blueprint, request, jsonify, make_response


meetup = Blueprint('MEETUP', __name__)

meetups = {}
Meetup = {}


@meetup.route('/meetups/<meetup-id>', methods = ['GET'])
def specific_meetup():
    '''  '''

    output = []

    for meetup in meetups:
        
        meetup_content = {}
        meetup_content['id'] = meetup.id
        meetup_content['topic'] = meetup.topic
        meetup_content['location'] = meetup.location
        meetup_content['happeningOn'] = meetup.date
        meetup_content['tags'] = meetup.tags
        output.append(meetup_content)
        return jsonify({'status' : 200, 'user' : output})
        

@app.route('/parcels', methods=['POST'])
def create_user():
    data = request.get_json()

    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    user = User(username=data['username'], email=data['email'], password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'status' : 200,'message' : 'order created'})


@meetup.route('/meetups/', methods=['POST'])
def new_meetup():
    ''' this endpoint registers a meetup '''
    data = request.get_json()

    meetup = Meetup (username = data[''])

    output = []

    for meetup in meetups:
        
        meetup_content = {}
        meetup_content['id'] = meetup.id
        meetup_content['topic'] = meetup.topic
        meetup_content['location'] = meetup.location
        meetup_content['happeningOn'] = meetup.date
        meetup_content['tags'] = meetup.tags
        output.append(meetup_content)
        return jsonify({'status' : 200, 'user' : output})