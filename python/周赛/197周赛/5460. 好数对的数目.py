from typing import List
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        def multi(x):
            res = 1
            for i in range(x-1,x+1):
                res *= i
            return res

        res = 0
        for value in dic.values():
            if value >= 2:
                res += multi(value)//2
        return res
s = Solution()
nums = [1,1,1,1,1]
print(s.numIdenticalPairs(nums))