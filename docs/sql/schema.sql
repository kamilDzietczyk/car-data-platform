/*
===============================================================================
Car Data Platform - Database Schema
===============================================================================

Purpose:
Defines database schemas and raw layer tables for the data platform.

Architecture Layers:
- raw      : source data ingested from APIs and datasets
- staging  : cleaned and standardized data
- mart     : analytical tables used for reporting and dashboards

Author: Kamil
===============================================================================
*/


-- ============================================================================
-- SCHEMAS
-- ============================================================================

CREATE SCHEMA IF NOT EXISTS raw;
CREATE SCHEMA IF NOT EXISTS staging;
CREATE SCHEMA IF NOT EXISTS mart;


-- ============================================================================
-- RAW TABLES
-- ============================================================================


-- Vehicle manufacturers from NHTSA API
CREATE TABLE IF NOT EXISTS raw.api_vehicle_makes (
    make_id INTEGER PRIMARY KEY,
    make_name TEXT,
    country TEXT,
    source_system TEXT NOT NULL DEFAULT 'nhtsa_api',
    ingested_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    pipeline_run_id TEXT
);


-- Used car listings dataset
CREATE TABLE IF NOT EXISTS raw.car_listings (
    id BIGSERIAL PRIMARY KEY,
    price INTEGER,
    year INTEGER,
    manufacturer TEXT,
    model TEXT,
    condition TEXT,
    fuel TEXT,
    transmission TEXT,
    odometer INTEGER,
    state TEXT,
    source_system TEXT NOT NULL DEFAULT 'craigslist_dataset',
    ingested_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    pipeline_run_id TEXT
);

-- ============================================================================
-- STAGGING VIEW
-- ============================================================================

--Stagging view for raw.api_vehicle_makes
CREATE OR REPLACE VIEW staging.stg_vehicle_makes AS
SELECT
    make_id,
    NULLIF(TRIM(make_name), '') AS make_name,
    country,
    source_system,
    ingested_at,
    pipeline_run_id
FROM raw.api_vehicle_makes;

--Stagging view for raw.stg_car_listings
CREATE OR REPLACE VIEW staging.stg_car_listings AS
SELECT
    id,
    price,
    year,
    NULLIF(TRIM(manufacturer), '') AS manufacturer,
    NULLIF(TRIM(model), '') AS model,
    LOWER(NULLIF(TRIM(condition), '')) AS condition,
    LOWER(NULLIF(TRIM(fuel), '')) AS fuel,
    LOWER(NULLIF(TRIM(transmission), '')) AS transmission,
    odometer,
    UPPER(NULLIF(TRIM(state), '')) AS state,
    source_system,
    ingested_at,
    pipeline_run_id
FROM raw.car_listings
WHERE price IS NOT NULL
  AND price > 0
  AND year IS NOT NULL
  AND NULLIF(TRIM(manufacturer), '') IS NOT NULL
  AND NULLIF(TRIM(model), '') IS NOT NULL;