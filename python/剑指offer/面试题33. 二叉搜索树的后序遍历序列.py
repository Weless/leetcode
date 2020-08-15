from typing import List

class Solution:
    def verifyPostorder(self, postorder: [int]) -> bool:
        def recur(i, j):
            if i >= j: return True
            p = i
            while postorder[p] < postorder[j]: p += 1
            m = p
            while postorder[p] > postorder[j]: p += 1
            return p == j and recur(i, m - 1) and recur(m, j - 1)

        return recur(0, len(postorder) - 1)


class Solution(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        if not postorder:
            return True
        def isTree(postorder):
            root = postorder[-1]
            length = len(postorder)
            for i in range(length): # 找到左子树的区间,此时注意下这样的切分不可能出现左子树中的节点比根节点大
                if postorder[i] > root:
                    break
            for j in range(i, length-1):# 如果右子树中存在比根节点的小的值,那么是不符合条件的
                if postorder[j] < root:
                    return False

            left = True
            if i > 0:
                left = isTree(postorder[:i])#判断左子树是否符合条件
            right = True
            if i < length -1 :
                right = isTree(postorder[i:-1])#判断右子树是否符合条件
            return left and right
        return isTree(postorder)