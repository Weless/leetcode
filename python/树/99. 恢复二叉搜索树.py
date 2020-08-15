class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        res = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        x = None
        y = None
        pre = res[0]
        # 找出可能存在错误交换的节点x与y
        for i in range(1,len(res)):
            if pre.val > res[i].val:
                y = res[i]
                if not x:
                    x = pre
            pre = res[i]
        # 如果x和y不为空，则交换这两个节点的值，恢复二叉搜索树
        if x and y:
            x.val,y.val = y.val,x.val

class Solution2:
    def recoverTree(self, root: TreeNode) -> None:
        self.x = None
        self.y = None
        self.pre = None
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            if not self.pre:
                self.pre = root
            else:
                if self.pre.val > root.val:
                    self.y = root
                    if not self.x:
                        self.x = self.pre
                self.pre = root
            inorder(root.right)
        inorder(root)
        if self.x and self.y:
            self.x.val,self.y.val = self.y.val,self.x.val
