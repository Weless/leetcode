class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        return set(s1) == set(s2)