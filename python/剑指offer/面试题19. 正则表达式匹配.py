class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n,m = len(s),len(p)
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        print(dp)
        for i in range(n+1):
            for j in range(m+1):
                if j == 0:
                    print(i,j)
                    dp[i][j] = (i == 0)
                else:
                    if p[j-1] != '*':
                        if i>0 and (s[i-1] == p[j-1] or b[j-1] == '.'):
                            dp[i][j] = dp[i-1][j-1]
                    else:
                        if j>=2:
                            dp[i][j] = dp[i][j] or dp[i][j-2]
                        if i>=1 and j>=2 and (s[i-1] == p[j-2] or p[j-2] == '.'):
                            dp[i][j] = dp[i][j] or dp[i-1][j]
        return dp[n][m]




s = Solution()
a = "aa"
b = "a"
print(s.isMatch(a,b))