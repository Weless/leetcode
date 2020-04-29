from typing import List
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        res = cur = sum(cardPoints[:k])
        for i in range(k):
            cur += cardPoints[-i - 1] - cardPoints[k - 1 - i]
            res = max(cur, res)
        return res

s = Solution()
cardPoints = [1,2,3,4,5,6,1]
k = 3
print(s.maxScore(cardPoints,k))