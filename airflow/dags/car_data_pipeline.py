from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


DBT_PROJECT_DIR = "/opt/airflow/dbt"
DBT_PROFILES_DIR = "."
DBT_LOG_PATH = "/tmp/dbt_logs"
DBT_TARGET_PATH = "/tmp/dbt_target"

INGESTION_WORKDIR = "/opt/airflow"


default_args = {
    "owner": "data-engineering",
    "retries": 1,
    "retry_delay": timedelta(minutes=2),
    "execution_timeout": timedelta(minutes=10),
}


with DAG(
    dag_id="car_data_pipeline",
    description="End-to-end car data platform pipeline: ingestion, dbt transformations and dbt tests.",
    default_args=default_args,
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    max_active_runs=1,
    tags=["car-data-platform", "ingestion", "dbt"],
) as dag:

    load_vehicle_makes = BashOperator(
        task_id="load_vehicle_makes",
        bash_command=(
            f"cd {INGESTION_WORKDIR} && "
            "python -m ingestion.pipelines.load_vehicle_makes"
        ),
    )

    load_car_listings = BashOperator(
        task_id="load_car_listings",
        bash_command=(
            f"cd {INGESTION_WORKDIR} && "
            "python -m ingestion.pipelines.load_car_listings"
        ),
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=(
            f"cd {DBT_PROJECT_DIR} && "
            f"dbt run --profiles-dir {DBT_PROFILES_DIR} "
            f"--log-path {DBT_LOG_PATH} "
            f"--target-path {DBT_TARGET_PATH}"
        ),
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=(
            f"cd {DBT_PROJECT_DIR} && "
            f"dbt test --profiles-dir {DBT_PROFILES_DIR} "
            f"--log-path {DBT_LOG_PATH} "
            f"--target-path {DBT_TARGET_PATH}"
        ),
    )

    load_vehicle_makes >> load_car_listings >> dbt_run >> dbt_test