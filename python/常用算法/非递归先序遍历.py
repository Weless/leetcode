# 1. 使用列表保存结果；
# 2. 使用栈（列表实现）存储结点；
# 3. 当根结点存在，保存结果，根结点入栈；
# 4. 将根结点指向左子树；
# 5. 根结点不存在，栈顶元素出栈，并将根结点指向栈顶元素的右子树；
# 6. 重复步骤3-6，直到栈空。

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        stack = []
        while root or stack:
            while root:
                ret.append(root.val)
                stack.append(root)
                root = root.left
            if stack:
                t = stack.pop()
                root = t.right
        return ret

