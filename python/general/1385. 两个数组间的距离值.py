from typing import List
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        for i in arr1:
            ok = True
            for j in arr2:
                if abs(i-j) <= d:
                    ok = False
                    break
            if ok:
                count +=1
        return count

s = Solution()
arr1 = [1,4,2,3]
arr2 = [-4,-3,6,10,20,30]
d = 3
print(s.findTheDistanceValue(arr1,arr2,d))
