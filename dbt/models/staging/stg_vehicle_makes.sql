SELECT
    make_id,

    NULLIF(TRIM(make_name), '') AS make_name,

    country,

    source_system,
    ingested_at,
    pipeline_run_id

FROM {{ source('raw', 'api_vehicle_makes') }}