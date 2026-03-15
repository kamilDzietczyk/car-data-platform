# System Architecture

The platform ingests vehicle data from multiple sources including APIs and large datasets.

Data flows through the following layers:

1. Data ingestion (Python)
2. Raw storage (PostgreSQL)
3. Orchestration (Airflow)
4. Transformation (dbt)
5. Data warehouse
6. API access (FastAPI)
7. Dashboarding (Metabase)