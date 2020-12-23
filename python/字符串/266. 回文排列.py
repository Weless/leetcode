class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
         l = len(s)
         from collections import defaultdict
         d = defaultdict(int)
         for i in s:
             d[i]+=1
         if l % 2 == 0:
             for k,v in d.items():
                 if v % 2 != 0:
                     return False
             return True
         else:
             count = 0
             for k,v in d.items():
                 if v % 2 != 0:
                     count+=1
                 if count > 1:
                     return False
             return True