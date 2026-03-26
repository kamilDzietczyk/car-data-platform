import logging
import uuid
from datetime import datetime

from psycopg2.extras import execute_values

from ingestion.datasets.car_listings_loader import load_car_listings_dataset
from ingestion.db.connection import get_connection


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def run_pipeline():
    logging.info("Car listings pipeline started")

    try:
        conn = get_connection()
        cursor = conn.cursor()

        logging.info("Connected to database")

        df = load_car_listings_dataset("data/vehicles.csv")

        logging.info(f"Loaded {len(df)} rows from CSV dataset")

        df = df.where(df.notna(), None)

        pipeline_run_id = str(uuid.uuid4())
        ingested_at = datetime.utcnow()
        source_system = "craigslist_dataset"

        records = [
            (
                row["price"],
                row["year"],
                row["manufacturer"],
                row["model"],
                row["condition"],
                row["fuel"],
                row["transmission"],
                row["odometer"],
                row["state"],
                source_system,
                ingested_at,
                pipeline_run_id
            )
            for _, row in df.iterrows()
        ]

        query = """
            INSERT INTO raw.car_listings (
                price,
                year,
                manufacturer,
                model,
                condition,
                fuel,
                transmission,
                odometer,
                state,
                source_system,
                ingested_at,
                pipeline_run_id
            )
            VALUES %s
        """

        execute_values(cursor, query, records)

        conn.commit()

        logging.info(f"Inserted {len(records)} records into raw.car_listings")
        logging.info(f"pipeline_run_id={pipeline_run_id}")

        cursor.close()
        conn.close()

        logging.info("Car listings pipeline finished successfully")

    except Exception as e:
        logging.error(f"Car listings pipeline failed: {e}")
        raise


if __name__ == "__main__":
    run_pipeline()