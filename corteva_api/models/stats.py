"""
For every year, for every weather station, calculate:

* Average maximum temperature (in degrees Celsius)
* Average minimum temperature (in degrees Celsius)
* Total accumulated precipitation (in centimeters)
"""


from corteva_api.database import db

class Stats(db.Model):
    """
    Stats Flask-SQLAlchemy Model

    Represent objects contained in the stats table
    """


    __tablename__ = "stats"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    station_id = db.Column(db.String(), nullable=False)
    year = db.Column(db.Date(), nullable=False)
    avg_temp = db.Column(db.Integer, nullable=False)
    avg_temp = db.Column(db.Integer, nullable=False)
    total_precip = db.Column(db.Integer, nullable=False)

