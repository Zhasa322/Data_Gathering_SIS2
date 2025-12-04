from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import logging

logger = logging.getLogger(__name__)
#DAG
with DAG(
    'imdb_pipeline',
    start_date=datetime(2025, 12, 2),
    schedule='43 3 * * *'
) as dag:

    #Tasks
    scraper = PythonOperator(
        task_id='scraper',
        python_callable=lambda: [exec(open('/home/zhasa/airflow/dags/scraper.py').read()), logger.info("Scraping success")]
    )

    cleaner = PythonOperator(
        task_id='cleaner',
        python_callable=lambda: [exec(open('/home/zhasa/airflow/dags/cleaner.py').read()), logger.info("Cleaning success")]

    )

    loader = PythonOperator(
        task_id='loader',
        python_callable=lambda: [exec(open('/home/zhasa/airflow/dags/loader.py').read()), logger.info("Loading success")]

    )

#Order

scraper >> cleaner >> loader
