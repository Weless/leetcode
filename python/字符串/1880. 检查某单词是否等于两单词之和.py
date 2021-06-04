class Solution:
    d = {"a":"0","b":"1","c":"2","d":"3","e":"4","f":"5","g":"6",
        "h":"7","i":"8","j":"9","k":"10","l":"11","m":"12","n":"13",
         "o":"14","p":"15","q":"16","r":"17","s":"18","t":"19","u":"20","v":"21",
         "w":"22","x":"23","y":"24","z":"25"}
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return int(self.trans(firstWord)) + int(self.trans(secondWord)) == int(self.trans(targetWord))
    def trans(self,word):
        t = ""
        for i in word:
            t+=self.d[i]
        print(t)
        return t
s = Solution()
firstWord = "acb"
secondWord = "cba"
targetWord = "cdb"
print(s.isSumEqual(firstWord,secondWord,targetWord))


class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def decode(word: str) -> int:
            res = 0
            for ch in word:
                res *= 10
                res += ord(ch) - ord('a')
            return res

        return decode(firstWord) + decode(secondWord) == decode(targetWord)

