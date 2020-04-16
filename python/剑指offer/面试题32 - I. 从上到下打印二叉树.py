from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue,res = [root],[root.val]
        while queue:
            temp = []
            for node in queue:
                if node.left:
                    temp.append(node)
                    res.append(node.left.val)
                if node.right:
                    temp.append(node)
                    res.append(node.right.val)
            queue = temp
        return res