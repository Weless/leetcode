from typing import List

# 回朔法
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(path,nums,length):
            if len(path) == length:
                res.append(path[:])
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:continue
                path.append(nums[i])
                dfs(path,nums[:i]+nums[i+1:],length)
                path.pop()
        res = []
        length = len(nums)
        nums.sort()
        dfs([],nums,length)
        return res

# 不断获取下一个全排列

class Solution2:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def nextPermutation(nums: List[int]) -> bool:
            i = len(nums) - 1
            while i > 0 and nums[i - 1] >= nums[i]:
                i -= 1
            if i <= 0:
                nums.sort()
                res.append(nums[:])
                return False

            j = len(nums) - 1
            while nums[i - 1] >= nums[j]:
                j -= 1
            nums[i - 1], nums[j] = nums[j], nums[i - 1]

            nums[i:] = nums[len(nums) - 1:i - 1:-1]

            res.append(nums[:])
            return True
        res = []
        nums.sort()
        while True:
            isTerminate = nextPermutation(nums)
            if not isTerminate:
                return res


s = Solution()
nums = [1,1,2]
print(s.permuteUnique(nums))


