class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from typing import List
class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        if not tree:
            return []
        from collections import deque
        queue = deque()
        queue.append(tree)
        res = []
        while queue:
            head = TreeNode(-1)
            start = head
            for _ in range(len(queue)):
                node = queue.popleft()
                head.next = ListNode(node.val)
                head = head.next
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(start.next)
        return res


