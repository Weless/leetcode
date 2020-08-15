class Solution:
    def arrangeCoins(self, n: int) -> int:
        sum = 0
        i = 1
        while True:
            sum += i
            if sum > n: return i-1
            if sum == n : return i
            i+=1
