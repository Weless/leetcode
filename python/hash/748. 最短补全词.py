from typing import List
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        from collections import defaultdict
        d = defaultdict(int)
        for i in licensePlate:
            if i.isalpha():
                d[i.upper()]+=1
    def helper(self,t,word):
        from collections import defaultdict
        d = defaultdict(int)
        for i in word:
            if i.isalpha():
                d[i.upper()]+=1
        for k,v in t:
            if d[k] == 0:
                continue
            if d[k] != v:
                return False,-1