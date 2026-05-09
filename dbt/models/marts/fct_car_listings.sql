WITH manufacturers AS (

    SELECT *
    FROM {{ ref('dim_manufacturers') }}

),

car_listings AS (

    SELECT *
    FROM {{ ref('stg_car_listings') }}

)

SELECT
    cl.id AS listing_id,

    m.manufacturer_id,

    cl.model,
    cl.year,

    cl.price,
    cl.odometer,

    cl.condition,
    cl.fuel,
    cl.transmission,
    cl.state,

    cl.ingested_at

FROM car_listings cl

LEFT JOIN manufacturers m
    ON cl.manufacturer = m.manufacturer_name