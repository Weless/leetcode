from typing import List
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        id = 0
        find_id = 0
        result = []
        idx = []
        while True:
            id = text.find(first + " " + second,find_id+1,len(text))
            print(id)
            find_id = id
            if id != -1:
                start = id + len(first) + len(second) + 1 + 1 # 两个空格
                idx.append(start)
            else:
                break
        # print(idx)
        for i in idx:
            j = i
            while True:
                if text[j] == " ":
                    break
                if j == len(text)-1:
                    break
                j+=1
            result.append(text[i:j+1].strip())
            # print(result)
        return resultfffff
sdfsf
s = Solution()
text = "alice is a good girl she is a good student"
first = "a"
second = "good"
print(s.findOcurrences(text, first, second))
