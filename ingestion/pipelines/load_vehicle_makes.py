import logging
from datetime import datetime

from psycopg2.extras import execute_values

from ingestion.api.vehicle_api import fetch_vehicle_makes
from ingestion.db.connection import get_connection


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def run_pipeline():

    logging.info("Pipeline started")

    try:

        conn = get_connection()
        cursor = conn.cursor()

        logging.info("Connected to database")

        makes = fetch_vehicle_makes()

        logging.info(f"Fetched {len(makes)} records from API")

        records = [
            (
                make["Make_ID"],
                make["Make_Name"],
                None,
                datetime.utcnow()
            )
            for make in makes
        ]

        query = """
            INSERT INTO raw.api_vehicle_makes (make_id, make_name, country, created_at)
            VALUES %s
            ON CONFLICT (make_id)
            DO UPDATE SET
                make_name = EXCLUDED.make_name,
                created_at = EXCLUDED.created_at
        """

        execute_values(cursor, query, records)

        conn.commit()

        logging.info(f"Upserted {len(records)} records into raw.api_vehicle_makes")

        cursor.close()
        conn.close()

        logging.info("Pipeline finished successfully")

    except Exception as e:

        logging.error(f"Pipeline failed: {e}")
        raise


if __name__ == "__main__":
    run_pipeline()