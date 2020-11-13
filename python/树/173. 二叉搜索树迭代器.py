class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:
    def dfs(self,root):
        if not root: return
        self.dfs(root.left)
        self.inorder.append(root.val)
        self.dfs(root.right)

    def __init__(self, root: TreeNode):
        self.inorder = []
        self.dfs(root)
        self.i = 0

    def next(self) -> int:
        """
        @return the next smallest number
        """
        r = self.inorder[self.i]
        self.i+=1
        return r

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.i < len(self.inorder):
            return True
        else:
            return False

# 受控递归
class BSTIterator:

    def __init__(self, root: TreeNode):

        # Stack for the recursion simulation
        self.stack = []

        # Remember that the algorithm starts with a call to the helper function
        # with the root node as the input
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, root):

        # For a given node, add all the elements in the leftmost branch of the tree
        # under it to the stack.
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """

        # Node at the top of the stack is the next smallest element
        topmost_node = self.stack.pop()

        # Need to maintain the invariant. If the node has a right child, call the
        # helper function for the right child
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
        return topmost_node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0

