# Car Data Platform

End-to-end Data Engineering project demonstrating a modern data stack using Python, PostgreSQL, dbt, Airflow, Docker and Metabase.

The platform ingests vehicle data from external APIs and CSV datasets, transforms it into analytical models and exposes business insights through dashboards.

---

# Project Overview

This project simulates a real-world data platform architecture used in modern analytics engineering and data warehouse environments.

The platform:

- ingests raw vehicle data
- stores data in PostgreSQL
- transforms datasets using dbt
- orchestrates pipelines with Airflow
- visualizes analytics in Metabase
- runs fully in Docker containers

The goal of the project is to demonstrate practical Data Engineering concepts including:

- ETL / ELT workflows
- layered warehouse architecture
- orchestration
- data modeling
- data quality testing
- analytics engineering
- containerized infrastructure

---

# Architecture

```text
NHTSA API + CSV Dataset
            ↓
     Python Ingestion
            ↓
 PostgreSQL RAW Layer
            ↓
 Airflow Orchestration
            ↓
   dbt Transformations
            ↓
 STAGING + MARTS Layer
            ↓
  Metabase Dashboards
```

---

# Tech Stack

| Layer | Technology |
|---|---|
| Programming Language | Python |
| Database | PostgreSQL |
| Transformations | dbt |
| Orchestration | Apache Airflow |
| Visualization | Metabase |
| Containerization | Docker |
| API Integration | Requests |
| Data Processing | Pandas |
| Database Driver | psycopg2 |
| Deployment Ready | Kubernetes (planned) |

---

# Data Sources

## NHTSA Vehicle API

Public API providing vehicle manufacturer information.

Source:
https://vpic.nhtsa.dot.gov/api/

---

## Craigslist Used Cars Dataset

Used car listings dataset containing vehicle pricing and metadata.

Dataset includes:

- manufacturer
- model
- year
- transmission
- fuel type
- condition
- odometer
- state
- listing price

---

# Warehouse Architecture

The project follows a layered warehouse architecture:

## RAW Layer

Stores unprocessed source data exactly as ingested.

Schemas:
- `raw.api_vehicle_makes`
- `raw.car_listings`

---

## STAGING Layer

dbt models responsible for:

- cleaning
- renaming
- standardization
- filtering invalid data

Models:
- `stg_vehicle_makes`
- `stg_car_listings`

---

## MARTS Layer

Business-oriented analytical models.

Models:
- `dim_manufacturers`
- `fct_car_listings`

---

# Orchestration

Apache Airflow orchestrates:

- API ingestion
- CSV ingestion
- dbt runs
- dbt tests

Example DAG:

```text
load_vehicle_makes
        ↓
load_car_listings
        ↓
dbt_run
        ↓
dbt_test
```

---

# Data Quality

dbt tests validate:

- not null constraints
- uniqueness
- accepted values
- relationships between fact and dimension tables

Example validations:

- unique manufacturer ids
- valid transmission types
- valid vehicle conditions
- foreign key integrity

---

# Dashboards

Metabase dashboards provide analytics such as:

- average vehicle price by manufacturer
- listings by state
- average odometer by production year
- vehicle distribution analysis

---

# Project Structure

```text
car-data-platform/
│
├── airflow/
│   ├── dags/
│   └── Dockerfile
│
├── dbt/
│   ├── models/
│   ├── macros/
│   ├── tests/
│   └── dbt_project.yml
│
├── ingestion/
│   ├── datasets/
│   ├── db/
│   ├── pipelines/
│   └── api/
│
├── data/
│
├── docs/
│   └── screenshots/
│
├── docker/
│
├── docker-compose.yml
│
└── README.md
```

---

# How To Run

## Start all services

```bash
docker compose up -d --build
```

---

## Run ingestion pipelines manually

### Vehicle API ingestion

```bash
docker compose exec airflow python -m ingestion.pipelines.load_vehicle_makes
```

### CSV dataset ingestion

```bash
docker compose exec airflow python -m ingestion.pipelines.load_car_listings
```

---

## Run dbt models

```bash
docker compose exec dbt dbt run --profiles-dir /usr/app
```

---

## Run dbt tests

```bash
docker compose exec dbt dbt test --profiles-dir /usr/app
```

---

# Local Services

| Service | URL |
|---|---|
| Airflow | http://localhost:8082 |
| Metabase | http://localhost:3000 |
| pgAdmin | http://localhost:8080 |

---

# Screenshots

## Airflow DAG

![Airflow](docs/screenshots/airflow.png)

---

## dbt Lineage Graph

![dbt](docs/screenshots/dbt_lineage.png)

---

## Metabase Dashboard

![Metabase](docs/screenshots/metabase.png)

---

# Future Improvements

Planned next steps:

- incremental dbt models
- SCD Type 2 dimensions
- CI/CD pipelines
- Terraform infrastructure
- Kubernetes deployment
- Great Expectations
- Kafka streaming ingestion
- Spark processing
- cloud deployment
- monitoring and alerting

---

# Author

Personal Data Engineering portfolio project focused on modern analytics engineering and warehouse architecture.