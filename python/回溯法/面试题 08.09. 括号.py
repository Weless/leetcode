class Solution:
    def generateParenthesis(self, n):
        def dfs(path,left,right):
            if left == 0 and right == 0:
                res.append(path)
                return
            if left > right: # 如果左括号剩余数量比右括号剩余数量多则减枝
                return
            if left>0:
                dfs(path+"(",left-1,right)
            if right>0:
                dfs(path+")",left,right-1)
        res = []
        dfs('',n,n)
        return res