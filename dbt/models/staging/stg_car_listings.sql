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

FROM {{ source('raw', 'car_listings') }}

WHERE price IS NOT NULL
  AND price > 0
  AND year IS NOT NULL
  AND NULLIF(TRIM(manufacturer), '') IS NOT NULL
  AND NULLIF(TRIM(model), '') IS NOT NULL