from typing import List


class OrderedStream:
    def __init__(self, n: int):
        self.res = ['' for _ in range(n)]
        self.id = 1

    def insert(self, id: int, value: str) -> List[str]:

        self.res[id - 1] = value
        ans = []
        i = self.id - 1
        while i < len(self.res):
            if self.res[i] == "":
                self.id = i + 1
                break
            else:
                ans.append(self.res[i])
            i += 1
        return ans

