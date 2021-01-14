from typing import List
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        from collections import defaultdict
        d = defaultdict(int)
        word = ''
        for i in paragraph:
            if i.isalpha():
                word+=i.lower()
            else:
                if not word:
                    continue
                d[word]+=1
                word = ''
        if word:
            d[word]+=1
        # print(d)
        # print(sorted(d.items(), key = lambda kv:(kv[1], kv[0])))
        for k,v in sorted(d.items(), key = lambda kv:(kv[1], kv[0]),reverse=True):
            # print(k,v)
            if k in banned:
                continue
            return k
s = Solution()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(s.mostCommonWord(paragraph,banned))