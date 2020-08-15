from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None

        # 前序遍历的特征：根-左-右
        # 因此前序列表的第一个元素一定是根节点
        root_value = preorder[0]
        root = TreeNode(root_value)

        # 中序遍历的特征：左-根-右
        # 结合前序遍历的特征，我们知道，中序列表和前序列表的最后一部分一定是右子树
        # 分割的点一定是中序遍历的根节点

        # 根节点值在中序列表中的索引
        root_in_index = inorder.index(root_value)
        print(root_in_index)
        # 左子树在前序列表中的子列表
        left_pre = preorder[1:root_in_index + 1]
        # 左子树在中序列表中的子列表
        left_in = inorder[:root_in_index]
        # 右子树在前序列表中的子列表
        right_pre = preorder[root_in_index + 1:]
        # 右子树在中序列表中的子列表
        right_in = inorder[root_in_index + 1:]

        # 遍历创建子树
        root.left = self.buildTree(left_pre, left_in)
        root.right = self.buildTree(right_pre, right_in)

        return root

