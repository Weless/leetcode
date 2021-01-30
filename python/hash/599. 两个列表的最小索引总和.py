from typing import List
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = dict()
        for i,v in enumerate(list1):
            d[v] = i

        res = []
        for i,v in enumerate(list2):
            if v in d:
                index = i + d[v]
                res.append((v,index))
        res.sort(key=lambda x:x[1])

        tmp_index = res[0][1]
        ans = []
        ans.append(res[0][0])
        for i in range(1,len(res)):
            if res[i][1] == tmp_index:
                ans.append(res[i][0])
        return ans

s = Solution()
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Shogun","Burger King"]
print(s.findRestaurant(list1,list2))



