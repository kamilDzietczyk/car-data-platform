from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def hello_world():
    print("Hello from Airflow!")


with DAG(
    dag_id="test_dag",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["test"],
) as dag:

    hello_task = PythonOperator(
        task_id="hello_task",
        python_callable=hello_world,
    )