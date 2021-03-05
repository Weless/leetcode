class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        wordList = sentence.split(" ")
        for i,v in enumerate(wordList):
            if v.startswith(searchWord):
                return i+1
        return -1