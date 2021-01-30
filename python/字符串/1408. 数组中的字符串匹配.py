from typing import List
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for word1 in words:
            for word2 in words:
                if word1 != word2:
                    if len(word1) <= len(word2):
                        continue
                    if word1.find(word2) != -1:
                        if word2 not in res:
                            res.append(word2)
        return res
s = Solution()
words = ["mass","as","hero","superhero"]
print(s.stringMatching(words))