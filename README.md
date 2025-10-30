# 🌦️ Weather ETL Data Engineering Pipeline

## 🧠 Overview
This project demonstrates an **end-to-end ETL (Extract, Transform, Load)** data pipeline built using **Apache Airflow**, **PostgreSQL**, and **Docker**.  
It automates fetching weather data from an API, transforming it using Python, and loading it into a PostgreSQL database.

---

## 🧑‍💻 Project Purpose
The goal of this project is to showcase key **Data Engineering concepts**:
- Workflow orchestration using **Apache Airflow**
- API data ingestion
- Data transformation using Python
- Automated data loading into a relational database
- Running everything inside Docker for easy deployment

---

## ⚙️ Tools & Technologies
| Tool | Purpose |
|------|----------|
| **Apache Airflow** | Workflow orchestration |
| **Docker Compose** | Containerization & local setup |
| **PostgreSQL** | Database for loading data |
| **Python 3.12** | Data extraction and transformation |
| **Requests / Pandas** | API integration & data cleaning |

---

## 📊 ETL Pipeline Flow
```text
Weather API → Airflow DAG (Extract → Transform → Load) → PostgreSQL Database
🚀 How to Run Locally
Clone the repository

bash
Copy code
git clone https://github.com/vaibhavmule-code/weather-etl-pipeline.git
cd weather-etl-pipeline
Start the containers

bash
Copy code
docker compose up -d
Access Airflow UI

URL: http://localhost:8080

Username: admin

Password: admin

Trigger the DAG

In the Airflow UI, enable and trigger weather_etl_dag

It will automatically:

Extract weather data from API

Transform data with Python

Load into PostgreSQL

🗂️ Project Structure
bash
Copy code
├── dags/
│   └── weather_etl_dag.py        # Main Airflow DAG
├── data/                         # Optional data samples
├── plugins/                      # (Optional) custom Airflow plugins
├── docker-compose.yaml           # Docker orchestration file
├── requirements.txt              # Python dependencies
├── .gitignore
└── README.md
🖼️ Screenshots
Airflow DAG

<img width="1867" height="917" alt="Airflow UI Dashboard" src="https://github.com/user-attachments/assets/df4ac21d-02dc-4a32-b926-e883bea89e44" />


📚 Future Improvements
Add automated data quality checks

Connect with cloud storage (AWS S3 / GCS)

Add data visualization dashboard (Tableau / Power BI)

Integrate with CI/CD pipeline

📜 License
This project is licensed under the MIT License.

---

---

## ✨ Author
**Vaibhav Mule**  
📍 Data Engineering Enthusiast  
🔗 [GitHub](https://github.com/vaibhavmule-code)  
💼 [LinkedIn](https://www.linkedin.com/in/vaibhav-d-mule/)  
📧 [Email](mailto:vaibhavmule125@gmail.com)


---
