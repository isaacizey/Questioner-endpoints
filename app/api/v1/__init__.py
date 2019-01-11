from flask import Flask
from flask import Blueprint
from app.api.v1.views.meetup_views import meetup
app = Flask(__name__)

app.register_blueprint(app)