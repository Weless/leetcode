class Solution:
    def sortSentence(self, s: str) -> str:
        tmp = []
        for word in s.split(" "):
            tmp.append((word[-1],word[:-1]))
        tmp.sort(key=lambda x:(x[0]))

        res = []
        for i,word in tmp:
            res.append(word)
        return " ".join(res)
s = Solution()
sentence = "is2 sentence4 This1 a3"
print(s.sortSentence(sentence))