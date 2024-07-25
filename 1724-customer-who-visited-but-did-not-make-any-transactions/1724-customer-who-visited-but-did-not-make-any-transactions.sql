# Write your MySQL query statement below
select customer_id, count(1) as count_no_trans
from Visits as v
left join Transactions as t
on (v.visit_id=t.visit_id)
where transaction_id is NULL
group by customer_id