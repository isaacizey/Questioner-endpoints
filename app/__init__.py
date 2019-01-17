from flask import Flask
from app.api.v1.views.meetup_views import version1 as v1
from app.api.v1.views.questions_view import version1 as v1
from app.api.v1.views.user_views import version1 as v1 

def create_app():
    app = Flask(__name__)
    app.register_blueprint(v1)

    return app



