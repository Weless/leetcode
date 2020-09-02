from typing import List
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def dfs(path,choice,start):
            if len(path)>=2 and self.isSorted(path):
                res.add(path[:])
            for i in range(start,len(nums)):
                if i>start and nums[i] == nums[i-1] : continue
                path.append(nums[i])
                dfs(path,choice,i+1)
                path.pop()
        dfs([],nums,0)
        return list(res)
    def isSorted(self,nums):
        # 判断是否为递增子序列
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                return False
        return True

s = Solution()
nums = [4, 7, 6, 7]
print(s.findSubsequences(nums))