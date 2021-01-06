

select unique_id,name
From Employees
left join EmployeeUNI
using(id)