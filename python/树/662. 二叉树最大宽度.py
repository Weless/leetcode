class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 宽度：R - L + 1
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        from collections import deque
        queue = deque()
        queue.appendleft((root,0))
        res = 0
        while queue:
            arr = []
            for _ in range(len(queue)):
                node, pos = queue.pop()
                arr.append(pos)
                if node.left:
                    queue.appendleft((node.left, pos * 2))
                if node.right:
                    queue.appendleft((node.right, pos * 2 + 1))
            res = max(res, 1 + arr[-1] - arr[0])
        return res
