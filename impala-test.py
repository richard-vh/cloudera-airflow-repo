import logging
from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
import pkg_resources

installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
   for i in installed_packages])
print(installed_packages_list)
 
with DAG(
    dag_id="imp_dag",
    start_date=datetime(2025, 2, 9),
    schedule=timedelta(days=1),
    catchup=False,
) as dag:

execute_query = SQLExecuteQueryOperator(
    task_id="execute_query",
    conn_id="rvh-impala",
    sql=f"SHOW TABLES",
    split_statements=True,
    return_last=False,
)

execute_query
