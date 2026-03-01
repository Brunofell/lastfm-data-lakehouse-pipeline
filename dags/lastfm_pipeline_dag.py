from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta


default_args = {
    "owner": "bruno",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


with DAG(
    dag_id="lastfm_data_pipeline",
    default_args=default_args,
    description="Pipeline LastFM to S3",
    schedule_interval="0 2 * * *",  # todo dia às 02:00
    start_date=datetime(2026, 2, 1),
    catchup=False,
    tags=["lastfm", "etl"],
) as dag:

    # 1. Extract → Raw
    extract_raw = BashOperator(
        task_id="extract_raw",
        bash_command="python /opt/airflow/project/main.py"
    )

    # 2. Raw → Parquet local
    json_to_parquet = BashOperator(
        task_id="json_to_parquet",
        bash_command="python /opt/airflow/project/transform/json_to_parquet.py"
    )

    # 3. Upload Bronze
    upload_bronze = BashOperator(
        task_id="upload_bronze",
        bash_command="python /opt/airflow/project/transform/upload_parquet_to_s3.py"
    )

    # 4. Bronze → Silver
    clean_silver = BashOperator(
        task_id="clean_silver",
        bash_command="python /opt/airflow/project/transform/clean_geo_tracks.py"
    )

    # Ordem
    extract_raw >> json_to_parquet >> upload_bronze >> clean_silver