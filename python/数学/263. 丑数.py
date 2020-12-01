class Solution:
    def isUgly(self, num: int) -> bool:
        for i in [2,3,5]:
            while num % i == 0:
                num //= i
        if num == 1: return True
        return False