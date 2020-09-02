from typing import List
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start,end = -1,-1
        i,j = 0 ,len(nums)-1
        while i<j:
            # start和end确定就退出
            if start != -1 and end != -1:
                break
            # 下面主要用来确定start和end的位置
            if start == -1:
                if min(nums[i:j+1]) == nums[i]:
                    i+=1
                else:
                    start = i
            if end == -1:
                if max(nums[i:j+1]) == nums[j]:
                    j-=1
                else:
                    end = j
        # 本身就有序，比如[1,2,3,4]
        if start == -1 and end == -1:
            return 0
        return end - start + 1
s = Solution()
nums = [2,1]
print(s.findUnsortedSubarray(nums))

        