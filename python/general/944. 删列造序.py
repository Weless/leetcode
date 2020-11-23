from typing import List
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        count = 0
        for id,item in enumerate(zip(*A)):
            if sorted(item) != list(item):
                count +=1
        return count
s = Solution()
A = ["cba", "daf", "ghi"]
print(s.minDeletionSize(A))