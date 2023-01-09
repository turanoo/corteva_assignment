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

    # override the built-in __repr__ function to define how the object looks like when logged
    def __repr__(self):
        return (
            f"**Weather Data** "
            f"id: {self.id}"
            f"station_id: {self.station_id}"
            f"date: {self.date}"
            f"max_temp: {self.max_temp}"
            f"min_temp: {self.min_temp}"
            f"precipitation: {self.precipitation}"
            f"**Weather Data** "
        )   