class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return False
        from collections import deque
        queue = deque()
        queue.append(root)
        res = [[root.val]]
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    tmp.append(node.left.val)
                else:
                    tmp.append(None)
                if node.right:
                    queue.append(node.right)
                    tmp.append(node.right.val)
                else:
                    tmp.append(None)
            res.append(tmp)
        for items in res:
            if len(items) > 1:
                i,j = 0,len(items)-1
                while i<j:
                    if items[i] != items[j]:
                        return False
                    i+=1
                    j-=1
        return True


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root,root)
    def isMirror(self,t1:TreeNode,t2:TreeNode):
        if not t1 and not t2: return True
        if t1 or t2: return False
        return t1.val == t2.val and self.isMirror(t1.right,t2.left) and self.isMirror(t1.left,t2.right)

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        from collections import deque
        queue = deque()
        queue.append(root)
        queue.append(root)
        while queue:
            t1 = queue.popleft()
            t2 = queue.popleft()
            if not t1 and not t2:
                continue
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)