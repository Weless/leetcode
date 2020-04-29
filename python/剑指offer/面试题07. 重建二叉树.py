from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        start = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        start.left = self.buildTree(preorder[index:index+1],inorder[:index])
        start.right = self.buildTree(preorder[index+1:],inorder[index:])
        return start

