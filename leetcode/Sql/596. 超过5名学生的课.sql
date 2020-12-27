--# Write your MySQL query statement below

select c.class
from courses as c
group by c.class
having COUNT(DISTI NCT student) >= 5;