from typing import List
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        for i in arr:
            if 2*i > arr[-1]:
                return False
            if i == 0:
                if arr.count(0)>1:
                    return True
            elif 2*i in arr:
                return True
        return False
s = Solution()
arr = [-2,0,10,-19,4,6,-8]
print(s.checkIfExist(arr))