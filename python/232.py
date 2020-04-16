class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.out = []
        self.into = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.into.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """

        if self.empty():
            raise LookupError

        if self.out == []:
            while self.into != []:
                self.out.append(self.into.pop())
        return self.out.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.into != []:
            return self.into[0]
        elif self.out != []:
            return self.out[-1]
        else:
            raise LookupError



    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.into == [] and self.out == []


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
print(param_2,param_3,param_4)

