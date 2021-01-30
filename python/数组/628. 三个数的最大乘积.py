from typing import List
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) == 3 :
            return nums[0]*nums[1]*nums[2]
        nums.sort(reverse=True,key=lambda x:abs(x))
        t1,t2 = [],[]
        for i in nums:
            if i < 0: t1.append(i)
            else: t2.append(i)

        if len(t2)==0:
            return t1[-1]*t1[-2]*t1[-3]
        if len(t1)<=1:
            return t2[0]*t2[1]*t2[2]

        res = 0
        if len(t1)>=2:
            res = t1[0]*t1[1]*t2[0]
        if len(t2)>=3:
            res = max(res,t2[0]*t2[1]*t2[2])
        return res