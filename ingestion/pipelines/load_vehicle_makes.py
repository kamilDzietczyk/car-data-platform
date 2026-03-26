import logging
import uuid
from datetime import datetime

from psycopg2.extras import execute_values

from ingestion.api.vehicle_api import fetch_vehicle_makes
from ingestion.db.connection import get_connection


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def run_pipeline():
    logging.info("Vehicle makes pipeline started")

    try:
        conn = get_connection()
        cursor = conn.cursor()

        logging.info("Connected to database")

        makes = fetch_vehicle_makes()

        logging.info(f"Fetched {len(makes)} records from API")

        pipeline_run_id = str(uuid.uuid4())
        ingested_at = datetime.utcnow()
        source_system = "nhtsa_api"

        records = [
            (
                make["Make_ID"],
                make["Make_Name"],
                None,
                source_system,
                ingested_at,
                pipeline_run_id
            )
            for make in makes
        ]

        query = """
            INSERT INTO raw.api_vehicle_makes (
                make_id,
                make_name,
                country,
                source_system,
                ingested_at,
                pipeline_run_id
            )
            VALUES %s
            ON CONFLICT (make_id)
            DO UPDATE SET
                make_name = EXCLUDED.make_name,
                country = EXCLUDED.country,
                source_system = EXCLUDED.source_system,
                ingested_at = EXCLUDED.ingested_at,
                pipeline_run_id = EXCLUDED.pipeline_run_id
        """

        execute_values(cursor, query, records)

        conn.commit()

        logging.info(f"Upserted {len(records)} records into raw.api_vehicle_makes")
        logging.info(f"pipeline_run_id={pipeline_run_id}")

        cursor.close()
        conn.close()

        logging.info("Vehicle makes pipeline finished successfully")

    except Exception as e:
        logging.error(f"Vehicle makes pipeline failed: {e}")
        raise


if __name__ == "__main__":
    run_pipeline()