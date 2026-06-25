-- Write your PostgreSQL query statement below
SELECT
    v.customer_id,
    COUNT(v.visit_id) AS count_no_trans
from visits v
LEFT JOIN Transactions t
ON v.visit_id = t.visit_id
where t.transaction_id is null
group by v.customer_id 
