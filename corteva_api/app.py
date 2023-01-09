import logging
import sys

from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


from flask import Flask
from flask_restful import Api

from corteva_api.constants import ROOT, CORTEVA_DB
from corteva_api.database import db

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
            print('creating something')
            db.create_all()

    api = Api(app)
    return app





if __name__ == "__main__":

    # # TODO check if DB exists, if not create a DB
    # if not path.exists(f"{ROOT}/{CORTEVA_DB}"):
    #     import sqlalchemy as Db
    #     engine = Db.create_engine(f"sqlite:////{ROOT}/{CORTEVA_DB}")
    #     connection = engine.connect()
    #     metadata = Db.MetaData()
    #     yields = Db.Table('yields', )
    #     weathers = Db.Table('weathers',)
        




    app = create_app(f"sqlite:////{ROOT}/{CORTEVA_DB}")
    app.run(debug=True)