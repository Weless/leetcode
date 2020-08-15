class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        res = []
        i,j = 0,len(res)-1
        while i<j:
            if res[i] + res[j] < k:
                i+=1
            elif res[i] + res[j] >k:
                j-=1
            else:
                return True
        return False