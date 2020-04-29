from typing import List

class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        def trackBack(nums,track):
            if len(track) == len(nums):
                res.append(track[:]) # 需要传递下track的拷贝，否则对track的修改会影响到结果
                return
            for i in nums:
                if i in track:
                    continue
                track.append(i)
                trackBack(nums,track)
                track.pop()
        res = []
        track = []
        trackBack(nums,track)
        return res


s = Solution()
print(s.permute([1,2,3]))