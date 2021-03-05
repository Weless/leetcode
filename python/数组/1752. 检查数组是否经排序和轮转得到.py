from typing import List
class Solution:
    def check(self, nums: List[int]) -> bool:
        i = 0
        tag = False
        while i < len(nums)-1:
            if nums[i] > nums[i+1]:
                tag = True
                break
            i+=1
        tmp = nums
        if tag:
            tmp = nums[i+1:] + nums[:i+1]
        else:
            return True
        print(tmp)
        i = 0
        nums.sort()
        while i < len(nums):
            if nums[i] != tmp[i]:
                return False
            i+=1
        return True

s = Solution()
nums = [3,4,5,1,2]
print(s.check(nums))
