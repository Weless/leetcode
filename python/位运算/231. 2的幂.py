class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return bin(n).count('1') == 1 if n > 0 else False

# 位运算
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0
