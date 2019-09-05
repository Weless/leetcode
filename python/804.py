import string
class Solution:
    Morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
             ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    alpha = string.ascii_lowercase
    mapTable = dict(zip(alpha, Morse))
    def uniqueMorseRepresentations(self, words):

        tmp = []
        for word in words:
            tmp.append(self.translate(word))
        return len(set(tmp))

    def translate(self,word):
        result = ''
        for i in word:
            result += self.mapTable[i]
        return result


s = Solution()
print(s.uniqueMorseRepresentations(words = ["gin", "zen", "gig", "msg"]));