class Solution:
    def toGoatLatin(self, S: str) -> str:
        res = S.split(" ")
        for i,word in enumerate(res):
            if word[0].lower() in "aeiou":
                res[i] += "ma"
                res[i] += "a"*(i+1)
            else:
                res[i] = word[1:]+word[0]+"ma"
                res[i] += "a"*(i+1)
        return " ".join(res)
