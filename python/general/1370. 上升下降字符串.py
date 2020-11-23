class Solution:
    def sortString(self, s: str) -> str:
        result = ''
        small = True
        while s != '':
            # print("s:",s)
            aset = set(s)
            if small:
                result += "".join(sorted(aset))
                small = False
            else:
                result += "".join(sorted(aset,reverse=True))
                small =True
            for i in aset:
                s = s.replace(i,"",1)
        return result

s = Solution()
astring= "aaaabbbbcccc"
print(s.sortString(astring))