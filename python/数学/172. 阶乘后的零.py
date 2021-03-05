class Solution:
    def trailingZeroes(self, n: int) -> int:
        c_2 = 0
        c_5 = 0
        for i in range(1,n+1):
            while True:
                ok = False
                if i%2 == 0:
                    c_2 += i//2
                    i //= 2
                    ok = True
                if i%5 == 0:
                    c_5 += i//5
                    i //= 5
                    ok = True
                if not ok:
                    break
        return min(c_2,c_5)
s = Solution()
n = 100
print(s.trailingZeroes(n))
