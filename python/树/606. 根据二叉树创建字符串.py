class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        self.s = ''
        def dfs(root,isLeft):
            if not root and not isLeft:
                return
            self.s+='('
            if root:
                self.s+= str(root.val)
                dfs(root.left,True)
                dfs(root.right,False)
            self.s+=')'
        dfs(t,True)
        return self.s[1:-1]
