# Write your MySQL query statement below
SELECT e.name  AS Employee,e.salary ,d.name AS Department FROM Employee e JOIN Department d
ON e.departmentId = d.id WHERE e.salary = (
    SELECT MAX(e2.salary) FROM Employee e2
    WHERE e2.departmentId = e.departmentId
)