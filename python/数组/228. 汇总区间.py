from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 0
        res = []
        while i < len(nums):
            start = nums[i]
            while i < len(nums)-1 and nums[i+1] - nums[i] == 1:
                i+=1
            end = nums[i]
            if start == end:
                res.append(str(start))
            else:
                res.append("%d->%d" % (start,end))
            i+=1
        return res
s = Solution()
nums = [0,1,2,4,5,7]
print(s.summaryRanges(nums))

