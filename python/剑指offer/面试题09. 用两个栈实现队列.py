class CQueue:

    def __init__(self):
        self.input = []
        self.output = []

    def appendTail(self, value: int) -> None:
        self.input.append(value)

    def deleteHead(self) -> int:
        if len(self.input) == 0 and len(self.output) == 0:
            return -1
        if self.output != []:
            return self.output.pop()
        while self.input != []:
            self.output.append(self.input.pop())
        return self.output.pop()