class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder and not inorder:
            return None
        rootVal = postorder[-1]
        root = TreeNode(rootVal)
        i = inorder.index(rootVal)
        root.left = self.buildTree(inorder[:i],postorder[0:i])
        root.right = self.buildTree(inorder[i+1:],postorder[i:-1])
        return root
    
s = Solution()
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
print(s.buildTree(inorder,postorder))