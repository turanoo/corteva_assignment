import pandas
import os
import logging


from corteva_api.constants import WX_DATA_DIR, YLD_DATA
from corteva_api.database import db


logger = logging.getLogger(__name__)


def convert_weather_data_to_dataframe():
    weather_files = os.listdir(WX_DATA_DIR)

    dfs = pandas.DataFrame()

    for weather_file in weather_files:
        df = pandas.read_csv(f"{WX_DATA_DIR}/{weather_file}", header=None, sep='\t', names=["date", "max_temp", "min_temp", "precipitation"])
        df['station_id'] = os.path.splitext(weather_file)[0]
        df['date'] = df['date'].apply(lambda x: pandas.to_datetime(str(x), format='%Y%m%d'))
        dfs = pandas.concat([dfs, df], ignore_index=True)
    
    return dfs

def import_weather_data_to_database(app):
        logger.info("Starting weather data import")
        total_weather_rows_processed = 0
        df = convert_weather_data_to_dataframe()        
            
        with app.app_context():
            rows_processed = df.to_sql(con=db.engine, index=False, name="weathers", if_exists='append', method='multi')
        total_weather_rows_processed = total_weather_rows_processed + rows_processed
        
        logger.info("Weather data successfully imported")
        logger.info(f"Total records processed: {total_weather_rows_processed}")
        return

def import_and_sanitize_yield_data(app):
    logger.info("Starting corn yield data import")
    df = pandas.read_csv(YLD_DATA,
                        sep='\t',
                        names=["year", "total_harvest"])
    df['year'] = df['year'].apply(lambda x: pandas.to_datetime(str(x), format='%Y'))

    with app.app_context():
        rows_processed = df.to_sql(con=db.engine, index=False, name="yields", if_exists='append', method='multi')
    
    logger.info("Yield data successfully imported")
    logger.info(f"Total records processed: {rows_processed}")
    return