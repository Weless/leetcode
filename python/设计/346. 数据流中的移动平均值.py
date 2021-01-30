class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        from collections import deque
        self.q = deque()
        self.size = size

    def next(self, val: int) -> float:
        if len(self.q)<self.size:
            self.q.append(val)
        else:
            self.q.popleft()
            self.q.append(val)
        return sum(self.q)/len(self.q)