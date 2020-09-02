class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        while numBottles >= numExchange:
            m,n = divmod(numBottles,numExchange)
            res += m
            numBottles = m + n
        return res
s = Solution()
numBottles = 9
numExchange = 3
print(s.numWaterBottles(numBottles,numExchange))