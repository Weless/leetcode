from typing import List
class Solution:
    def permutation(self, s: str) -> List[str]:
        from itertools import permutations
        temp = ["".join(i) for i in permutations(s)]
        return list(set(temp))

s = Solution()
test = "aab"
print(s.permutation(test))