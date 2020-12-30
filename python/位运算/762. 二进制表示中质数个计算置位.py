# 因为2的21次幂已经超出L和R的范围（10^6）了，所以在这个范围内的数的二进制表示中最多只可能有19个1
class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        temp = [2, 3, 5, 7, 11, 13, 17, 19]
        return len([i for i in range(L, R + 1) if bin(i).count('1') in temp])

s = Solution()
L,R=244,269
print(s.countPrimeSetBits(L,R))