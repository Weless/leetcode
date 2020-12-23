# 首次解法
class Solution:
    def countLetters(self, S: str) -> int:
        from collections import defaultdict
        d = defaultdict(int)
        i = 0
        while i < len(S):
            d[S[i]]+=1
            j = i+1
            tmp = S[i]
            while j<len(S):
                if S[j] == S[i]:
                    tmp+=S[j]
                    d[tmp]+=1
                    j += 1
                else:
                    break
            i+=1
        ans = 0
        for v in d.values():
            ans +=v
        return ans

# 通项公式 n(n+1)/2  考虑：aaa的子串数为1+2+3
class Solution2:
    def countLetters(self, S: str) -> int:
        S = S + '!'
        count = 1
        total = 0
        for i in range(len(S) - 1):
            if S[i + 1] != S[i]:
                total += (count + 1) * count // 2
                count = 1
            else:
                count += 1
        return total

s = Solution2()
S = "aaaaaaaaaa"
print(s.countLetters(S))
