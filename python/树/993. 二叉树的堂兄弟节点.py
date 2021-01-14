class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return False
        from collections import deque
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            temp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                # 如果某个节点的左节点和右节点的值等于x/y，则为兄弟节点
                if (node.left and node.left.val in [x,y]) and (node.right and node.right.val in [x,y]):
                    return False
            res.append(temp)
        for item in res:
            if len(item) > 1:
                if x in item and y in item:
                    return True
        return False




