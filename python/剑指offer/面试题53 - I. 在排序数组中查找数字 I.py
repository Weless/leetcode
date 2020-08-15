from typing import List

# 二分查找
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        import bisect
        left,right = bisect.bisect_left(nums,target),bisect.bisect_right(nums,target)
        return right - left


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return nums.count(target)

s = Solution()
nums = [5,7,7,8,8,10]
target = 8
print(s.search(nums,target))