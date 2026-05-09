WITH distinct_manufacturers AS (

    SELECT DISTINCT
        manufacturer

    FROM {{ ref('stg_car_listings') }}

    WHERE manufacturer IS NOT NULL

)

SELECT
    ROW_NUMBER() OVER (ORDER BY manufacturer) AS manufacturer_id,

    manufacturer AS manufacturer_name

FROM distinct_manufacturers