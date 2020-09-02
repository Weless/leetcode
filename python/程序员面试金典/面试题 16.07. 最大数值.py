class Solution:
    def maximum(self, a: int, b: int) -> int:
        return (a + b + abs(a-b)) // 2

s = Solution()
a = 1
b = 2
print(s.maximum(a,b))