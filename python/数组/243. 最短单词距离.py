from typing import List
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
        ans = float('+inf')
        for i,word in enumerate(words):
            if word == word1:
                x,y = i-1,i+1
                while x>=0 or y < len(words):
                    if x>=0 and words[x] == word2:
                        ans = min(ans,i-x)
                    if y<len(words) and words[y] == word2:
                        ans = min(ans,y-i)
                    x-=1
                    y+=1
        return ans