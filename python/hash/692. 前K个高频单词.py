from typing import List
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import defaultdict
        d = defaultdict(int)
        for word in words:
            d[word]+=1

        res  = []
        for key,value in d.items():
            res.append((key,value))

        res.sort(key=lambda x:(-x[1],x[0]))
        return [i for i,_ in res[:k]]
s = Solution()
words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
print(s.topKFrequent(words,k))