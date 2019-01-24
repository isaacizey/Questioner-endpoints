from flask import Flask
from app.api.v1.views.meetup_views import version1 as v1
from app.api.v1.views.questions_view import version1 as v1
from app.api.v1.views.user_views import version1 as v1

from app.api.v2.views.meetup_views import version2 as v2
from app.api.v2.views.questions_view import version2 as v2
from app.api.v2.views.user_views import version2 as v2
from flask import jsonify

from . import db_connect 

def create_app():
    app = Flask(__name__)
    app.register_blueprint(v1)
    app.register_blueprint(v2)
    

    return app



