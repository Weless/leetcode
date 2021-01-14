from typing import List
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        from collections import deque
        sandwiches = deque(sandwiches)
        students = deque(students)

        while True:
            ok = False
            for _ in range(len(students)):
                if students[0] == sandwiches[0]:
                    students.popleft()
                    sandwiches.popleft()
                    ok = True
                else:
                    students.append(students.popleft())
            if not ok:
                break
        return len(students)