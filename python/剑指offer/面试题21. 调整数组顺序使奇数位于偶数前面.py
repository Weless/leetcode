from typing import List
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        from collections import deque

        d = deque()

        for i in nums:
            if i % 2 != 0:
                d.appendleft(i)
            else:
                d.append(i)
        return list(d)

s = Solution()
nums = [1,2,3,4]
print(s.exchange(nums))


# 首尾双指针
# 定义头指针 left ，尾指针 right.
# left 一直往右移，直到它指向的值为偶数
# right一直往左移， 直到它指向的值为奇数
# 交换 nums[left] 和 nums[right].
# 重复上述操作，直到 left == right.

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            while i < j and nums[i] & 1 == 1: i += 1
            while i < j and nums[j] & 1 == 0: j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return nums

