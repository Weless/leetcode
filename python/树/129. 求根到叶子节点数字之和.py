class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.num = 0
        def dfs(root,path):
            if not root:
                return
            path.append(root.val)
            if not root.left and not root.right:
                self.num += self.getSum(path)
                path.pop()
                return
            dfs(root.left)
            dfs(root.right)
        dfs(root,[])
        return self.num
    def getSum(self,A):
        i = 0
        ret = 0
        while i < len(A):
            ret *= 10
            ret += A[i]
            i+=1
        return ret

# DFS
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, prevTotal: int) -> int:
            if not root:
                return 0
            total = prevTotal * 10 + root.val
            if not root.left and not root.right:
                return total
            else:
                return dfs(root.left, total) + dfs(root.right, total)

        return dfs(root, 0)
