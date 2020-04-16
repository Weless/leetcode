from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        import sys
        minNum = sys.maxsize
        maxNum = 0
        for i in prices:
            minNum = min(i,minNum)
            maxNum = max(maxNum,i-minNum)
        return maxNum
s = Solution()
prices = [7,1,5,3,6,4]
print(s.maxProfit(prices))