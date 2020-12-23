class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0
        step = 0
        while i < len(abbr):
            if not abbr[i].isdigit() and abbr[i] == word[j]:
                i+=1
                j+=1
            else:
                tmp = ''
                while i < len(abbr) and abbr[i].isdigit():
                    tmp+=abbr[i]
                    i+=1
                if tmp:
                    step = int(tmp)
                    j += step
                if j < len(word):
                    if word[j] != abbr[i]:
                        return False
        return True

S= Solution()
s = "internationalization"
abbr = "i12iz4n"
print(S.validWordAbbreviation(s,abbr))