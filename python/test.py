from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root: return 0
        self.


s = Solution()
nums = [1,1,2]
print(s.sumOfLeftLeaves(nums))