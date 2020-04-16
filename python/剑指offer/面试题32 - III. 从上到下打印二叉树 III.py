from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue, res= [root],[root.val]
        i = 1
        while queue:
            temp = []
            for node in queue:
                if node.left: temp.append(node.left)
                if node.right: temp.append(node.right)
            queue = temp
            if temp:
                if i % 2 == 0:
                    res.append(temp[::-1])
                else:
                    res.append(temp)
            i+=1
        return res