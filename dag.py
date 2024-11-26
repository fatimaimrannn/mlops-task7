from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import subprocess

# Function to fetch weather data
def fetch_weather_data():
    subprocess.run(["python", "fetch_weather.py"])

# Function to preprocess the data
def preprocess_data():
    subprocess.run(["python", "preprocess.py"])

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 11, 25),
    'retries': 1,
}

# Define the DAG
dag = DAG(
    'weather_data_pipeline',  # DAG name
    default_args=default_args,
    schedule_interval=None,  # To run manually or set a cron expression
)

# Define the task for fetching weather data
task_fetch_data = PythonOperator(
    task_id='fetch_weather_data',  # Task ID
    python_callable=fetch_weather_data,  # Function to be executed
    dag=dag,
)

# Define the task for preprocessing data
task_preprocess_data = PythonOperator(
    task_id='preprocess_data',  # Task ID
    python_callable=preprocess_data,  # Function to be executed
    dag=dag,
)

# Set task dependencies: task_fetch_data runs before task_preprocess_data
task_fetch_data >> task_preprocess_data
