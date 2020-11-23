from typing import List
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        res = 0
        for i,j in zip(startTime,endTime):
            if i<= queryTime <=j :
                res += 1
        return res