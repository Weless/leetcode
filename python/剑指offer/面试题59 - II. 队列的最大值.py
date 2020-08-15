class MaxQueue:

    def __init__(self):
        from collections import deque
        self.queue = deque()
        self.max = deque()

    def max_value(self) -> int:
        if self.max:
            return self.max[0]
        else:
            return -1


    def push_back(self, value: int) -> None:
        self.queue.append(value)
        while self.max and value > self.max[-1]:
            self.max.pop()
        self.max.append(value)

    def pop_front(self) -> int:
        if self.queue:
            x = self.queue.popleft()
            if x == self.max[0]:
                self.max.popleft()
            return x
        else:
            return -1