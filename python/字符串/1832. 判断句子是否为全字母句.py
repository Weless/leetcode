class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = set()
        for i in sentence:
            if not i.isalpha():
                return False
            s.add(i)
            if len(s) == 26:
                return True
        return False

s = Solution()
sentence = "thequickbrownfoxjumpsoverthelazydog"
print(s.checkIfPangram(sentence))