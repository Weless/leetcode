class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        import collections
        d = dict(collections.Counter(magazine))
        for i in ransomNote:
            if i not in ransomNote:
                return False
            if d[i]<0:
                return False
            d[i]-=1
        return True
s = Solution()
print(s.canConstruct("aa", "aab"))
