from typing import List
from collections import deque
class AnimalShelf:

    def __init__(self):
        self.dogs = deque()
        self.cats = deque()

    def enqueue(self, animal: List[int]) -> None:
        if animal[1] == 0:
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def dequeueAny(self) -> List[int]:
        if self.cats and self.dogs:
            if self.cats[0] < self.dogs[0]:
                return self.cats.popleft()
            else:
                return self.dogs.popleft()
        elif self.cats:
            return self.cats.popleft()
        elif self.dogs:
            return self.dogs.popleft()
        else:
            return [-1,-1]

    def dequeueDog(self) -> List[int]:
        if self.dogs:
            return self.dogs.popleft()
        return [-1, -1]

    def dequeueCat(self) -> List[int]:
        if self.cats:
            return self.cats.popleft()
        return [-1, -1]
