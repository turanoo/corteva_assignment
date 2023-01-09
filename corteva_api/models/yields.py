from corteva_api.database import db

class Yield(db.Model):
    """
    Yield Flask-SQLAlchemy Model

    Represent objects contained in the yield table
    """


    __tablename__ = "yields"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    year = db.Column(db.Integer, nullable=False)
    total_harvest = db.Column(db.Integer, nullable=False)
