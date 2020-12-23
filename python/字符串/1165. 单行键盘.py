class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        d = dict()
        for i,v in enumerate(keyboard):
            d[v] = i
        tmp = keyboard[0] + word
        ans = 0
        pre = 0
        i = 1
        while i < len(tmp):
            t = d[tmp[i]]-pre
            ans += abs(t)
            pre = d[tmp[i]]
            i+=1
        return ans
s = Solution()
keyboard = "pqrstuvwxyzabcdefghijklmno"
word = "leetcode"
print(s.calculateTime(keyboard,word))