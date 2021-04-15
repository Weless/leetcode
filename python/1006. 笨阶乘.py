import math
class Solution:
    def clumsy(self, N: int) -> int:
        stack = [N]
        N-=1
        i = 0
        while N > 0:
            if i % 4 == 0:
                stack[-1]*=N
            elif i % 4 == 1:
                stack[-1] //= N
            elif i % 4 == 2:
                stack.append(N)
            else:
                stack.append(-N)
            N-=1
            i+=1
        return sum(stack)
s = Solution()
print(s.clumsy(56))