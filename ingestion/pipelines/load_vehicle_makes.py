from datetime import datetime

from psycopg2.extras import execute_values

from ingestion.api.vehicle_api import fetch_vehicle_makes
from ingestion.db.connection import get_connection


def run_pipeline():

    conn = get_connection()
    cursor = conn.cursor()

    makes = fetch_vehicle_makes()

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

    cursor.close()
    conn.close()

    print(f"Pipeline finished. Upserted {len(records)} records.")
    

if __name__ == "__main__":
    run_pipeline()