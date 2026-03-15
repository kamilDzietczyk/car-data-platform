# Car Data Platform

End-to-end Data Engineering project demonstrating a modern data stack using Python, Airflow, dbt and PostgreSQL.

---

## Overview

The goal of this project is to build a complete data platform that ingests vehicle data from multiple sources, transforms it into an analytical warehouse and exposes insights via API and dashboards.

---

## Architecture

Data pipeline:

API + Dataset  
↓  
Python ingestion  
↓  
PostgreSQL (RAW layer)  
↓  
Airflow orchestration  
↓  
dbt transformations  
↓  
Data Warehouse  
↓  
FastAPI service  
↓  
Metabase dashboards

---

## Tech Stack

| Layer | Technology |
|------|-------------|
| Language | Python |
| Database | PostgreSQL |
| Orchestration | Airflow |
| Transformations | dbt |
| Containerization | Docker |
| API | FastAPI |
| Analytics | Metabase |
| Deployment | Kubernetes |

---

## Data Sources

- NHTSA Vehicle API
- Craigslist Used Cars Dataset (~426k records)

---

## Repository Structure
