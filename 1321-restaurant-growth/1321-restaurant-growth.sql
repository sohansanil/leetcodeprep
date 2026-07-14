# Write your MySQL query statement below
SELECT
    visited_on,
    amount,
    ROUND(average_amount, 2) AS average_amount
FROM
(
    SELECT
        visited_on,

        SUM(amount) OVER(
            ORDER BY visited_on
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS amount,

        AVG(amount) OVER(
            ORDER BY visited_on
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS average_amount,

        COUNT(*) OVER(
            ORDER BY visited_on
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS cnt

    FROM
    (
        SELECT
            visited_on,
            SUM(amount) AS amount
        FROM Customer
        GROUP BY visited_on
    ) daily

) t

WHERE cnt = 7;