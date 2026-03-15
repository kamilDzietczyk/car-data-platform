import requests
import psycopg2
from datetime import datetime

API_URL = "https://vpic.nhtsa.dot.gov/api/vehicles/getallmakes?format=json"

conn = psycopg2.connect(
    host="localhost",
    database="car_data",
    user="postgres",
    password="postgres"
)

cursor = conn.cursor()

response = requests.get(API_URL)
data = response.json()

makes = data["Results"]

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

print(f"Inserted {len(makes)} records.")