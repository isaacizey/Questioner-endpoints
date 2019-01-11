import os
from app import create_app
from instance.config import Config
from app.api.v1.views.meetup_views import MEETUP

config_name = os.getenv("FLASK_ENV")

app = create_app()

app.register_blueprint(MEETUP)

if __name__ == "__main__":
    app.run(debug=True)
    