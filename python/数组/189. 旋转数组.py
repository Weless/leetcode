from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp = nums[:]
        for i,v in enumerate(nums):
            tmp[(i+k)%len(nums)] = v
        for i,_ in enumerate(nums):
            nums[i] = tmp[i]

class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        tmp = nums[-k:] + nums[:-k]
        for i,_ in enumerate(tmp):
            nums[i] = tmp[i]

class Solution3:
    def rotate(self, nums: List[int], k: int) -> None:
        i = 0
        l = len(nums)
        n = l
        tmp = 0
        while True:
            ni = (i+k)%l
            if i == 0:
                tmp = nums[ni]
                nums[ni] = nums[i]
                n-=1
            else:
                nums[ni],tmp =tmp,nums[ni]
                n-=1
            if n == 0:
                break
            i=ni
        print(nums)
s = Solution3()
print(s.rotate([-1,-100,3,99],2))