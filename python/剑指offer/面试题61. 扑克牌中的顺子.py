from typing import List
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        if nums[0] == 0:
            for i in range(len(nums)-1):
                if nums[i]+1 != nums[i+1]:
                    return False
            return True
        else:
            zeroNum = 0
            cardNum = 0
            for i in range(len(nums)-1):
                if nums[i] == 0:
                    zeroNum += 1
                    cardNum += 1
                elif nums[i]+1 == nums[i+1]:
                    cardNum += 1
                else:
                    gap = nums[i+1] - nums[i]
                    if gap-1 > zeroNum:
                        return False
                    if zeroNum == 1:
                        
                if cardNum == 5:




