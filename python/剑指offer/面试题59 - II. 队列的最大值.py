class MaxQueue:

    def __init__(self):
        from collections import deque
        self.queue = deque()
        self.max = deque()

    def max_value(self) -> int:
        if len(self.queue) > 0:
            return self.max[0]
        else:
            return -1

    def push_back(self, value: int) -> None:
        self.queue.appendleft(value)
        if not self.max or value > self.max[0]:
            self.max.appendleft(value)

    def pop_front(self) -> int:
        if len(self.queue)>0:
            return self.queue.pop()
        else:
            return -1