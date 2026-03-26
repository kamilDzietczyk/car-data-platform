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
CREATE TABLE IF NOT EXISTS raw.api_vehicle_makes
(
    make_id INTEGER PRIMARY KEY,
    make_name TEXT,
    country TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- Used car listings dataset
CREATE TABLE IF NOT EXISTS raw.car_listings (

    id SERIAL PRIMARY KEY,

    price INTEGER,
    year INTEGER,

    manufacturer TEXT,
    model TEXT,

    condition TEXT,
    fuel TEXT,
    transmission TEXT,

    odometer INTEGER,
    state TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

CREATE TABLE IF NOT EXISTS raw.car_listings (

    id SERIAL PRIMARY KEY,

    price INTEGER,
    year INTEGER,

    manufacturer TEXT,
    model TEXT,

    condition TEXT,
    fuel TEXT,
    transmission TEXT,

    odometer INTEGER,
    state TEXT,

    source_system TEXT DEFAULT 'craigslist_dataset',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ingestion_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);