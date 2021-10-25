from typing import List


class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        t = 0
        for i in range(-6,11):
            t +=i+self.rand7()
        return

    def rand7(self):
        import random,time
        random.seed(time.time())
        return random.randint(1,7)



s = Solution()
print(s.rand7())


class GetMax:
    def getMax(self,arr):
        return self.process(arr,0,len(arr)-1)
    def process(self,arr,l,r):
        if l == r:
            return arr[l]
        mid = l + ((r-l)>>1) # 中点
        leftMax = self.process(arr,l,mid)
        rightMax = self.process(arr,l,mid)
        return max(leftMax,rightMax)
