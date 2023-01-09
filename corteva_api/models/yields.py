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

    # override the built-in __repr__ function to define how the object looks like when logged
    def __repr__(self):
        return (
            f"**Yield Data** "
            f"id: {self.id}"
            f"year: {self.date}"
            f"total_harvest: {self.max_temp}"
            f"**Yield Data** "
        )   