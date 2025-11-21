import logging
from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator

with DAG(
    dag_id="imp_dag",
    start_date=datetime(2025, 2, 9),
    schedule="*/5 * * * *",
    catchup=False,
) as dag:
    # 🚨 This task definition was missing indentation.
    execute_query = SQLExecuteQueryOperator(
        task_id="execute_query",
        conn_id="rvh-impala",
        sql=f"SHOW TABLES",
        split_statements=True,
        return_last=False,
        show_return_value_in_logs=True,
    )


    # 🚨 This task dependency definition was also missing indentation.
    execute_query