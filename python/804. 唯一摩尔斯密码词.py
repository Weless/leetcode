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



#### other answer

'''
def uniqueMorseRepresentations(self, words):
        d = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
             "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        return len({''.join(d[ord(i) - ord('a')] for i in w) for w in words})
        
        
def uniqueMorseRepresentations(self, words):
    
    map_=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
    res=set()
        
    for word in words:
        val=""
        for s in word:
            val+=map_[ord(s)-ord('a')]
        res.add(val)
        
    return len(res)
'''