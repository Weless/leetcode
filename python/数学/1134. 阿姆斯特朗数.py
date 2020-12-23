class Solution:
    def isArmstrong(self, N: int) -> bool:
        str_N = str(N)
        res = 0
        for i in str_N:
            res += int(i)**len(str_N)
        return res == N