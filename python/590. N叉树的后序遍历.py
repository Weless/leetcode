class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
from typing import List
class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        def helper(node,res=[]):
            if node:
                helper(node.children,res)
                for n in node.children:
                    res.append(n.val)
                res.append(node.val)
        res = []
        helper(root,res)
        return res


from pythonds import s