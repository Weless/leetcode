from typing import List
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        i = 0
        ans = []
        while i< len(text):
            for word in words:
                j = i+len(word)
                if j<len(text):
                    tmp = text[i:j]
                    if tmp == word:
                        ans.append([i,j-1])
            i+=1
        ans.sort(key=lambda x:(x[0],x[1]))
        return ans
s = Solution()
text = "thestoryofleetcodeandme"
words = ["story","fleet","leetcode"]
print(s.indexPairs(text,words))
            
