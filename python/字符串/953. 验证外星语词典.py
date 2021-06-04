from typing import List
class Solution:
    order_dict = {}
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1:
            return True
        for index,v in enumerate(order):
            self.order_dict[v] = index
        i = 1
        while i < len(words):
            if not self.compare(words[i-1],words[i]):
                return False
            i+=1
        return True

    def compare(self,word1:str,word2:str):
        if word1 == word2:
            return True
        i = 0
        while i < len(word1) or i < len(word2):
            if i == len(word1) and i < len(word2):
                return True
            if i == len(word2) and i < len(word1):
                return False
            t1,t2 = word1[i],word2[i]
            if self.order_dict[t1] > self.order_dict[t2]:
                return False
            elif self.order_dict[t1] < self.order_dict[t2]:
                return True
            i+=1
        return True
s = Solution()
words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(s.isAlienSorted(words,order))
