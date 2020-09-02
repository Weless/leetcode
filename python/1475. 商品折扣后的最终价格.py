from typing import List
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = prices[:]
        stack = []
        for i in range(len(prices)):
            while stack and prices[i] <= prices[stack[-1]]:
                res[stack[-1]] = prices[stack[-1]] - prices[i]
                stack.pop()
            stack.append(i)
        return res
s = Solution()
prices = [8,4,6,2,3]
print(s.finalPrices(prices))