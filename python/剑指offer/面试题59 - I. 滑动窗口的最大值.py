from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if nums == [] or k == 0:
            return []
        result = []
        i = 0
        while i < len(nums)-k+1:
            # print(nums[i:i+k])
            result.append(max(nums[i:i+k]))
            i+=1
        return result


# 双向队列
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        from collections import deque
        queue = deque()
        i = 0
        while i < k:
            queue.append(nums[i])
            i+=1
        res = []
        res.append(max(queue))
        while i < len(nums):
            queue.popleft()
            queue.append(nums[i])
            res.append(max(queue))
            i+=1
        return res


# 单调队列
class Solution3:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import collections
        if not nums or k == 0: return []
        deque = collections.deque()
        for i in range(k): # 未形成窗口
            while deque and deque[-1] < nums[i]: deque.pop()
            deque.append(nums[i])
        res = [deque[0]]
        for i in range(k, len(nums)): # 形成窗口后
            if deque[0] == nums[i - k]: deque.popleft()
            while deque and deque[-1] < nums[i]: deque.pop()
            deque.append(nums[i])
            res.append(deque[0])
        return res

s = Solution3()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(s.maxSlidingWindow(nums,k))