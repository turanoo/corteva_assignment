from marshmallow import Schema, fields, post_load
from corteva_api.models.stats import Stats

class StatSchema(Schema):
    """
    Stat Marshmallow Schema
    Marshmallow schema used for loading/dumping weather stats info
    """

    id = fields.Integer(allow_none=False)
    year = fields.Date(allow_none=False)
    station_id = fields.String(allow_none=False)
    avg_max_temp = fields.Integer()
    avg_min_temp = fields.Integer()
    total_precip = fields.Integer()

    @post_load
    def create_stat(self, data, **kwargs):
        return Stats(**data)