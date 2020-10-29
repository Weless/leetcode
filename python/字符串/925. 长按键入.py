class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i,j = 0,0
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i+=1
                j+=1
            else:
                if j != 0 and typed[j] == typed[j-1]:
                    j+=1
                else:
                    return False
        return True if len(name) == i else False
s = Solution()
input = [("alex","aaleex"),("saeed","ssaaedd"),("leelee","lleeelee"),("laiden","laiden"),("alex","aaleelx"),("alex","alexxr"),("saeedi","ssaaeediixxxiii" )]
for x,y in input:
    print(s.isLongPressedName(x,y))