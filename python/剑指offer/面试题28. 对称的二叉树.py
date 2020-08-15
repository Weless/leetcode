# 递归
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def recur(L, R):
            if not L and not R: return True
            if not L or not R or L.val != R.val: return False
            return recur(L.left, R.right) and recur(L.right, R.left)

        return recur(root.left, root.right) if root else True


# 层次遍历
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        from collections import deque
        queue = deque()
        queue.append(root)
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node:
                    tmp.append(None)
                else:
                    tmp.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    else:
                        queue.append(None)
                    if node.right:
                        queue.append(node.right)
                    else:
                        queue.append(None)
            if tmp != tmp[::-1]:
                return False
        return True