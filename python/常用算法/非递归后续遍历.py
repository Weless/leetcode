# 使用栈存储结点；
# 当结点存在或者栈不为空，判断结点；
# 当结点存在，结点值保存，结点入栈，并将指针指向结点的右子树；
# 当栈不为空，结点出栈，并将指针指向左子树；
# 重复2-4直到结果产生；
# 逆序输出结果，利用Python列表的-1.

class Solution(object):
    def postorderTraversal(self, root):
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
                root = root.right
            if stack:
                top = stack.pop()
                root = top.left
        return ret[::-1]