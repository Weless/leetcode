from typing import List
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        sign = 0
        for i in range(1,len(A)):
            if A[i] >= A[i-1]:
                if sign == 0:
                    sign = 1
                elif sign == 2:
                    return False
            else:
                if sign == 0:
                    sign = 2
                elif sign == 1:
                    return False
        return True