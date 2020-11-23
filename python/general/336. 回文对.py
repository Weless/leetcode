from typing import List
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        i = 0
        res = []
        while i < len(words):
            j = i+1
            while j < len(words):
                if words[i][0] == words[j][-1] or words[i][-1] == words[j][0]:
                    tmp = words[i] + words[j]
                    if self.helper(tmp):
                        res.append([i,j])
                    tmp = words[j] + words[i]
                    if self.helper(tmp):
                        res.append([j,i])
                j+=1
            i+=1
        return res
    def helper(self,s):
        return s == s[::-1]
s = Solution()
words = ["bat","tab","cat"]
print(s.palindromePairs(words))