
import pandas
import numpy
import logging


from corteva_api.database import db

logger = logging.getLogger(__name__)


def perform_weather_analysis(df, app):
    logger.info("Starting weather data analysis")

    # Format the date to only show year for ease with grouping
    df['date'] = pandas.to_datetime(df['date']).dt.year
    df = df.replace(-9999, numpy.nan)
    avg_max_temp_df = df.groupby(["date","station_id"])['max_temp'].mean().to_frame()
    avg_min_temp_df = df.groupby(["date","station_id"])['min_temp'].mean().to_frame()
    total_precip_df = df.groupby(["date","station_id"])['precipitation'].sum().to_frame()

    results = pandas.concat([avg_max_temp_df, avg_min_temp_df, total_precip_df], axis=1)
    results.rename(columns={'max_temp': 'avg_max_temp', 'min_temp': 'avg_min_temp', 'precipitation': 'total_precip'})

    with app.app_context():
            rows_processed = df.to_sql(con=db.engine, index=False, name="stats", if_exists='replace', method='multi')

    logger.info("Weather data analysis successful")
    logger.info(f"Total rows processed: {rows_processed}")

    return