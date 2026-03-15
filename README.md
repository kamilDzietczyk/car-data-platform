# car-data-platform
# Car Data Platform

End-to-end Data Engineering project demonstrating modern data stack using Python, Airflow, dbt and PostgreSQL.

## Project Goal

Build a data platform analyzing the used car market using multiple data sources including public APIs and large datasets.

## Architecture

API + Dataset
↓
Python ingestion
↓
PostgreSQL (RAW)
↓
Airflow orchestration
↓
dbt transformations
↓
Data Warehouse
↓
FastAPI
↓
Metabase dashboards

## Tech Stack

Python  
PostgreSQL  
Docker  
Airflow  
dbt  
FastAPI  
Metabase  
Kubernetes  

## Data Sources

NHTSA Vehicle API  
Craigslist Used Cars Dataset (~426k records)

## Repository Structure

architecture/ – system architecture diagrams  
docker/ – Docker environment configuration  
ingestion/ – data ingestion scripts  
airflow/ – DAG orchestration  
dbt/ – data warehouse transformations  
api/ – analytics API  
dashboards/ – BI dashboards  
kubernetes/ – deployment manifests  
docs/ – documentation

## Project Status

🚧 In development