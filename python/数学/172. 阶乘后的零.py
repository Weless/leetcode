class Solution:
    def trailingZeroes(self, n: int) -> int:
        c_2 = 0
        c_5 = 0
        for i in range(1,n+1):
            if i%2 == 0:
                c_2 += i//2
            if i%5 == 0:
                c_5 += i//5
        return min(c_2,c_5)
