from typing import List

# 对称遍历
# 从左往右遍历累乘，结果保存在数组 ret 中，此时 ret[i]] 表示，A[i] 左边所有元素的乘积
# 然后从右往左遍历累乘，获取A[i] 右边所有元素的乘积
# 两边遍历之后得到的 ret，就是最终结果

class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        res = [0 for _ in range(len(a))]
        left = 1
        for i in range(len(a)):
            res[i] = left
            left = left * a[i]
        right = 1
        for i in range(len(a)-1,-1,-1):
            res[i] *= right
            right *= a[i]
        return res


s = Solution()
res = [1,2,3,4,5]
print(s.constructArr([1,2,3,4,5]))
