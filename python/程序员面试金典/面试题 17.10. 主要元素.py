from typing import List

# 摩尔投票法的基本原理是，维护一个众数major和一个频数count，
# 如果出现不同的数count减1，如果出现相同的数，count+1。
# 最终会发现，如果存在主要元素，那么最终count一定大于0，否则一定不存在主要元素。
# 但仅大于0也不一定能判断确实存在主要元素，因为如果数组为[4,3,3,2,2,2]，会发现count为2。
# 但是，2并不是主要元素，所以还要添加验证环节。

# 摩尔投票法
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return -1
        major, vote = None, 0
        for num in nums:
            if vote == 0:
                major = num
                vote += 1
            else:
                if num == major:
                    vote += 1
                else:
                    vote -= 1
        if vote <= 0:
            return -1

        identify = 0
        for num in nums:
            if num == major:
                identify += 1
                if identify > len(nums) / 2:
                    return major
