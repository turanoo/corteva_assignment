import logging
import sys

from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


from flask import Flask
from flask_restful import Api

from corteva_api.constants import ROOT, CORTEVA_DB
from corteva_api.database import db
from corteva_api.resources.weather_api import WeatherResource, WEATHER_ENDPOINT
from corteva_api.resources.yield_api import YieldResource, YIELD_ENDPOINT

from corteva_api.models import weather, yields




def create_app(db_location):
    """
    Function that creates our Flask application.
    This function creates the Flask app, Flask-RESTful API,
    and Flask-SQLAlchemy connection

    :param db_location: Connection string to the database
    :return: Initialized Flask app
    """

    # This configures our logging, writing all logs to the file "football_api.log"
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
        datefmt="%m-%d %H:%M",
        handlers=[logging.FileHandler("corteva_api.log"), logging.StreamHandler()],
    )    

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = db_location
    db.init_app(app)

    if not path.exists(db_location):
        with app.app_context():    
            # add log
            db.create_all()

    api = Api(app)
    api.add_resource(WeatherResource, WEATHER_ENDPOINT)
    api.add_resource(YieldResource, YIELD_ENDPOINT)
    
    return app





if __name__ == "__main__":
    app = create_app(f"sqlite:////{ROOT}/{CORTEVA_DB}")
    app.run(debug=True)