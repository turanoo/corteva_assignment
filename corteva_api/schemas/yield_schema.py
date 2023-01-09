from marshmallow import Schema, fields, post_load
from corteva_api.models.yields import Yield


class YieldSchema(Schema):
    """
    Yield Marshmallow Schema
    Marshmallow schema used for loading/dumping yield info
    """

    id = fields.Integer(allow_none=False)
    year = fields.Date(allow_none=False)
    total_harvest = fields.Integer()

    @post_load
    def create_yield(self, data, **kwargs):
        return Yield(**data)