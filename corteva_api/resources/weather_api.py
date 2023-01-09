import logging


from flask import request
from flask_restful import Resource, abort
from sqlalchemy.orm.exc import NoResultFound

from corteva_api.database import db
from corteva_api.models.weather import Weather
from corteva_api.schemas.weather_schema import WeatherSchema


WEATHER_ENDPOINT = "/api/weather"

logger = logging.getLogger(__name__)


class WeatherResource(Resource):
    def get(self, station_id=None):
        """
        WeatherResource GET method. Retrieves all weather information 
        found in the CORTEVA DB under the Weather table. 
        If the station id parameter is provided all the records for that particular station is returned
        

        :param station_id: Station ID to retrieve all weather records pertaining to that station
        :return: Weather, 200 HTTP status code
        """

        if not station_id:
            return self._get_all_weather(), 200
        

        if station_id:
            try:
                return self._get_all_weather_by_station(station_id)
            except NoResultFound:
                abort(404, message="No weather information found")


    
    def _get_all_weather(self):
        weathers = Weather.query.all()
        weathers_json = [WeatherSchema().dump(weather) for weather in weathers]

        logger.info("All weather data returned")
        return weathers_json


    def _get_all_weather_by_station(self, station_id):
        weathers = Weather.query.filter_by(station_id=station_id)
        weathers_json = [WeatherSchema().dump(weather) for weather in weathers]

        if not weathers_json:
            logger.info(f"No records found with this station: {station_id}")
            raise NoResultFound


        logger.info(f"Returning all weather data filtered by {station_id} station_id")
        return weathers_json



    
        
