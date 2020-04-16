class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minNum = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.minNum  == [] or x <= self.minNum[-1]:
            self.minNum.append(x)

    def pop(self) -> None:
         x = self.stack.pop()
         if x == self.minNum[-1]:
             self.minNum.pop()

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.minNum[-1]