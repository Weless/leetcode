class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def path(root: TreeNode, sum: int,  mp):
            if not root:
                return
            tmp.append(root.val)
            #如果只有根节点或只有叶子结点，则直接放入ans中
            if not root.left and not root.right and root.val == sum:
                ans.append(tmp[:])
            path(root.left,sum-root.val,tmp)
            path(root.right,sum-root.val,tmp)
            # 这里利用了回溯的思想: 每次回退上一个节点再寻找另一条边的节点作为新路径
            tmp.pop()

        ans = []
        tmp = []
        path(root,sum,tmp)
        return ans

