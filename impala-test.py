import logging
from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
import pkg_resources
import importlib.metadata

with DAG(
    dag_id="imp_dag",
    start_date=datetime(2025, 2, 9),
    schedule=timedelta(days=1),
    catchup=False,
) as dag:
    # 🚨 This task definition was missing indentation.
    execute_query = SQLExecuteQueryOperator(
        task_id="execute_query",
        conn_id="rvh-impala",
        sql=f"SHOW TABLES",
        split_statements=True,
        return_last=False,
    )

    # 🚨 This code was also missing indentation.
    # Note: Airflow will execute this code when parsing the DAG file, not as a task.
    installed_packages_list = sorted(["%s==%s" % (d.metadata['Name'], d.version) 
                                      for d in importlib.metadata.distributions()])

    # The print statement will run during the DAG parsing process.
    print(installed_packages_list)

    # 🚨 This task dependency definition was also missing indentation.
    execute_query