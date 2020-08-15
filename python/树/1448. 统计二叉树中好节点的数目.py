class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        from collections import deque
        queue = deque()
        queue.appendleft((root.val,root))
        count = 1
        while queue:
            nodeVal,node = queue.pop()
            if node.left:
                if node.left.val >= nodeVal:
                    queue.appendleft((node.left.val,node.left))
                    count+=1
                else:
                    queue.appendleft((nodeVal,node.left))
            if node.right:
                if node.right.val >= nodeVal:
                    queue.appendleft((node.right.val,node.right))
                    count+=1
                else:
                    queue.appendleft((nodeVal,node.right))
        return count


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0
        def dfs(root,val):
            if not root:
                return
            if root.left:
                if root.left.val >= val:
                    self.res +=1
                    dfs(root.left,root.left.val)
                else:
                    dfs(root.left,val)
            if root.right:
                if root.right.val >= val:
                    self.res +=1
                    dfs(root.right,root.right.val)
                else:
                    dfs(root.right,val)
        dfs(root,root.val)
        return self.res