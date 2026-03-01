# Last.fm Data Lakehouse Pipeline

## Overview

This project is a personal study project focused on building a complete
data lakehouse pipeline using AWS, Apache Airflow, and Python.

The main goal is to practice real-world data engineering concepts such
as ingestion, processing, orchestration, and analytics.

## Architecture

-   Data Source: Last.fm API
-   Storage: AWS S3 (Bronze, Silver)
-   Processing: Python + Pandas
-   Orchestration: Apache Airflow (Docker)
-   Query Engine: AWS Athena
-   Database: PostgreSQL (Airflow metadata)

## Project Structure

    lastfm-data-lakehouse-pipeline/
    ├── dags/
    ├── docker-compose.yaml
    ├── scripts/
    ├── notebooks/
    └── README.md

## Data Layers

### Bronze

Raw data ingested from the Last.fm API and stored in S3.

### Silver

Cleaned and processed data in Parquet format.

### Gold

The Gold layer was intentionally skipped because the project scope did
not require additional aggregation or modeling. The Silver layer already
satisfied the analytical needs.

This decision was made consciously for learning purposes.

## AWS Setup

### 1. Create S3 Bucket

Create a bucket to store the data lake:

Example:

    bruno-lastfm-datalake

### 2. Configure AWS Credentials

Install AWS CLI and configure:

    aws configure

Provide: - Access Key - Secret Key - Region - Output format

Credentials are stored locally in:

    ~/.aws/credentials

### 3. Folder Structure in S3

    s3://bruno-lastfm-datalake/
     ├── raw/        (bronze)
     ├── processed/  (silver)

## Athena Setup

1.  Open AWS Athena
2.  Configure query result location (S3 bucket)
3.  Create external tables on Silver layer
4.  Query Parquet files using SQL

Athena was used for data validation and exploration.

## Docker Setup

### 1. Install Dependencies

Install: - Docker - Docker Compose

Verify:

    docker --version
    docker-compose --version

### 2. Docker Compose File

The project uses docker-compose.yaml to run:

-   Airflow Webserver
-   Airflow Scheduler
-   PostgreSQL

### 3. Start Containers

    docker-compose up -d

### 4. Stop Containers

    docker-compose down

### 5. Remove Volumes (Reset Database)

    docker-compose down -v

### 6. Clean Docker System (Optional)

    docker system prune -f

## Airflow Setup

### 1. Initialize Database

Run:

    docker-compose run airflow-webserver airflow db init

Or (new versions):

    docker-compose run airflow-webserver airflow db migrate

### 2. Create Admin User

    docker-compose run airflow-webserver airflow users create   --username admin   --firstname Bruno   --lastname Martins   --role Admin   --email admin@test.com   --password admin

### 3. Start Airflow

    docker-compose up -d

### 4. Access Web UI

Open browser:

    http://localhost:8080

Login with created credentials.

### 5. DAGs Configuration

DAGs are located in:

    dags/

Each DAG orchestrates: - Data extraction - Processing - Upload to S3

Example tasks: - extract_lastfm - transform_silver - load_s3

## Local Development

### Reading Parquet from S3

Example:

``` python
import pandas as pd

PATH = "s3://bruno-lastfm-datalake/processed/silver/geo_top_tracks.parquet"

df = pd.read_parquet(PATH)

print(df.head())
```

## Workflow

1.  Extract data from API
2.  Store in Bronze (S3)
3.  Transform to Silver (Parquet)
4.  Orchestrate with Airflow
5.  Query with Athena

## Purpose of the Project

This project was developed exclusively for learning and portfolio
purposes.

Main goals: - Practice cloud data pipelines - Learn Airflow
orchestration - Understand lakehouse architecture - Improve AWS skills -
Build a professional portfolio project

## Lessons Learned

-   Dockerized Airflow setup
-   AWS integration
-   S3 data lake design
-   Athena querying
-   Pipeline automation
-   Debugging distributed systems

## Future Improvements

-   Add monitoring and alerts
-   Implement Gold layer
-   Add CI/CD
-   Improve data quality checks
-   Add unit tests

## Author

Bruno Feliciano Martins Junior Frontend Developer \| Aspiring Data
Engineer
