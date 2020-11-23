from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        import math
        root = TreeNode(1)
        level = math.ceil(math.sqrt(label))
        res = []
        i = 1
        for i in range(1,level+1):
            if level % 2 == 0:
                res.append(i)
            else:


