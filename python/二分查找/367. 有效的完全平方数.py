# 效率低
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        from itertools import count
        for i in count(1,1):
            if i ** 2 == num:
                return True
            elif i ** 2 > num:
                return False

# 二分查找
class Solution2:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2: return True
        i,j = 2,num//2
        while i <= j:
            x = (i+j)//2
            if x**2 == num:
                return True
            elif x**2 < num: i = x+1
            else: j = x-1
        return False


s = Solution()
num = 16
print(s.isPerfectSquare(num))