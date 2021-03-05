from typing import List

# 前缀和
class NumArray:

    def __init__(self, nums: List[int]):
        if not nums:
            return []
        self.res = []
        self.res.extend(nums)
        self.sum = [0] * len(nums)
        self.sum[0] = self.res[0]
        for i in range(1,len(self.res)):
            self.sum[i] = self.res[i] + self.sum[i-1]


    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.sum[j]
        return self.sum[j] - self.sum[i-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
