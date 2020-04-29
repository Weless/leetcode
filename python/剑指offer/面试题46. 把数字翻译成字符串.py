class Solution:
    def translateNum(self, num: int) -> int:
        s = str(num)
        dp = [0] * (len(s)+1)
        dp[1] = 1
        dp[0] = 1
        for i in range(2,len(s)+1):
            tmp = s[i-2:i]
            dp[i] = dp[i-1] + dp[i-2] if "10" <= tmp <= "25" else dp[i-1]
        return dp[-1]

s = Solution()
num = 12258
print(s.translateNum(num))