# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        stack = []
        stack.append(root)
        while stack != []:

            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
