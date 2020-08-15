class CQueue:

    def __init__(self):
        self.input = []
        self.output = []

    def appendTail(self, value: int) -> None:
        self.input.append(value)

    def deleteHead(self) -> int:
        if not self.input and not self.output:
            return -1
        if self.output:
            return self.output.pop()
        while self.input:
            self.output.append(self.input.pop())
        return self.output.pop()