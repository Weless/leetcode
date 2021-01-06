
# 子查询1
select id,name
from Students
where department_id
not in (select id from Departments)

# 子查询2
SELECT
	id,
	`name`
FROM
	Students AS s
WHERE NOT EXISTS(
	SELECT
		1
	FROM
		Departments
	WHERE
		id = s.department_id
);


# 外连接
select s.id,s.name
from students s
left join Departments d
on s.department_id=d.id
where d.id is null

