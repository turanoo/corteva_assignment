import logging
import sys

from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


from flask import Flask
from flask_restful import Api
from sqlalchemy import create_engine

from corteva_api.constants import CORTEVA_DB, WX_DATA_DIR, YLD_DATA
from corteva_api.database import db
from corteva_api.resources.weather_api import WeatherResource, WEATHER_ENDPOINT
from corteva_api.resources.yield_api import YieldResource, YIELD_ENDPOINT

from corteva_api.ingestion import convert_weather_data_to_dataframe, import_weather_data_to_database, import_and_sanitize_yield_data
from corteva_api.analysis import perform_weather_analysis

from corteva_api.models import weather, yields, stats




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
        handlers=[logging.FileHandler("corteva_api.log")]
    )
    logger = logging.getLogger(__name__)   

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = db_location
    db.init_app(app)

    api = Api(app)
    api.add_resource(WeatherResource, WEATHER_ENDPOINT)
    api.add_resource(YieldResource, YIELD_ENDPOINT) 



    # Check if the database exists, if not create the DB and run the imports
    if not path.exists(CORTEVA_DB):
        with app.app_context():    
            logger.info("Database not found. Creating the database and instantiating all tables")
            db.create_all()
            
            logger.info("Importing weather and corn yield data into the database")
            import_weather_data_to_database(app)
            import_and_sanitize_yield_data(app)

    # Initiate data analysis and save the results
    df = convert_weather_data_to_dataframe()
    perform_weather_analysis(df, app)


    return app



if __name__ == "__main__":
    app = create_app(f"sqlite:////{CORTEVA_DB}")
    app.run(debug=True)