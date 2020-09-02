

class Solution(object):
    def judgeSquareSum(self, c):
        import math
        j = int(math.sqrt(c))
        i = 0
        while i <= j:
            total = i * i + j * j
            if total > c:
                j = j - 1
            elif total < c:
                i = i + 1
            else:
                return True
        return False

s = Solution()
c = 5
print(s.judgeSquareSum(c))