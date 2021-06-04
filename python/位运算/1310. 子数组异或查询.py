from typing import List
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        for i,j in queries:
            res.append(self.xor(arr[i:j+1]))
        return res
    def xor(self,arr):
        if len(arr) == 1:
            return arr[0]
        res = 0
        for i in arr:
            res ^= i
        return res


# https://leetcode-cn.com/problems/xor-queries-of-a-subarray/solution/python3-qian-zhui-he-de-si-lu-chao-guo-9-fhux/
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        mp = {} #累计与或map
        curr = 0
        for i, v in enumerate(arr): #计算累计与或
            curr ^= v
            mp[i] = curr
        res = []

        for l, r in queries:
            if l == 0:
                # 从0 开始，直接取结果
                res.append(mp[r])
            else:
                # 通过 R 和 L-1 计算结果
                res.append(mp[l-1] ^ mp[r])
        return res

s = Solution()
arr = [4,8,2,10]
queries =  [[2,3],[1,3],[0,0],[0,3]]
print(s.xorQueries(arr,queries))