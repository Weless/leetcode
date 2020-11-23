from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        maxNum = 0
        prices.append(-1)
        for i in prices:
            while stack and stack[-1]>i:
                maxNum = max(maxNum,stack[-1]-stack[0])
                stack.pop()
            stack.append(i)
        return maxNum
s = Solution()
test = [7,1,5,3,6,4]
print(s.maxProfit(test))