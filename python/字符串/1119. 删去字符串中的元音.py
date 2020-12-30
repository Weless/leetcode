class Solution:
    def removeVowels(self, s: str) -> str:
        res = ''
        for i in s:
            if i in 'aeiou':
                continue
            res+=i
        return res