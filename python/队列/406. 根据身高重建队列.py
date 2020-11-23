from typing import List
# 解题思路：先排序再插入
#      * 1.排序规则：按照先H高度降序，K个数升序排序
#      * 2.遍历排序后的数组，根据K插入到K的位置上
#      *
#      * 核心思想：高个子先站好位，矮个子插入到K位置上，前面肯定有K个高个子，矮个子再插到前面也满足K的要求

#  [7,0], [7,1], [6,1], [5,0], [5,2], [4,4]
#  再一个一个插入。
#  [7,0]
#  [7,0], [7,1]
#  [7,0], [6,1], [7,1]
#  [5,0], [7,0], [6,1], [7,1]
#  [5,0], [7,0], [5,2], [6,1], [7,1]
#  [5,0], [7,0], [5,2], [6,1], [4,4], [7,1]

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []
        for i in people:
            res.insert(i[1], i)
        return res

s = Solution()
people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(s.reconstructQueue(people))