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
        node = ListNode(tree.val)
        res = [node]
        while queue:
            tmp = []
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                tmp.append(ListNode(node.left.val))
            if node.right:
                queue.append(node.right)
                tmp.append(ListNode(node.right.val))
            if node.left and node.right:
                tmp[0].next = tmp[1]
            res.append(tmp)
        return res



