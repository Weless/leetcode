from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        mask = 0
        for i in nums:
            mask ^= i
        diff = mask & (-mask)
        res = 0
        for i in nums:
            # 在该位不同，以这一位区分出两个数字，这里最终必然会只剩下一个数字
            if i & diff:
                res ^= i
        return [res,res^mask]