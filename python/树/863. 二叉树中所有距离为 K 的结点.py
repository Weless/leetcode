from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        ans = []

        def dfs(root):
            if not root: return -1
            if root is target:
                subtree_add(root,0)
                return 1
            else:
                left,right = dfs(root.left),dfs(root.right)
                if left != -1:
                    if left == K: ans.append(root.val)
                    subtree_add(root.right,left+1)
                    return left+1
                elif right != -1:
                    if right == K: ans.append(root.val)
                    subtree_add(root.left,right+1)
                    return right+1
                else:
                    return -1

        def subtree_add(root,dist):
            if not root: return
            if dist == K:
                ans.append(root.val)
            else:
                subtree_add(root.left,dist+1)
                subtree_add(root.right,dist+1)
        dfs(root)
        return ans


