\# 🌦️ Weather ETL Data Engineering Pipeline



\## 📘 Overview

This project demonstrates a complete \*\*ETL (Extract, Transform, Load)\*\* data pipeline built using \*\*Apache Airflow\*\*, \*\*PostgreSQL\*\*, and \*\*Docker\*\*.  

The pipeline automatically extracts weather data from an API, transforms it using Python, and loads it into a PostgreSQL database.



\## 🧠 Key Features

\- \*\*Orchestrated with Apache Airflow\*\*

\- \*\*Automated ETL\*\* workflow: Extract → Transform → Load

\- \*\*Data extraction\*\* from public weather API

\- \*\*Data transformation\*\* using Python

\- \*\*Data loading\*\* into PostgreSQL

\- Fully \*\*containerized\*\* using Docker

\- \*\*Scalable \& schedulable\*\* — can run daily, hourly, etc.



\## ⚙️ Tech Stack

\- \*\*Apache Airflow\*\* – Workflow orchestration

\- \*\*PostgreSQL\*\* – Database storage

\- \*\*Python 3.12\*\* – Data transformation

\- \*\*Docker \& Docker Compose\*\* – Containerization

\- \*\*Pandas (optional)\*\* – For data cleaning (if used)



\## 🏗️ Project Structure


├── dags/ # Airflow DAGs (weather\_etl\_dag.py)

├── data/ # Example extracted/processed data

├── plugins/ # Custom Airflow plugins (optional)

├── docker-compose.yaml # Container orchestration file

├── .gitignore

└── README.md




\## 🚀 How to Run

```bash

\# Clone the repository

git clone https://github.com/<your-username>/weather-etl-pipeline.git

cd weather-etl-pipeline



\# Start the containers

docker compose up -d



\# Access Airflow UI

http://localhost:8080

Username: admin

Password: admin



🎯 Skills Demonstrated



-Data Pipeline Development



-Workflow Scheduling (Airflow)



-ETL Automation



-Docker \& Containerization



-PostgreSQL Integration



-Real-world Data Engineering Deployment



📂 Future Enhancements



-Add data quality checks (Great Expectations)



-Integrate with cloud storage (AWS S3 / GCP)



-Add visualization using Power BI / Tableau

