import logging


from flask import request
from flask_restful import Resource, abort
from sqlalchemy.orm.exc import NoResultFound

from corteva_api.database import db
from corteva_api.models.stats import Stats
from corteva_api.schemas.stat_schema import StatSchema


STATS_ENDPOINT = "/api/weather/stats"

logger = logging.getLogger(__name__)


class StatsResource(Resource):
    def get(self, station_id=None, date=None):
        """
        StatsResource GET method. Retrieves all stat information 
        found in the CORTEVA DB under the stats table. 
        If the station id parameter is provided all the records for that particular station is returned
        

        :param station_id: Station ID to retrieve all weather records pertaining to that station
        :param date: Date to retrieve all weather records pertaining to that date
        :return: Weather, 200 HTTP status code
        """

        if not station_id:
            return self._get_all_weather(), 200
        

        if station_id:
            try:
                return self._get_all_weather_by_station(station_id)
            except NoResultFound:
                abort(404, message="No weather stat found for this station")


    
    def _get_all_weather(self):
        stats = Stats.query.all()
        stats_json = [StatSchema().dump(stat) for stat in stats]

        logger.info("All weather stat returned")
        return stats_json


    def _get_all_weather_by_station(self, station_id):
        stats = Stats.query.filter_by(station_id=station_id)
        stats_json = [StatSchema().dump(stat) for stat in stats]

        if not stats_json:
            logger.info(f"No records found with this station: {station_id}")
            raise NoResultFound


        logger.info(f"Returning all weather stats filtered by {station_id} station_id")
        return stats_json