from datetime import datetime

from ingestion.api.vehicle_api import fetch_vehicle_makes
from ingestion.db.connection import get_connection


def run_pipeline():

    conn = get_connection()
    cursor = conn.cursor()

    makes = fetch_vehicle_makes()

    for make in makes:

        cursor.execute(
            """
            INSERT INTO raw.api_vehicle_makes (make_id, make_name, created_at)
            VALUES (%s, %s, %s)
            """,
            (
                make["Make_ID"],
                make["Make_Name"],
                datetime.utcnow()
            )
        )

    conn.commit()

    cursor.close()
    conn.close()

    print(f"Inserted {len(makes)} records")


if __name__ == "__main__":
    run_pipeline()