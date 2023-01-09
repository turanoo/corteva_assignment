import logging


from flask import request
from flask_restful import Resource, abort
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from corteva_api.database import db
from corteva_api.models.yields import Yield
from corteva_api.schemas.yield_schema import YieldSchema


YIELD_ENDPOINT = "/api/yield"

logger = logging.getLogger(__name__)


class YieldResource(Resource):
    def get(self, station_id=None, date=None):
        """
        YieldResource GET method. Retrieves all weather information 
        found in the CORTEVA DB under the Weather table. 
        If the station id parameter is provided all the records for that particular station is returned
        

        :param station_id: Station ID to retrieve all weather records pertaining to that station
        :param date: Date to retrieve all weather records pertaining to that date
        :return: Weather, 200 HTTP status code
        """

        return self._get_all_yield, 200
        

    
    def _get_all_yield(self):
        yields = Yield.query.all()
        yields_json = [YieldSchema().dump(yieldd) for yieldd in yields]

        logger.info("Yield info returned")
        return yields_json
    