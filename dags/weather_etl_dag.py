from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests
import psycopg2

# DAG configuration
default_args = {
    'owner': 'vaibhav',
    'retries': 2,
    'retry_delay': timedelta(minutes=2)
}

def extract_data():
    url = "https://api.open-meteo.com/v1/forecast?latitude=19.0760&longitude=72.8777&current_weather=true"
    response = requests.get(url)
    data = response.json()
    return data['current_weather']

def transform_data(ti):
    weather = ti.xcom_pull(task_ids='extract_data')
    transformed = {
        'temperature': weather['temperature'],
        'windspeed': weather['windspeed'],
        'time': weather['time']
    }
    return transformed

def load_data(ti):
    data = ti.xcom_pull(task_ids='transform_data')
    conn = psycopg2.connect(
        host="airflow_postgres",
        database="airflow",
        user="airflow",
        password="airflow"
    )
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS weather_data (
            id SERIAL PRIMARY KEY,
            temperature FLOAT,
            windspeed FLOAT,
            time TIMESTAMP
        )
    """)
    cur.execute(
        "INSERT INTO weather_data (temperature, windspeed, time) VALUES (%s, %s, %s)",
        (data['temperature'], data['windspeed'], data['time'])
    )
    conn.commit()
    cur.close()
    conn.close()

with DAG(
    dag_id='weather_etl_dag',
    default_args=default_args,
    start_date=datetime(2025, 10, 30),
    schedule_interval='@hourly',
    catchup=False
) as dag:

    extract = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data
    )

    transform = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data
    )

    load = PythonOperator(
        task_id='load_data',
        python_callable=load_data
    )

    extract >> transform >> load
