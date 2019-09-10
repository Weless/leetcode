from collections import deque
class Solution:
    def diStringMatch(self, S):
        deq = deque(range(len(S)+1))
        result = []
        for i in S:
            if i == "D":
                result.append(deq.pop())
            else:
                result.append(deq.popleft())
        result.append(deq.pop())
        return result
s = Solution()
print(s.diStringMatch("IDID"))