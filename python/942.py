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


# simple answer
class Solution(object):
    def diStringMatch(self, S):
        lo, hi = 0, len(S)
        ans = []
        for x in S:
            if x == 'I':
                ans.append(lo)
                lo += 1
            else:
                ans.append(hi)
                hi -= 1

        return ans + [lo]
