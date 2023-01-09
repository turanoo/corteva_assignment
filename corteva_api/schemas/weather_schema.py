from marshmallow import Schema, fields, post_load
from corteva_api.models.weather import Weather

class WeatherSchema(Schema):
    """
    Weather Marshmallow Schema
    Marshmallow schema used for loading/dumping weather info
    """

    id = fields.Integer(allow_none=False)
    date = fields.Date(allow_none=False)
    station_id = fields.String(allow_none=False)
    max_temp = fields.Integer()
    min_temp = fields.Integer()
    precipitation = fields.Integer()

    @post_load
    def create_weather(self, data, **kwargs):
        return Weather(**data)