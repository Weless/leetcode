from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(path, n, start):
            if len(path) == n:
                res.append(path[:])
                return
            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(path, n, i + 1)
                path.pop()
        if not nums:
            return []
        res = []
        for i in range(len(nums) + 1):
            dfs([], i, 0)
        return res

s = Solution()
nums = [1,2,3]
print(s.subsets(nums))