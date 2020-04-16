class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.res = []

    def addNum(self, num: int) -> None:
        self.res.append(num)
        self.res.sort()

    def findMedian(self) -> float:
        if len(self.res) % 2 != 0:
            return self.res[len(self.res)//2]
        else:
            l,r = 0,len(self.res)-1
            mid = (l+r)//2

            return (self.res[mid]+self.res[mid+1])/2