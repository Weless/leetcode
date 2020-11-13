class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        res = []
        def dfs(root,path):
            if not root:
                return
            path.append(root.val)
            if not root.left and not root.right:
                res.append(path[:])
            dfs(root.left,path)
            dfs(root.right,path)
            path.pop()
        dfs(root,[])
        # print(res)
        i = 0
        for r in res:
            if self.isFackPalindrome(r):
                i+=1
        return i

    def isFakePalindrome(self,path):
        from collections import defaultdict
        d = defaultdict(int)
        for i in path:
            d[i] +=1
        count = 0
        for v in d.values():
            if v & 1:
                count += 1
            if count == 2:
                return False
        return True

