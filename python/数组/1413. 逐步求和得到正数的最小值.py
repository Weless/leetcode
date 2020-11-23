from typing import List
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        startValue = 1
        while True:
            tmp = startValue
            ok = True
            for i in nums:
                tmp+=i
                if tmp <= 0:
                    ok = False
                    break
            if ok:
                break
            startValue += abs(tmp)+1
        return startValue
s = Solution()
nums = [2,3,5,-5,-1]
print(s.minStartValue(nums))