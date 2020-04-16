class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        from collections import deque
        deq = deque()
        for i in range(n):
            deq.appendleft(i)
        while len(deq) != 1:
            k = m-1
            while k:
                deq.appendleft(deq.pop())
                k -= 1
            deq.pop()
        return deq.pop()

s = Solution()
n = 70866
m = 116922
print(s.lastRemaining(n,m))