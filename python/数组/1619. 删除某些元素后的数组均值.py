from typing import List
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        import math
        l = len(arr)
        c = math.ceil(l * 0.05)
        print(l,c)
        arr.sort()
        print(len(arr[c:-c]))
        return sum(arr[c:-c]) / len(arr[c:-c])
s = Solution()
arr = [4,8,4,10,0,7,1,3,7,8,8,3,4,1,6,2,1,1,8,0,9,8,0,3,9,10,3,10,1,10,7,3,2,1,4,9,10,7,6,4,0,8,5,1,2,1,6,2,5,0,7,10,9,10,3,7,10,5,8,5,7,6,7,6,10,9,5,10,5,5,7,2,10,7,7,8,2,0,1,1]
print(s.trimMean(arr))




