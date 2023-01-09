from corteva_api.database import db

class Weather(db.Model):
    """
    Weather Flask-SQLAlchemy Model

    Represent objects contained in the weather table
    """


    __tablename__ = "weathers"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    station_id = db.Column(db.String(), nullable=False)
    date = db.Column(db.Date(), nullable=False)
    max_temp = db.Column(db.Integer, nullable=False)
    min_temp = db.Column(db.Integer, nullable=False)
    precipitation = db.Column(db.Integer, nullable=False)

