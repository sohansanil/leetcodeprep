# Write your MySQL query statement below
select person_name
from 
    (SELECT
    person_name,turn,
    SUM(weight) OVER (ORDER BY turn) as running_total
    FROM Queue
    ) t
where running_total <=1000
order by turn desc limit 1