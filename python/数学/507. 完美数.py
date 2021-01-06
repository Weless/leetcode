class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        import math
        if num == 1:
            return False
        res = 0
        for i in range(1,int(math.sqrt(num))+1):
            if num%i == 0:
                res += i
                res += num//i
        return res == num * 2

s = Solution()
num = 28
print(s.checkPerfectNumber(num))