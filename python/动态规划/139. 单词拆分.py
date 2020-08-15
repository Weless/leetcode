from typing import List

# dp[i]表示s的前i位是否可以用wordDict中的单词表示
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(n+1):
            for j in range(i+1,n+1):
                if(dp[i] and s[i:j] in wordDict):
                    dp[j] = True
        return dp[-1]
ans = Solution()
s = "applepenapple"
wordDict = ["apple", "pen"]
print(ans.wordBreak(s,wordDict))