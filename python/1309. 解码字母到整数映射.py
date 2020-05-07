class Solution:
    def freqAlphabets(self, s: str) -> str:
        import string
        signals = ['1','2','3','4','5','6','7','8','9','10#','11#','12#','13#','14#','15#','16#','17#',
                   '18#','19#','20#','21#','22#','23#','24#','25#','26#']
        aMap = dict(zip(signals,string.ascii_lowercase))

        l = len(s)
        i = 0
        result = s
        while i < l:
            print(i)
            if s[i] == "#":
                tmp = s[i-2:i+1]
                print(tmp)
                result = result.replace(tmp,aMap[tmp],1)
                print(s)
            i+=1
        for i in result:
            if i in aMap:
                result = result.replace(i,aMap[i],1)
        return result

s = Solution()
c1 = "10#11#12"
c2 = "1326#"
c3 = "25#"
print(s.freqAlphabets(c3))

class Solution2:
    def freqAlphabets(self, s: str) -> str:
        import string
        signals = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10#', '11#', '12#', '13#', '14#', '15#', '16#', '17#',
                   '18#', '19#', '20#', '21#', '22#', '23#', '24#', '25#', '26#']
        aMap = dict(zip(signals, string.ascii_lowercase))
        i = len(s) - 1
        result = ''
        while i >=0:
            if s[i] == "#":
                tmp = s[i-2] + s[i-1] + "#"
                i-=3
                result += aMap[tmp]
            else:
                result += aMap[s[i]]
                i-=1
        return result[::-1]

s2 = Solution2()
print(s2.freqAlphabets(c2))

## simple result

class Solution:
    def freqAlphabets(self, s: str) -> str:
        def get(st):
            return chr(int(st) + 96)

        i, ans = 0, ""
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                ans += get(s[i : i + 2])
                i += 2
            else:
                ans += get(s[i])
            i += 1
        return ans


