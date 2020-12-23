from typing import List
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        i = 0
        while i< len(words):
            word = words[i]
            index = text.find(word)
            
