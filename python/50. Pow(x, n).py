class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        if n >0:
            for i in range(n):
                result = result * x
            return result
        elif n == 0:
            return 1
        else:
            for i in range(-n):
                result = result * x
            return 1/result


# 分治法 + 递归
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            if N == 0:
                return 1.0
            y = quickMul(N // 2)
            return y * y if N % 2 == 0 else y * y * x

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)

s = Solution()
x = 0.44528
n = 0
print(s.myPow(x,n))