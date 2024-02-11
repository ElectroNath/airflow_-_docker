from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta 

default_args = {
    'owner': 'Nathan',
    'retries': 5,
    'retry_delay': timedelta(minutes=2),
}

with DAG(
    dag_id = 'first_dag_v3',
    default_args = default_args,
    description = 'This is the first dag I am running on Docker',
    start_date =  datetime(2024, 1, 30, 1),
    schedule_interval = '@daily',
    
) as dag:
    task1 = BashOperator(
        task_id =  'first_task',
        bash_command = 'echo Hello world, this is the first taks'
    )
    
    task2 = BashOperator(
        task_id = 'second_task',
        bash_command = 'echo This is the second task'
    )
    
    task3 = BashOperator(
        task_id = 'third_task',
        bash_command = 'echo This is the third taks'
    )
    
    
    task1 >> [task2, task3]