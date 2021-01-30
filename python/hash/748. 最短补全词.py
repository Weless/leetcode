from typing import List
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        from collections import defaultdict
        d = defaultdict(int)
        for i in licensePlate:
            if i.isalpha():
                d[i.upper()]+=1

        res = float('+inf')
        w = ""
        for word in words:
            ok,t = self.helper(d,word)
            if ok and t < res:
                res = t
                w = word
        return w

    def helper(self,t,word):
        from collections import defaultdict
        d = defaultdict(int)
        for i in word:
            if i.isalpha():
                d[i.upper()]+=1
        for k,v in d.items():
            if v < t[k]:
                return False,-1
        return True,len(word)

s = Solution()
licensePlate = "Ah71752"
words = ["suggest","letter","of","husband","easy","education","drug","prevent","writer","old"]
print(s.shortestCompletingWord(licensePlate,words))