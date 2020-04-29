from typing import List

# 回朔法
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def trackBack(nums,track,visited):
            if len(track) == len(nums):
                res.append(track[:])
                return
            for i in range(len(nums)):
                if(visited[i]):
                    continue
                if(i>0 and nums[i] == nums[i-1] and visited[i-1]):
                    continue
                track.append(nums[i])
                visited[i] = True
                trackBack(nums,track,visited)
                track.pop()
                visited[i] = False

        track = []
        res = []
        visited = [False for _ in range(len(nums))]
        nums.sort()
        trackBack(nums,track,visited)
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


