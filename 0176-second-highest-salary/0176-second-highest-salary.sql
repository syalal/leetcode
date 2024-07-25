# Write your MySQL query statement below

select max(salary) as SecondHighestSalary
from employee e 
-- left join (select id, MAX(salary) m from employee) as d
-- on (e.id = d.id)
where e.salary != (select MAX(salary) from employee)
