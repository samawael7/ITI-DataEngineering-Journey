from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime, timedelta

def hello_func():
    print("hello all")

with DAG(
    dag_id = "iti_hello_DE",
    description = "say hello using pythonOperator",
    start_date = datetime(2024, 1, 1),
    schedule = "@daily",
    catchup = False,
    dagrun_timeout = timedelta(minutes=30),
    tags = ["greeting", "iti"]
    
    )as dag:
        begin = EmptyOperator(task_id="start")
        
        hello = PythonOperator(
            task_id="say_hello",
            python_callable=hello_func
            )
            
        finish = EmptyOperator(task_id="end")
        
        begin >> hello >> finish
