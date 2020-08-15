from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1 for _ in range(amount+1)]
        dp[0] = 0
        for i in range(1,amount+1):
            for coin in coins:
                if (i-coin<0):
                    continue
                dp[i] = min(dp[i],1+dp[i-coin])
        return -1 if dp[amount] == amount+1 else dp[amount]

s = Solution()
coins = [1,2,5]
amount = 11
print(s.coinChange(coins,amount))