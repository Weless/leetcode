class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        while True:
            tmp =  numBottles // numExchange
            if tmp == 0:
                break
            res += tmp
            numBottles = numBottles % numExchange + tmp
        return res
s = Solution()
numBottles = 2
numExchange = 3
print(s.numWaterBottles(numBottles,numExchange))