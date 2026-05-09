SELECT DISTINCT
    ROW_NUMBER() OVER (ORDER BY manufacturer) AS manufacturer_id,

    manufacturer AS manufacturer_name

FROM {{ ref('stg_car_listings') }}

WHERE manufacturer IS NOT NULL