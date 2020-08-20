# 1. 使用一个栈保存结点（列表实现）；
# 2. 如果结点存在，入栈，然后将当前指针指向左子树，直到为空；
# 3. 当前结点不存在，则出栈栈顶元素，并把当前指针指向栈顶元素的右子树；
# 4. 栈不为空，循环2、3步。

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                t = stack.pop()
                ret.append(t.val)
                root = t.right
        return ret