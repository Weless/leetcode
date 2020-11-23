from typing import List
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        tmp = 0
        for i in range(len(arr)-1):
            if tmp == 0:
                tmp = arr[i] - arr[i+1]
            else:
                if tmp != arr[i] - arr[i+1]:
                    return False
        return True

s = Solution()
arr = [3,3,3,3]
print(s.canMakeArithmeticProgression(arr))