from collections import Counter, deque
from typing import List


class FirstUnique:
    def __init__(self, nums: List[int]):
        self.counter = Counter(nums)
        self.queue = deque(nums)

    def showFirstUnique(self) -> int:
        while self.queue and self.counter[self.queue[0]] != 1:
            self.queue.popleft()
        return -1 if not self.queue else self.queue[0]

    def add(self, value: int) -> None:
        self.counter[value] += 1
        self.queue.append(value)