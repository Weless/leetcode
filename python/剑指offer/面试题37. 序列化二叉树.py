class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        import collections
        if not root:
            return []
        queue = collections.deque()
        queue.appendleft(root)
        res = []
        while queue:
            node = queue.popleft()
            res.append(node.val)
            if node.left:
                queue.appendleft(node.left)
            else:
                res.append(None)
            if node.right:
                queue.appendleft(node.right)
            else:
                res.append(None)
        return res


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """