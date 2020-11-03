from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return
        i = self.getIndex(nums)
        root = TreeNode(nums[i])
        root.left = self.constructMaximumBinaryTree(nums[:i])
        root.right = self.constructMaximumBinaryTree(nums[i+1:])
        return root
    def getIndex(self,nums):
        index,max_num = 0,float('-inf')
        for i in range(len(nums)):
            if nums[i] > max_num:
                index = i
                max_num = nums[i]
        return index
