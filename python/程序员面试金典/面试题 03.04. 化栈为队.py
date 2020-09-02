class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input = []
        self.ouput = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.input.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.ouput:
            return self.ouput.pop()
        while self.input:
            self.ouput.append(self.input.pop())
        return self.ouput.pop()
    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.ouput:
            return self.ouput[-1]
        while self.input:
            self.ouput.append(self.input.pop())
        return self.ouput[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.input and not self.ouput