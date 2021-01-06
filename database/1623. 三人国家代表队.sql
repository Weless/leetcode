# 方法一
select
    A.student_name as member_A,
    B.student_name as member_B,
    C.student_name as member_C
from
    SchoolA as A,
    SchoolB as B,
    SchoolC as C
where
    A.student_name != B.student_name
    and A.student_name != C.student_name
    and B.student_name != C.student_name
    and A.student_id != B.student_id
    and A.student_id != C.student_id
    and B.student_id != C.student_id

# 方法二：cross join
SELECT
    A.student_name member_A,
    B.student_name member_B,
    C.student_name member_C
FROM
    SchoolA A
CROSS JOIN
    SchoolB B
CROSS JOIN
    SchoolC C
WHERE
    A.student_name != B.student_name
    AND B.student_name != C.student_name
    AND A.student_name != C.student_name
    AND A.student_id != B.student_id
    AND B.student_id != C.student_id
    AND A.student_id != C.student_id
