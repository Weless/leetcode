class Solution:
    def countCharacters(self, words, chars):
        result  = 0
        for word in words:
            tag = 0
            tmp_chars = chars
            for i in word:
                if i not in tmp_chars:
                    tag = 1
                    break
                tmp_chars = tmp_chars.replace(i,'',1)
            if tag == 0:
                result += len(word)
        return result
s = Solution()
print(s.countCharacters( words=["hello","world","leetcode"], chars = "welldonehoneyr"))



### other answer

'''

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        res = 0

        for word in words:
            indicator = True
            for i in word:
                if word.count(i) > chars.count(i):
                    indicator = False
                    break
            if indicator:
                res += len(word)

        return res
        
'''