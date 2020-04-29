class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

from typing import List

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employees.sort(key=lambda x:x[0])
        s = set()
        s.add(id)
        count = 0
        for employees in employees:
            if employees.id in s:
                count += employees.importance
                for sub in employees.subordinates:
                    s.add(sub.id)
        return count