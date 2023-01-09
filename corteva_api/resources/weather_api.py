import logging


from flask import request
from flask_restful import Resource, abort
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from corteva_api.database import db
from corteva_api.models.weather import Weather
from corteva_api.schemas.weather_schema import WeatherSchema


WEATHER_ENDPOINT = "/api/weather"

logger = logging.getLogger(__name__)


class WeatherResource(Resource):
    def get(self, station_id=None, date=None):
        """
        WeatherResource GET method. Retrieves all weather information 
        found in the CORTEVA DB under the Weather table. 
        If the station id parameter is provided all the records for that particular station is returned
        

        :param station_id: Station ID to retrieve all weather records pertaining to that station
        :param date: Date to retrieve all weather records pertaining to that date
        :return: Weather, 200 HTTP status code
        """

        if not station_id and not date:
            return self._get_all_weather(), 200
        

    
    def _get_all_weather(self):
        weathers = Weather.query.all()
        weathers_json = [WeatherSchema().dump(weather) for weather in weathers]

        logger.info("Weather info returned")
        return weathers_json
    
        
