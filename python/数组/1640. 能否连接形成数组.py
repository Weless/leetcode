from typing import List
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        i = 0
        while i<len(arr):
            find = False
            for alist in pieces:
                j = 0
                if alist[0] == arr[i]:
                    find = True
                    while j < len(alist):
                        if arr[i] != alist[j]:
                            return False
                        j+=1
                        i+=1
                    break
            if not find:
                return False
            if i == len(arr):
                return True

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        from collections import defaultdict
        d = defaultdict(list)
        for alist in pieces:
            d[alist[0]] = alist
        i = 0
        while i < len(arr):
            if arr[i] not in d:
                return False
            else:
                for j in d[arr[i]]:
                    if j != arr[i]:
                        return False
                    i+=1
        return i == len(arr)


s = Solution()
arr = [85]
pieces = [[85]]
print(s.canFormArray(arr,pieces))