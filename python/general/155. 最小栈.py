class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.min) == 0 or self.min[-1] >= x:
            self.min.append(x)
    def pop(self) -> None:
        if len(self.stack) != 0:
            x = self.stack.pop()
            if x == self.min[-1]:
                self.min.pop()

    def top(self) -> int:
        if len(self.stack) != 0:
            return self.stack[-1]

    def getMin(self) -> int:
        if len(self.min) != 0:
            return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()