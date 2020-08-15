# 超时
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def dfs(path,choice):
            if len(path) == n:
                res.append(path[:])
                return
            for i in choice:
                if i in path:continue
                path.append(i)
                dfs(path,choice)
                path.pop()
        res = []

        nums = list(range(1,n+1))
        dfs([], nums)
        # print(res)
        return "".join([str(i) for i in res[k-1]])
s = Solution()
n = 3
k = 3
print(s.getPermutation(n,k))