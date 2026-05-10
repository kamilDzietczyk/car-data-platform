from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="car_data_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["car-data-platform"],
) as dag:

    load_vehicle_makes = BashOperator(
        task_id="load_vehicle_makes",
        bash_command="cd /opt/airflow && python -m ingestion.pipelines.load_vehicle_makes"
    )

    load_car_listings = BashOperator(
        task_id="load_car_listings",
        bash_command="cd /opt/airflow && python -m ingestion.pipelines.load_car_listings"
    )

    dbt_run = BashOperator(
    task_id="dbt_run",
    bash_command="cd /opt/airflow/dbt && dbt run --profiles-dir . --log-path /tmp/dbt_logs --target-path /tmp/dbt_target"
    )

    dbt_test = BashOperator(
    task_id="dbt_test",
    bash_command="cd /opt/airflow/dbt && dbt test --profiles-dir . --log-path /tmp/dbt_logs --target-path /tmp/dbt_target"
    )

    load_vehicle_makes >> load_car_listings >> dbt_run >> dbt_test