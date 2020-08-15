from typing import List

# 暴力，超时
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        if len(heights) == 1:
            return heights[0]
        area = []
        i = 0
        while i < len(heights):
            j = i + 1
            z = i - 1
            d1,d2=0,0
            while j < len(heights) and heights[j] >= heights[i]:
                j+=1
                d1+=1
            while z >= 0 and heights[z] >= heights[i]:
                z-=1
                d2+=1
            area.append(heights[i]*(1+d1+d2))
            i+=1
        # print(area)
        return max(area)

# 单调栈
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [0] * n, [0] * n

        mono_stack = list()
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)

        mono_stack = list()
        for i in range(n - 1, -1, -1):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            right[i] = mono_stack[-1] if mono_stack else n
            mono_stack.append(i)

        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return ans

s = Solution()
heights = [5,5,1,7,1,1,5,2,7,6]
print(s.largestRectangleArea(heights))