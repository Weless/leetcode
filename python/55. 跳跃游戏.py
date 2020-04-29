from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False


s = Solution()
test = [2,3,1,1,4]
test2 = [3,2,1,0,4]
print(s.canJump(test2))