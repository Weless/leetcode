from typing import List
    class Solution:
        def findString(self, words: List[str], s: str) -> int:
            i,j = 0,len(words)-1
            while i<=j:
                mid = i+(j-i)//2
                tmp = mid
                while words[mid] == '' and mid < j: mid+=1 # 向右搜索
                if words[mid] == '': # 表示mid==j，右边未找到字符串
                    j = tmp - 1
                    continue
                if words[mid] == s: return mid
                if words[mid] < s : i = mid + 1
                else: j = mid -1
            return -1
S = Solution()
words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""]
s = "ball"
print(S.findString(words,s))