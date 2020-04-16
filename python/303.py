from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
    def sumRange(self, i: int, j: int) -> int:

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
        return sum(self.nums[i:j+1])
nums = [-2, 0, 3, -5, 2, -1]
s = NumArray(nums)
print(s.sumRange(0,5))


# 动态规划求解

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        # 先创建列表空间
        self.sums = [0]
        # 利用append实现动态计算累加值，动态添加至列表
        for i in range(len(nums)):
            self.sums.append(nums[i]+self.sums[i])

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j+1]-self.sums[i]