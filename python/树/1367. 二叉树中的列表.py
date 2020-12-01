class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def dfs(head,node):
            if not head: return True
            if not node: return False
            if head.val != node.val: return False
            return dfs(head.next,node.left) or dfs(head.next,node.right)
        if not head: return True
        if not root: return False
        return dfs(head,root) or self.isSubPath(head,root.left) or self.isSubPath(head,root.right)


