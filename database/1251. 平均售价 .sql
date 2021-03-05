SELECT
    product_id,
    ROUND(SUM(total_prices)/SUM(units),2) AS average_price
FROM
    (SELECT
        p.product_id AS product_id,
        p.price*u.units AS total_prices,
        u.units
    FROM
        Prices AS p
    JOIN
        UnitsSold AS u
    ON
        p.product_id = u.product_id
    WHERE
        u.purchase_date BETWEEN p.start_date AND p.end_date
    ) as T
GROUP BY
    product_id