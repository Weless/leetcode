class Solution:
    def reformatNumber(self, number: str) -> str:
        tmp = ""
        for i in number:
            if i == "-" or i == " ":
                continue
            else:
                tmp+=i

        l = len(tmp)
        res = ""
        if l % 3 == 0 or l % 3 == 2:
            i = 1
            while i <= l:
                if i % 3 == 0:
                    res+=tmp[i]
                    res+="-"
                else:
                    res+=tmp[i]
                i+=1
        else:
            pass
            # i = 1
            # while i <= l-4:
            #     if i % 3 == 0:
            #         res += "-"
            #     else:
            #         res+=tmp[i]
            #     i+=1
            # res += tmp[i]+tmp[i+1]
            # res += "-"
            # res += tmp[i+2]+tmp[i+3]
        return res
s = Solution()
number = "1-23-45 6"
print(s.reformatNumber(number))
